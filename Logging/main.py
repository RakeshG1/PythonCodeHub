import logging
import a

# Configure logging (applies globally)
logging.basicConfig(
    # filename="info.log",
    # filemode="a",
    level=logging.DEBUG, # Set logging level
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    logging.info("Started root code execution!")
    a.sample_error()