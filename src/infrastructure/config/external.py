
from pydantic_settings import BaseSettings, SettingsConfigDict

from ._default import CONFIG_DEFAULT


class External(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='EXTERNAL_', **CONFIG_DEFAULT)

    url: str
