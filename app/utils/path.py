from pathlib import Path

# Folder app/utils/
CURRENT_DIR = Path(__file__).resolve().parent

# Folder app/
APP_DIR = CURRENT_DIR.parent

# Root project
BASE_DIR = APP_DIR.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
TEST_DIR = BASE_DIR / "tests"