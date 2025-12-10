from pathlib import Path

from sqlalchemy import URL


class Database:
    @property
    def url(self):
        project_root = Path(__file__).parent.parent.parent.parent
        db_path = project_root / "database.db"
        
        return URL.create(
            drivername="sqlite+aiosqlite",
            database=str(db_path),
        ) 