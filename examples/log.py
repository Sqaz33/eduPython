import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def foo():
  try:
    logger.debug("trying 1 + 1")
    1 + 1
    logger.info("1 + 1")
    raise ValueError("1 + 1")
  except ValueError:
    logger.error("ValueError")

foo()