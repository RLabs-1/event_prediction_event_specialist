import argparse
import os
import yaml
import sys
from logger import setup_logger  # assuming you have a logger.py
import logging
from src.reasoning.performance import run_performance_reason


def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to the configuration YAML file"
    )

    args = parser.parse_args()
    return args.config

def config_exists(config_path):
    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Could not find config file: {config_path}")
    return True

def load_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config



if __name__ == "__main__":
    setup_logger()

    try:
        config_path = get_config()
        config_exists(config_path)
        config = load_config(config_path)
    except Exception as e:
        logging.error(e)
        sys.exit(1)

    logging.info(f"{config_path} loaded.")


    if config_path == "configs/performance.yaml":
        performance_bool, performance_output = run_performance_reason(config)
        if performance_bool:
            print(performance_output) # Return to main.py
            logging.info("Performance Specialist - Output Printed to Console.")























