# Module 3 - Exercise 1
# Delete Task Using a Function

def display_tasks(tasks):
    """Display all tasks."""

    if len(tasks) == 0:
        print("Your task list is empty.")
        return

    print("\n--- Your Tasks ---")

    for index, task in enumerate(tasks):
        print(
            f"  {index + 1}. "
            f"{task['description']} "
            f"[{task['status']}]"
        )

    print("------------------")


def add_task(tasks):
    """Add a new task."""

    description = input("Enter the task description: ")

    if description.strip() == "":
        print("Task description cannot be empty.")
        return

    task = {
        "description": description,
        "status": "pending"
    }

    tasks.append(task)

    print(f'Added: "{description}"')


def mark_task_complete(tasks):
    """Mark a task as completed."""

    if len(tasks) == 0:
        print("No tasks to mark.")
        return

    display_tasks(tasks)

    task_number = input(
        "Enter the task number to mark complete: "
    )

    if not task_number.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    if tasks[task_index]["status"] == "completed":
        print("That task is already completed.")
        return

    tasks[task_index]["status"] = "completed"

    print(
        f'Marked '
        f'"{tasks[task_index]["description"]}" '
        f'as completed.'
    )


def delete_task(tasks):
    """Delete a task from the task list."""

    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    display_tasks(tasks)

    task_number = input(
        "Enter the task number to delete: "
    )

    if not task_number.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(task_number) - 1

    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    deleted_task = tasks.pop(task_index)

    print(
        f'Deleted: "{deleted_task["description"]}"'
    )


def main():
    """Run the Task Manager."""

    tasks = []

    print("=== Task Manager ===\n")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as complete")
        print("4. Exit")
        print("5. Delete a task")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            mark_task_complete(tasks)

        elif choice == "4":
            print("Goodbye!")
            break

        elif choice == "5":
            delete_task(tasks)

        else:
            print(
                "Invalid choice. "
                "Please enter 1, 2, 3, 4, or 5."
            )


main()
