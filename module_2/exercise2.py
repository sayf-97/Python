# Exercise 2
# Experiment with Dictionaries

# Create a dictionary representing a person.
person = {
    "name": "Sayf",
    "age": 29,
    "city": "Mauritius"
}

# Access values by key
print("Name:")
print(person["name"])

print("\nAge:")
print(person["age"])

print("\nCity:")
print(person["city"])

# Add a new key
person["job"] = "Student"

print("\nPerson after adding job:")
print(person)


# Change an existing value
person["age"] = 26

print("\nPerson after changing age:")
print(person)

# Access a key that does not exist
# The following line will produce a KeyError.
# Uncomment it to experiment.

# print(person["phone"])

# Using .get()

phone = person.get("phone", "No phone number")

print("\nPhone:")
print(phone)


# Try another missing key with .get()

country = person.get("country", "No country provided")

print("\nCountry:")
print(country)
