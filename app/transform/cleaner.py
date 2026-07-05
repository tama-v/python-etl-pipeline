from app.config.logger import logger


def transform(df):

    logger.info("Transform dimulai")

    df.columns = df.columns.str.lower()

    df = df.drop_duplicates()

    logger.info("Transform selesai")

    return df