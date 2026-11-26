"""Code skeleton for the slides "Control Structures in Python".

Each cell (# %%) is labelled with the number of the slide it belongs to.
Replace every ___ with your own code, then run the cell.
"""

# %%
# Slide 6
# Define list of numbers from 1 to 10
numbers = ___

# Alternative
numbers = ___


# %%
# Slide 10
number = 5

if ___:
    print('Number is less than 10')


# %%
# Slide 11
number = 15

if ___:
    print('Number is less than 10')
else:
    print('Number is greater than or equal to 10')


# %%
# Slide 12
age = 19

if ___:
    print('Person is younger than 18')
elif ___:
    print('Person is 18')
else:
    print('Person is older than 18')


# %%
# Slide 13
number = 5

if ___:
    print('Number plus 5 is less than 10')

if not ___:
    print('Number plus 5 is 10 or more')

if ___ and ___:
    print('Number is greater than 3 and less than 10')


# %%
# Slide 14
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = numbers[1]

if ___:
    print(num)


# %%
# Slide 15
# Exercise 1

# 1.1 Print the minimum of both numbers
num1 = 8
num2 = 5

if ___:
    print(num1)
else:
    print(num2)

# 1.2 Print the grade based on the points received
points = 77

if ___:
    print('Grade 1')
elif ___:
    print('Grade 2')
elif ___:
    print('Grade 3')
elif ___:
    print('Grade 4')
else:
    print('Grade 5')


# %%
# Slide 16
# Exercise 2: first write down your answer, then run the cell to check it
print((1 + 2) == 3)

print(True != False)

num = 4
print((num != 0) and (20 / num > 0))

hour = 12
print((hour < 9) or (hour > 18))


# %%
# Slide 20
count = 0

while ___:
    count = ___
    print('Hello!')


# %%
# Slide 21
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for ___ in ___:
    print(num)


# %%
# Slide 22
# Iterate over a range
for i in range(___, ___, ___):
    print(i)

# Iterating by index of sequences
words = ['Iterating', 'by', 'index', 'of', 'sequences']

for i in ___:
    print(words[i])

# Simpler: iterate directly over the elements
for word in words:
    print(word)


# %%
# Slide 23
for letter in 'science':
    if ___:
        continue
    print('Current Letter:', letter)


for letter in 'science':
    if ___:
        break
    print('Current Letter:', letter)


for letter in 'science':
    pass
print('Last Letter:', letter)


# %%
# Slide 25
# Define list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterate over list
for ___ in ___:
    # Check remainder of num
    if ___:
        # Print num if even
        print(num)


# %%
# Slide 26
# Exercise 3
numbers = [5, 23, 37, 49, 50, 46, 30, 46, 70]

# 1. while loop
count = ___
list_size = ___
i = ___

while ___:
    if ___ > 30:
        count = ___
    i = ___

print(count)

# 2. for loop
count = 0

for ___ in ___:
    if ___:
        count = ___

print(count)
