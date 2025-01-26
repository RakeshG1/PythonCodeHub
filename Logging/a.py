import logging

# Get logger for this module
logger = logging.getLogger(__name__)

def sample_error():
    try:
        1/0 # Intentional error
    except Exception as e:
        logger.error("Error raised")
        logger.error(e)
        # traceback.print_exc()  # Displays full error on console, not in the log
