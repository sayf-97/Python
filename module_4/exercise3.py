# Exercise 3
# Save Only When Exiting

import json


TASKS_FILE = "exercise_tasks.json"


def load_tasks(filename):

    try:

        with open(filename, "r") as f:
            return json.load(f)

    except FileNotFoundError:

        return []

    except json.JSONDecodeError:

        print("Save file is corrupted.")

        return []


def save_tasks(tasks, filename):

    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

    print("Tasks saved.")


def display_tasks(tasks):

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


def add_task(tasks):

    description = input(
        "Enter the task description: "
    )

    if description.strip() == "":
        print("Task description cannot be empty.")
        return

    tasks.append(
        {
            "description": description,
            "status": "pending"
        }
    )

    print("Task added.")


def mark_task_complete(tasks):

    if len(tasks) == 0:
        print("No tasks.")
        return

    display_tasks(tasks)

    number = input(
        "Enter task number to complete: "
    )

    if not number.isdigit():
        print("Invalid number.")
        return

    index = int(number) - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return

    tasks[index]["status"] = "completed"

    print("Task completed.")


def main():

    tasks = load_tasks(TASKS_FILE)

    while True:

        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            add_task(tasks)

        elif choice == "2":

            display_tasks(tasks)

        elif choice == "3":

            mark_task_complete(tasks)

        elif choice == "4":

            save_tasks(tasks, TASKS_FILE)

            print("Goodbye!")

            break

        else:

            print("Invalid choice.")


main()
