# Nerry Koukoui

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Reading Group_A
'''n = int(input("Enter the number of elements to add to Group_A: "))
Group_A = ['a', 'a', 'b', 'a', 'b']
for i in range(n):
    Group_A.append(input("Enter an element for Group_A: ").strip())

# Reading Group_B and checking occurrences
m = int(input("Enter the number of elements for Group_B: "))
Group_B = ['a', 'a']
for j in range(m):
    word = input("Enter an element for Group_B: ").strip()
    indices = [i + 1 for i in range(len(Group_A)) if Group_A[i] == word]
    if indices:
        print(" ".join(map(str, indices)))
    else:
        print(-1)'''

# Reading Group_A
'''n = int(input("Enter the number of elements to add to Group_A: "))
Group_A = ['a', 'a', 'b', 'a', 'b']
for i in range(n):
    Group_A.append(input("Enter an element for Group_A: ").strip())

# Reading Group_B and checking occurrences
m = int(input("Enter the number of elements for Group_B: "))
Group_B = ['a', 'a']
results = []

for j in range(m):
    word = input("Enter an element for Group_B: ").strip()
    indices = [i + 1 for i in range(len(Group_A)) if Group_A[i] == word]
    if indices:
        results.append(" ".join(map(str, indices)))
    else:
        results.append("-1")

# Print results
for result in results:
    print(result)
'''


# Reading Group_A
Group_A = ['a', 'a', 'b', 'a', 'b']
n = int(input("Enter the number of elements to add to Group_A: "))
for i in range(n):
    Group_A.append(input("Enter an element for Group_A: ").strip())

# Reading Group_B and checking occurrences
m = int(input("Enter the number of elements for Group_B: "))
results = []

for j in range(m):
    word = input("Enter an element for Group_B: ").strip()
    indices = [i + 1 for i in range(len(Group_A)) if Group_A[i] == word]
    if indices:
        results.append(" ".join(map(str, indices)))
    else:
        results.append("-1")

# Print results
for result in results:
    print(result)


