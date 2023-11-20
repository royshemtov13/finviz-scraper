from typing import Optional

from from_root import from_root
from omegaconf import DictConfig, ListConfig, OmegaConf


def get_config(filename: Optional[str] = None) -> ListConfig | DictConfig:
    return OmegaConf.load(from_root("config") / filename)
