# -*- coding: utf-8 -*-
"""
@author: Anna
@since: 2026-11-27
@update: 2026-11-27
@version: v.0.0.1
"""

#%% these signs create a cell block. Using cells makes running the code easier.
# you can create a new cell by using #%%
# you can create a comment by using #
# comments are ignored when the code is run

# Let's start writing our first code.
#%% Hello world
print('Hello World')

# using print allows us to get an output in the console

#%% Let's create a variable. We use variables for storing values. 
# We use Camel Case as our naming convention. This ensures that variables are
# easy to understand.

name = 'Anna'
age = 28

#we can print our variables by using the variable name
print(name)
print(age)

#%% Assigning new values
# If we use the same variable name again, we overwrite the value that was stored
# in that variable previously.

# Enter a different age
age = 29
print(age)

# Learning: Use variables for abstraction. In this way, you can easily make changes
# to the values you use, without having to rewrite the entire code.
#%% Exercise 1: 
    # Create a short profile of yourself with your first name, favorite city,
    # and your year of birth. Save each in a separate variable. Print all three
    # variables. Bonus: Change the city and print it again.
    
first_name = "Anna"
favorite_city = "Frankfurt"
year_of_birth = "1999"

print(first_name)
print(favorite_city)
print(year_of_birth)

#Bonus
favorite_city = "Lisbon"
print(favorite_city)

#%% Data types
# Python supports different data types. They are assigned automatically, but 
# can be changed. We differentiate between numbers, symbols, and binary values.

# Numbers
my_first_int = 1
my_first_float = 2.0

# Symbols
my_first_str = 'Hello'

#it does not matter if you use '' or ""
my_second_str = "Hi"

# Binary
yes = True
no = False

# Notice something when looking at the different data types?
# Spyder automatically shows them in different colors!

#%% Checking a data type
# There are multiple ways to check your data type
# in Spyder we can either use the variable explorer on the top right
# or we can use python to show the data type

print(type(my_first_int))

#%% The good thing about variables is that we can reuse them
my_first_addition = my_first_int + my_first_int

print(my_first_addition)

#what is the data type?
print(type(my_first_addition))

#We can use +, -, * and / just like in math

#%% But be aware, data types can change ...

my_second_addition = my_first_int + my_first_float

#What is the result of the addition? 
print(my_second_addition)

#What do you think the data type of the result will be?

print(type(my_second_addition))

#%% as you can see, we can use simple math with our variables
# but what happens when we apply it to different data types?

my_third_addition = my_first_str + my_second_str

print(my_third_addition)
print(type(my_third_addition))

#%% so does this work with all data types?

my_fourth_addition = my_first_int + my_first_str

print(my_fourth_addition)
#You cannot mix strings and numbers
#%% Exercise 2
# Guess the type of each value first, then check it with type()
# How can you differentiate the different types?

# 17, '17', 17.0, False, 'False', 3/2

print(type(17))
print(type('17'))
print(type(17.0))
print(type(False))
print(type('False'))
print(type(3/2))


#%% Coffee Shop
product = "Cafe Latte"
price = 3.99
quantity = 2
total = price * quantity

print(total)

#Make the print look nicer in the console
print("The customer has bought", product, "for a total of", total)

#You can mix strings and numbers in print statements by doing a type cast
# by using str() you can turn a number into a string, WITHOUT changing the 
# type of the variable

print("The customer has bought" , product , "for a total of:" + str(total))

#Notice one thing:
    #when you use a , in a print statement, it automatically creates a space
    #when you use a + between strings, there is no space

























