# Exercise 1 - Modify and Run

# Two default tasks
tasks = ["Learn Python", "Build a Task Manager"]

print("Tasks before adding:")
print(tasks)

# Add a new task
new_task = input("\nEnter a new task: ")
tasks.append(new_task)

print("\nTasks after adding:")
print(tasks)
