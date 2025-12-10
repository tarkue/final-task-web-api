
from pydantic_settings import BaseSettings, SettingsConfigDict

from ._default import CONFIG_DEFAULT


class Nats(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='NATS_', **CONFIG_DEFAULT)

    host: str
    port: int
    
    @property
    def url(self):
        return f"nats://{self.host}:{self.port}"
