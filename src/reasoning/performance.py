import os
import sys
import json
import torch
from transformers import pipeline

def load_json(filename="logs.json"):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    log_path = os.path.join(project_root, filename)

    if not os.path.exists(log_path):
        raise FileNotFoundError(f"'{filename}' not found in project root: {project_root}")

    with open(log_path, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON in '{filename}': {e}")

    return data


def run_performance_reason(config):

    try:
        logs = load_json()
    except FileNotFoundError as fnf_error:
        raise fnf_error
    except ValueError as val_error:
        raise val_error


    pipe = pipeline(
        "text-generation",
        model=config["model"]["name"],
        max_new_tokens=config["model"]["inference"]["max_tokens"],
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )

    print("Injected prompt_starter")

    output = pipe(str(logs) + config["performance_detection"]["prompt_starter"])

    if output == "No":
        return False , "No performance predictions were found."

    list_of_keywords = pipe(config["performance_detection"]["prompt_filter"] + " " + config["performance_detection"]["performance_keywords"])

    return True, pipe(config["performance_detection"]["prompt_template"] + str(list_of_keywords))













