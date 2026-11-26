"""Solutions for the slides "Control Structures in Python".

Each cell (# %%) is labelled with the number of the slide it belongs to.
Run the cells one at a time, e.g. in VS Code, Spyder or PyCharm.
"""

# %%
# Slide 6
# Define list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Alternative
numbers = list(range(1, 11))


# %%
# Slide 10
number = 5

if number < 10:
    print('Number is less than 10')


# %%
# Slide 11
number = 15

if number < 10:
    print('Number is less than 10')
else:
    print('Number is greater than or equal to 10')


# %%
# Slide 12
age = 19

if age < 18:
    print('Person is younger than 18')
elif age == 18:
    print('Person is 18')
else:
    print('Person is older than 18')


# %%
# Slide 13
number = 5

if number + 5 < 10:
    print('Number plus 5 is less than 10')

if not number + 5 < 10:
    print('Number plus 5 is 10 or more')

if number > 3 and number < 10:
    print('Number is greater than 3 and less than 10')


# %%
# Slide 14
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = numbers[1]

if num % 2 == 0:
    print(num)


# %%
# Slide 15
# Exercise 1

# 1.1 Print the minimum of both numbers
num1 = 8
num2 = 5

if num1 <= num2:
    print(num1)
else:
    print(num2)

# 1.2 Print the grade based on the points received
points = 77

if points >= 90:
    print('Grade 1')
elif points >= 75:
    print('Grade 2')
elif points >= 60:
    print('Grade 3')
elif points >= 50:
    print('Grade 4')
else:
    print('Grade 5')


# %%
# Slide 16
# Exercise 2
print((1 + 2) == 3)                       # True

print(True != False)                      # True

num = 4
print((num != 0) and (20 / num > 0))      # True

hour = 12
print((hour < 9) or (hour > 18))          # False


# %%
# Slide 20
count = 0

while count < 3:
    count = count + 1
    print('Hello!')


# %%
# Slide 21
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)


# %%
# Slide 22
# Iterate over a range
for i in range(1, 10, 2):
    print(i)

# Iterating by index of sequences
words = ['Iterating', 'by', 'index', 'of', 'sequences']

for i in range(len(words)):
    print(words[i])

# Simpler: iterate directly over the elements
for word in words:
    print(word)


# %%
# Slide 23
for letter in 'science':
    if letter == 'e' or letter == 'c':
        continue
    print('Current Letter:', letter)


for letter in 'science':
    if letter == 'e' or letter == 'c':
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
for num in numbers:
    # Check remainder of num
    if num % 2 == 0:
        # Print num if even
        print(num)


# %%
# Slide 26
# Exercise 3
numbers = [5, 23, 37, 49, 50, 46, 30, 46, 70]

# 1. while loop
count = 0
list_size = len(numbers)
i = 0

while i < list_size:
    if numbers[i] > 30:
        count = count + 1
    i = i + 1

print(count)

# 2. for loop
count = 0

for num in numbers:
    if num > 30:
        count = count + 1

print(count)
