# ==========================================
# Module 4 - Exercise 1
# Testing JSON Errors
# ==========================================

import json


filename = "tasks.json"


try:

    with open(filename, "r") as f:
        tasks = json.load(f)

    print("Tasks loaded successfully.")

    print(tasks)

except FileNotFoundError:

    print("The tasks.json file does not exist.")

    print("Starting with an empty task list.")

    tasks = []

except json.JSONDecodeError:

    print("The tasks.json file contains invalid JSON.")

    print("Starting with an empty task list.")

    tasks = []


print("\nCurrent tasks:")

print(tasks)
