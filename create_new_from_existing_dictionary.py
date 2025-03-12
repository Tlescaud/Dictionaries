# Creating a new list from an existing one can be done in several ways, depending on what you want to achieve. Here are some common methods:


#using list comprehensions

#example

# Example: Create a new list with squares of the original list elements
original_list = [1, 2, 3, 4]
new_list = [x ** 2 for x in original_list]
print(new_list)  # Output: [1, 4, 9, 16]


# using copy () method


#example

# Example: Create a copy of the original list
original_list = [1, 2, 3, 4]
new_list = original_list.copy()
print(new_list)  # Output: [1, 2, 3, 4]


# using slicing

# Example: Create a new list using slicing
original_list = [1, 2, 3, 4]
new_list = original_list[:]
print(new_list)  # Output: [1, 2, 3, 4]

#using the list () constructor

# Example: Create a new list using the list() constructor
original_list = [1, 2, 3, 4]
new_list = list(original_list)
print(new_list)  # Output: [1, 2, 3, 4]

#using the map function ()

# Example: Create a new list with double the value of original list elements
original_list = [1, 2, 3, 4]
new_list = list(map(lambda x: x * 2, original_list))
print(new_list)  # Output: [2, 4, 6, 8]


# filtering elements with filter ()

# Example: Create a new list with only even numbers from the original list
original_list = [1, 2, 3, 4, 5, 6]
new_list = list(filter(lambda x: x % 2 == 0, original_list))
print(new_list)  # Output: [2, 4, 6]


