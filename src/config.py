import os
from dataclasses import dataclass
from datetime import date
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "dev")
    batch_date: str = os.getenv("BATCH_DATE", date.today().isoformat())
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
