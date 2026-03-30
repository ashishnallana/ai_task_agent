import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """Loads tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
