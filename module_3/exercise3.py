# ==========================================
# Module 3 - Exercise 3
# Keep Asking Until Valid Input
# ==========================================


def display_tasks(tasks):
    """Display all tasks."""

    if len(tasks) == 0:
        print("Your task list is empty.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks):
        print(
            f"{index + 1}. "
            f"{task['description']} "
            f"[{task['status']}]"
        )

    print("------------------")


def get_task_number(tasks):
    """Keep asking until the user enters a valid task number."""

    while True:

        task_number = input(
            "Enter the task number: "
        )

        if not task_number.isdigit():
            print("Please enter a number.")
            continue

        task_index = int(task_number) - 1

        if task_index < 0 or task_index >= len(tasks):
            print("Invalid task number.")
            continue

        return task_index


def mark_task_complete(tasks):
    """Mark a task as completed."""

    if len(tasks) == 0:
        print("No tasks to mark.")
        return

    display_tasks(tasks)

    task_index = get_task_number(tasks)

    if tasks[task_index]["status"] == "completed":
        print("That task is already completed.")
        return

    tasks[task_index]["status"] = "completed"

    print(
        f'Marked '
        f'"{tasks[task_index]["description"]}" '
        f'as completed.'
    )


def main():
    """Run the Task Manager."""

    tasks = [
        {
            "description": "Learn Python",
            "status": "pending"
        },
        {
            "description": "Practice functions",
            "status": "pending"
        },
        {
            "description": "Build a project",
            "status": "pending"
        }
    ]

    print("=== Task Manager ===")

    while True:

        print("\nWhat would you like to do?")
        print("1. View tasks")
        print("2. Mark a task as complete")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            mark_task_complete(tasks)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()
