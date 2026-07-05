import pandas as pd

from app.config.logger import logger
from app.config.settings import DATA_DIR


def extract():

    logger.info("Reading CSV")

    csv_file = DATA_DIR / "mahasiswa.csv"

    df = pd.read_csv(csv_file)

    logger.info(f"{len(df)} rows loaded")

    return df