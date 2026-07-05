from pathlib import Path
from dotenv import load_dotenv
import os

# Root project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env
load_dotenv(BASE_DIR / ".env")

# Database
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Folder
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
TEST_DIR = BASE_DIR / "tests"