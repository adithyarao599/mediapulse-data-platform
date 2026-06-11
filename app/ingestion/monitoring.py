from app.utils.logger import get_logger

logger = get_logger()


def log_pipeline_status(source, status):

    logger.info(f"{source}: {status}")
