# Exercise 2
# Save Confirmation

import json


def save_tasks(tasks, filename):
    """Save tasks and report how many were saved."""

    try:

        with open(filename, "w") as f:
            json.dump(tasks, f, indent=4)

        print(
            f"Saved {len(tasks)} task(s) "
            f"to {filename}."
        )

    except IOError as e:

        print(f"Error saving tasks: {e}")


tasks = [
    {
        "description": "Learn Python",
        "status": "pending"
    },
    {
        "description": "Practice JSON",
        "status": "pending"
    },
    {
        "description": "Build Task Manager",
        "status": "completed"
    }
]


save_tasks(tasks, "exercise_tasks.json")
