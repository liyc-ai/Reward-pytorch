import os
from os.path import exists, join

import hydra
import torch as th
from omegaconf import DictConfig, OmegaConf
from rlplugs.drls.env import get_env_info, make_env, reset_env_fn
from rlplugs.logger import TBLogger
from rlplugs.net.ptu import clean_cuda, load_torch_model, save_torch_model, set_torch
from stable_baselines3.common.utils import set_random_seed

import rwpyt

WORK_DIR = os.getcwd()


@hydra.main(
    config_path=join(WORK_DIR, "conf"),
    config_name="run_exp",
    version_base="1.3.1",
)
def main(cfg: DictConfig):
    cfg.work_dir = WORK_DIR
    # set torch and GPU
    clean_cuda()
    set_torch(getattr(th, cfg.default_th_dtype))
    set_random_seed(cfg.seed, th.cuda.is_available() and cfg.device.startswith("cuda"))

    # setup logger
    logger = TBLogger(
        work_dir=WORK_DIR,
        args=OmegaConf.to_object(cfg),
        record_param=cfg.log.record_param,
    )

    # setup environment
    train_env, eval_env = make_env(cfg.env.id), make_env(cfg.env.id)
    OmegaConf.update(cfg, "env[info]", get_env_info(eval_env), merge=False)

    # setup agent
    agent = rwpyt.make(cfg, logger)
    if cfg.preload_model_path is not None and exists(cfg.preload_model_path):
        logger.console.info(
            f"Successfully load model from {load_torch_model(agent.models, join(cfg.work_dir, cfg.preload_model_path))}"
        )

    # learning
    agent.learn(train_env, eval_env, reset_env_fn)

    # save the final model
    logger.console.info(
        f"Successfully save model to {save_torch_model(agent.models, logger.ckpt_dir, 'final_model.pt')}"
    )
