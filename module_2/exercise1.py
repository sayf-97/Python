# Exercise 1
# Delete a Task

tasks = [
    {
        "description": "Learn Python",
        "status": "pending"
    },
    {
        "description": "Build a Task Manager",
        "status": "pending"
    },
    {
        "description": "Practice dictionaries",
        "status": "completed"
    }
]

print("=== Task Manager ===")

while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Exit")
    print("5. Delete a task")

    choice = input("\nEnter your choice (1-5): ")

    # Add a task
    if choice == "1":

        description = input("Enter the task description: ")

        task = {
            "description": description,
            "status": "pending"
        }

        tasks.append(task)

        print(f'Added: "{description}"')

    # View all tasks

    elif choice == "2":

        if len(tasks) == 0:
            print("Your task list is empty.")

        else:
            print("\n--- Your Tasks ---")

            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}. "
                    f"{task['description']} "
                    f"[{task['status']}]"
                )

            print("------------------")

    # Mark task as complete
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to mark.")

        else:
            print("\n--- Your Tasks ---")

            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}. "
                    f"{task['description']} "
                    f"[{task['status']}]"
                )

            print("------------------")

            task_number = input(
                "Enter the task number to mark complete: "
            )

            if task_number.isdigit():

                task_index = int(task_number) - 1

                if 0 <= task_index < len(tasks):

                    if tasks[task_index]["status"] == "completed":
                        print("That task is already completed.")

                    else:
                        tasks[task_index]["status"] = "completed"

                        print(
                            f'Marked '
                            f'"{tasks[task_index]["description"]}" '
                            f'as completed.'
                        )

                else:
                    print("Invalid task number.")

            else:
                print("Please enter a valid number.")

    elif choice == "4":

        print("Goodbye!")
        break

    # Delete a task
    elif choice == "5":

        if len(tasks) == 0:
            print("There are no tasks to delete.")

        else:
            print("\n--- Your Tasks ---")

            for index, task in enumerate(tasks):
                print(
                    f"{index + 1}. "
                    f"{task['description']} "
                    f"[{task['status']}]"
                )

            print("------------------")

            task_number = input(
                "Enter the task number to delete: "
            )

            if task_number.isdigit():

                task_index = int(task_number) - 1

                if 0 <= task_index < len(tasks):

                    deleted_task = tasks.pop(task_index)

                    print(
                        f'Deleted: '
                        f'"{deleted_task["description"]}"'
                    )

                else:
                    print("Invalid task number.")

            else:
                print("Please enter a valid number.")

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")