from smolagents import tool
from database import load_tasks, save_tasks


@tool
def add_task(task_name: str, due_date: str, time: str) -> str:
    """
    Adds a new task to the user's task manager database.

    Args:
        task_name: The description or name of the task.
        due_date: The date the task is due.
        time: The time the task is due.
    """
    tasks = load_tasks()

    # Smarter ID generation to prevent duplicates after deletion
    new_id = max([t['id'] for t in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "task_name": task_name,
        "due_date": due_date,
        "time": time,
        "status": "pending"
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return f"Success! Task '{task_name}' added as ID {new_id}."


@tool
def list_tasks() -> str:
    """
    Retrieves all current tasks. ALWAYS use this tool first when a user asks to 
    delete, complete, or edit a task so you can find the correct Task ID.
    """
    tasks = load_tasks()
    if not tasks:
        return "No tasks found."
    return "\n".join([f"ID {t['id']}: {t['task_name']} | Due: {t['due_date']} @ {t['time']} | Status: {t['status']}" for t in tasks])


@tool
def delete_task(task_id: int) -> str:
    """
    Deletes a task from the database.

    Args:
        task_id: The integer ID of the task to delete.
    """
    tasks = load_tasks()
    initial_count = len(tasks)
    tasks = [t for t in tasks if t['id'] != task_id]

    if len(tasks) == initial_count:
        return f"Error: Task ID {task_id} not found."

    save_tasks(tasks)
    return f"Success! Task ID {task_id} deleted."


@tool
def update_task_status(task_id: int, status: str) -> str:
    """
    Updates the status of a specific task.

    Args:
        task_id: The integer ID of the task.
        status: The new status (MUST be either 'completed' or 'pending').
    """
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = status
            save_tasks(tasks)
            return f"Success! Task ID {task_id} marked as {status}."
    return f"Error: Task ID {task_id} not found."


@tool
def edit_task(task_id: int, task_name: str, due_date: str, time: str) -> str:
    """
    Edits the details of an existing task. Pass 'KEEP' for any argument you DO NOT want to change.

    Args:
        task_id: The integer ID of the task to edit.
        task_name: The new task description, or 'KEEP'.
        due_date: The new due date, or 'KEEP'.
        time: The new time, or 'KEEP'.
    """
    tasks = load_tasks()
    for t in tasks:
        if t['id'] == task_id:
            if task_name != 'KEEP':
                t['task_name'] = task_name
            if due_date != 'KEEP':
                t['due_date'] = due_date
            if time != 'KEEP':
                t['time'] = time
            save_tasks(tasks)
            return f"Success! Task ID {task_id} updated."
    return f"Error: Task ID {task_id} not found."
