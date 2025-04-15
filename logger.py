import logging
import os

def setup_logger(log_file="app.log", level=logging.INFO):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(module)s | %(message)s",
        handlers=[
            logging.FileHandler(log_path),
            logging.StreamHandler()
        ]
    )


    