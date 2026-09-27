# Exercise 4
# Search Tasks

def search_tasks(tasks, search_text):
    """Return tasks whose descriptions contain the search text."""

    results = []

    for task in tasks:

        if search_text.lower() in task["description"].lower():
            results.append(task)

    return results


def display_tasks(tasks):
    """Display a list of tasks."""

    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\n--- Tasks ---")

    for index, task in enumerate(tasks):
        print(
            f"{index + 1}. "
            f"{task['description']} "
            f"[{task['status']}]"
        )

    print("-------------")


def main():
    """Run the task search program."""

    tasks = [
        {
            "description": "Buy groceries",
            "status": "pending"
        },
        {
            "description": "Read Python book",
            "status": "pending"
        },
        {
            "description": "Practice Python functions",
            "status": "completed"
        },
        {
            "description": "Walk the dog",
            "status": "pending"
        },
        {
            "description": "Build Python project",
            "status": "pending"
        }
    ]

    print("=== Task Search ===")

    search_text = input(
        "Enter text to search for: "
    )

    results = search_tasks(tasks, search_text)

    print("\nSearch results:")

    display_tasks(results)


main()
