from pydantic_settings import BaseSettings, SettingsConfigDict

from ._default import CONFIG_DEFAULT


class BackgroundTask(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='BACKGROUND_TASK_', **CONFIG_DEFAULT)

    url: str
    interval_in_minutes: int