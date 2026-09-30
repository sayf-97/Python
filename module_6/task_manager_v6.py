# task_manager_v6.py
# Module 6: The TaskManager
# A complete object-oriented Task Manager with:
# - Task objects
# - JSON persistence
# - Add tasks
# - View tasks
# - Mark tasks complete
# - Delete tasks
# - Filter pending tasks
# - Sort tasks by priority
# - Priority
# - Due dates


import json


# ============================================================
# TASK CLASS
# ============================================================

class Task:
    """Represents a single task."""

    def __init__(
        self,
        description,
        status="pending",
        priority="medium",
        due_date=None
    ):
        self.description = description
        self.status = status
        self.priority = priority
        self.due_date = due_date

    def __str__(self):
        """Return a readable string representation of the task."""

        parts = [
            f"{self.description} [{self.status}]"
        ]

        parts.append(
            f"priority: {self.priority}"
        )

        if self.due_date:
            parts.append(
                f"due: {self.due_date}"
            )

        return " | ".join(parts)

    def mark_complete(self):
        """Mark this task as completed."""

        self.status = "completed"

    def is_complete(self):
        """Return True if the task is completed."""

        return self.status == "completed"

    def to_dict(self):
        """Convert the Task object into a dictionary."""

        return {
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary."""

        return cls(
            description=data["description"],
            status=data.get("status", "pending"),
            priority=data.get("priority", "medium"),
            due_date=data.get("due_date")
        )


# ============================================================
# TASK MANAGER CLASS
# ============================================================

class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []

        # Load existing tasks when the manager starts.
        self._load_tasks()

    # --------------------------------------------------------
    # INTERNAL METHODS
    # --------------------------------------------------------

    def _load_tasks(self):
        """Load tasks from the JSON file."""

        try:
            with open(self.filename, "r") as f:
                tasks_data = json.load(f)

            self.tasks = [
                Task.from_dict(data)
                for data in tasks_data
            ]

            print(
                f"Loaded {len(self.tasks)} task(s) "
                f"from {self.filename}."
            )

        except FileNotFoundError:
            print(
                "No save file found. "
                "Starting with an empty task list."
            )

            self.tasks = []

        except json.JSONDecodeError:
            print(
                "Save file is corrupted. "
                "Starting with an empty task list."
            )

            self.tasks = []

    def _save_tasks(self):
        """Save all tasks to the JSON file."""

        tasks_data = [
            task.to_dict()
            for task in self.tasks
        ]

        try:
            with open(self.filename, "w") as f:
                json.dump(
                    tasks_data,
                    f,
                    indent=4
                )

            print(
                f"Saved {len(self.tasks)} task(s)."
            )

        except IOError as e:
            print(
                f"Error saving tasks: {e}"
            )

    # --------------------------------------------------------
    # PUBLIC METHODS
    # --------------------------------------------------------

    def add_task(self):
        """Interactively add a new task."""

        description = input(
            "Enter the task description: "
        )

        if not description.strip():
            print(
                "Task description cannot be empty."
            )
            return

        # Ask for priority.
        priority = input(
            "Priority (high/medium/low) [medium]: "
        ).strip().lower()

        if priority not in (
            "high",
            "medium",
            "low"
        ):
            print(
                "Invalid priority. "
                "Using medium."
            )
            priority = "medium"

        # Ask for due date.
        due_date = input(
            "Due date (YYYY-MM-DD) "
            "or press Enter for none: "
        ).strip()

        if due_date == "":
            due_date = None

        # Create the Task object.
        task = Task(
            description=description,
            priority=priority,
            due_date=due_date
        )

        self.tasks.append(task)

        # Save automatically.
        self._save_tasks()

        print(
            f'Added: "{description}"'
        )

    def view_tasks(self):
        """Display all tasks."""

        if len(self.tasks) == 0:
            print(
                "Your task list is empty."
            )
            return

        print("\n--- Your Tasks ---")

        for index, task in enumerate(self.tasks):
            print(
                f"{index + 1}. {task}"
            )

        print("------------------")

    def view_pending(self):
        """Display only pending tasks."""

        pending_tasks = [
            task
            for task in self.tasks
            if task.status == "pending"
        ]

        if len(pending_tasks) == 0:
            print(
                "There are no pending tasks."
            )
            return

        print("\n--- Pending Tasks ---")

        for index, task in enumerate(pending_tasks):
            print(
                f"{index + 1}. {task}"
            )

        print("---------------------")

    def mark_task_complete(self):
        """Show tasks and mark one as completed."""

        if len(self.tasks) == 0:
            print(
                "No tasks to mark."
            )
            return

        self.view_tasks()

        task_number_str = input(
            "Enter the task number to mark complete: "
        )

        if not task_number_str.isdigit():
            print(
                "Please enter a valid number."
            )
            return

        task_index = int(task_number_str) - 1

        if (
            task_index < 0
            or task_index >= len(self.tasks)
        ):
            print(
                "Invalid task number."
            )
            return

        task = self.tasks[task_index]

        if task.is_complete():
            print(
                "That task is already completed."
            )
            return

        task.mark_complete()

        self._save_tasks()

        print(
            f'Marked "{task.description}" '
            f"as completed."
        )

    def delete_task(self):
        """Show tasks and delete one."""

        if len(self.tasks) == 0:
            print(
                "No tasks to delete."
            )
            return

        self.view_tasks()

        task_number_str = input(
            "Enter the task number to delete: "
        )

        if not task_number_str.isdigit():
            print(
                "Please enter a valid number."
            )
            return

        task_index = int(task_number_str) - 1

        if (
            task_index < 0
            or task_index >= len(self.tasks)
        ):
            print(
                "Invalid task number."
            )
            return

        removed_task = self.tasks.pop(task_index)

        self._save_tasks()

        print(
            f'Deleted: "{removed_task.description}"'
        )

    def sort_by_priority(self):
        """Display tasks sorted by priority."""

        if len(self.tasks) == 0:
            print(
                "Your task list is empty."
            )
            return

        # Lower number = higher priority.
        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2
        }

        sorted_tasks = sorted(
            self.tasks,
            key=lambda task: priority_order.get(
                task.priority,
                1
            )
        )

        print("\n--- Tasks by Priority ---")

        for index, task in enumerate(sorted_tasks):
            print(
                f"{index + 1}. {task}"
            )

        print("-------------------------")

    # --------------------------------------------------------
    # MAIN APPLICATION LOOP
    # --------------------------------------------------------

    def run(self):
        """Run the interactive Task Manager."""

        print("=== Task Manager ===\n")

        while True:

            print("\nWhat would you like to do?")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Mark a task as complete")
            print("4. Delete a task")
            print("5. View pending tasks")
            print("6. View tasks sorted by priority")
            print("7. Exit")

            choice = input(
                "\nEnter your choice (1-7): "
            )

            # Add task
            if choice == "1":
                self.add_task()

            # View all tasks
            elif choice == "2":
                self.view_tasks()

            # Complete task
            elif choice == "3":
                self.mark_task_complete()

            # Delete task
            elif choice == "4":
                self.delete_task()

            # View pending tasks
            elif choice == "5":
                self.view_pending()

            # Sort by priority
            elif choice == "6":
                self.sort_by_priority()

            # Exit
            elif choice == "7":
                self._save_tasks()
                print("Goodbye!")
                break

            # Invalid menu choice
            else:
                print(
                    "Invalid choice. "
                    "Please enter 1, 2, 3, 4, 5, 6, or 7."
                )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    app = TaskManager()
    app.run()
