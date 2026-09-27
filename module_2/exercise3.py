# Exercise 3
# Lists of Lists vs Dictionaries

tasks_as_lists = [
    ["Buy groceries", "pending"],
    ["Read a book", "pending"],
    ["Walk the dog", "completed"]
]

print("=== LIST OF LISTS ===")
print(tasks_as_lists)

print("\nFirst task:")
print(tasks_as_lists[0])

print("\nFirst task description:")
print(tasks_as_lists[0][0])

print("\nFirst task status:")
print(tasks_as_lists[0][1])

# Change the status
tasks_as_lists[0][1] = "completed"

print("\nAfter completing the first task:")
print(tasks_as_lists)


# List of Dictionaries
tasks_as_dictionaries = [
    {
        "description": "Buy groceries",
        "status": "pending"
    },
    {
        "description": "Read a book",
        "status": "pending"
    },
    {
        "description": "Walk the dog",
        "status": "completed"
    }
]

print("\n=== LIST OF DICTIONARIES ===")

print(tasks_as_dictionaries)

print("\nFirst task:")
print(tasks_as_dictionaries[0])

print("\nFirst task description:")
print(tasks_as_dictionaries[0]["description"])

print("\nFirst task status:")
print(tasks_as_dictionaries[0]["status"])

tasks_as_dictionaries[0]["status"] = "completed"

print("\nAfter completing the first task:")
print(tasks_as_dictionaries)


# Compare the two approaches

print("\n=== COMPARISON ===")

print("\nList of lists:")
print(tasks_as_lists[0][0])

print("\nDictionary:")
print(tasks_as_dictionaries[0]["description"])
