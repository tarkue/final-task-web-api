from dataclasses import dataclass

from .app import App
from .background_task import BackgroundTask
from .database import Database
from .external import External
from .nats import Nats


@dataclass
class EnvironmentConfig:
    app: App = App()
    nats = Nats()
    database: Database = Database()
    external: External = External()
    background_task: BackgroundTask = BackgroundTask()


env = EnvironmentConfig()