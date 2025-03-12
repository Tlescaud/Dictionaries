# examples

# Creating a dictionary
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing values using keys
print(my_dict['name'])  # Output: Alice
print(my_dict['age'])   # Output: 30

# Adding a new key-value pair
my_dict['profession'] = 'Engineer'
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}

# Updating a value
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}

# Removing a key-value pair
del my_dict['city']
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'profession': 'Engineer'}

# Iterating over a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 31
# profession: Engineer
