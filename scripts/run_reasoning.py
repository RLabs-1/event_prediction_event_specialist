import argparse
import os
import yaml
import torch
import sys

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

    config_path = get_config()
    config_exists(config_path)
    config = load_config(config_path)

    print("Loaded Config Files")

    performance_bool, performance_output = run_performance_reason(config)
    if performance_bool:
        print(performance_output)























