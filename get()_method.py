# Creating a dictionary
student_grades = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78
}

# Using the get() method to retrieve values
grade_alice = student_grades.get('Alice', 'No grade found')
grade_david = student_grades.get('David', 'No grade found')

print(f"Alice's grade: {grade_alice}")  # Output: Alice's grade: 85
print(f"David's grade: {grade_david}")  # Output: David's grade: No grade found


# Alice's Grade: Since 'Alice' is a key in the student_grades dictionary, student_grades.get('Alice', 'No grade found') returns the value 85.
#
# David's Grade: Since 'David' is not a key in the dictionary, student_grades.get('David', 'No grade found') returns the default value 'No grade found'.

# diff ex.

print("\n")

# Creating a dictionary
employee_names = {
    101: 'John Doe',
    102: 'Jane Smith',
    103: 'Alice Johnson'
}

# Using the get() method to retrieve values
employee_101 = employee_names.get(101, 'Employee not found')
employee_104 = employee_names.get(104, 'Employee not found')

print(f"Employee 101: {employee_101}")  # Output: Employee 101: John Doe
print(f"Employee 104: {employee_104}")  # Output: Employee 104: Employee not found
