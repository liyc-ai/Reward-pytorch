from typing import Any, Callable, Dict

from gymnasium import Env
from omegaconf import DictConfig
from rlplugs.logger import LoggerType

from rwpyt.irl.gail import GAILAgent


class AIRLAgent(GAILAgent):
    def __init__(self, cfg: DictConfig, logger: LoggerType):
        super().__init__(cfg, logger)

    def setup_model(self):
        ...

    def learn(self, train_env: Env, eval_env: Env, reset_env_fn_fn: Callable[..., Any]):
        ...

    def update(self) -> Dict:
        ...
