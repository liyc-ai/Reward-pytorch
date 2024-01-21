from typing import Dict

from omegaconf import DictConfig
from rlplugs.logger import LoggerType

from rwpyt._base import BaseRWAgent
from rwpyt.irl import *
from rwpyt.preference import *

AGENTS: Dict[str, BaseRWAgent] = {
    "gail": GAILAgent,
    "airl": AIRLAgent,
    "dac": DACAgent,
    "value_dice": ValueDiceAgent,
    "iq_learn": IQLearnAgent,
    "cpl": CPLAgent,
    "drex": DREXAgent,
    "ipl": IPLAgent,
    "pt": PTAgent,
    "trex": TREXAgent,
}


def make(cfg: DictConfig, logger: LoggerType) -> BaseRWAgent:
    """To instantiate an agent"""

    def _get_agent(cfg: DictConfig, logger: LoggerType) -> BaseRWAgent:
        """For python annotations"""
        return AGENTS[cfg.agent.algo](cfg, logger)

    agent = _get_agent(cfg, logger)
    agent.setup_model()
    return agent


__version__ = "1.0.0"

__all__ = ["AGENTS", "AIRLAgent", "make"]
