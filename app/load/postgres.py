from app.config.database import engine
from app.config.logger import logger


def load(df):

    logger.info("Load dimulai")

    df.to_sql(
        "mahasiswa",
        con=engine,
        if_exists="append",
        index=False,
    )

    logger.info("Load selesai")