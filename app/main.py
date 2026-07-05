from app.config.logger import logger

from app.extract import extract
from app.transform import transform
from app.load import load


logger.info("=" * 50)
logger.info("ETL DIMULAI")
logger.info("=" * 50)

try:

    df = extract()

    df = transform(df)

    load(df)

    logger.info("ETL berhasil")

except Exception:

    logger.exception("ETL gagal")

finally:

    logger.info("=" * 50)
    logger.info("ETL selesai")
    logger.info("=" * 50)

print("Program selesai.")