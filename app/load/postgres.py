from app.config.database import get_engine
from app.config.logger import logger


def load(df):

    logger.info("Load dimulai")

    engine = get_engine()

    df.to_sql(
        "mahasiswa",
        con=engine,
        if_exists="append",
        index=False,
    )

    logger.info("Load selesai")