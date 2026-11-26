# -*- coding: utf-8 -*-
"""
@author: 
@since: 
@update: 
@version: 
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

name = 
age = 

#we can print our variables by using the variable name



#%% Assigning new values
# If we use the same variable name again, we overwrite the value that was stored
# in that variable previously.

# Enter a different age


# Learning: Use variables for abstraction. In this way, you can easily make changes
# to the values you use, without having to rewrite the entire code.
#%% Exercise 1: 
    # Create a short profile of yourself with your first name, favorite city,
    # and your year of birth. Save each in a separate variable. Print all three
    # variables. Bonus: Change the city and print it again.
    




print()
print()
print()

#Bonus: change the city



#%% Data types
# Python supports different data types. They are assigned automatically, but 
# can be changed. We differentiate between numbers, symbols, and binary values.

# Numbers
my_first_int = 
my_first_float = 

# Symbols
my_first_str = 

#it does not matter if you use '' or ""
my_second_str = 

# Binary
yes = 
no = 

# Notice something when looking at the different data types?
# Spyder automatically shows them in different colors!

#%% Checking a data type
# There are multiple ways to check your data type
# in Spyder we can either use the variable explorer on the top right
# or we can use python to show the data type

print(type(my_first_int))

#%% The good thing about variables is that we can reuse them
my_first_addition = 

print(my_first_addition)

#what is the data type?


#We can use +, -, * and / just like in math

#%% But be aware, data types can change ...

my_second_addition = 

#What is the result of the addition? 


#What do you think the data type of the result will be?



#%% as you can see, we can use simple math with our variables
# but what happens when we apply it to different data types?

my_third_addition = my_first_str + my_second_str




#%% so does this work with all data types?

my_fourth_addition = my_first_int + my_first_str



#%% Exercise 2
# Guess the type of each value first, then check it with type()
# How can you differentiate the different types?

# 17, '17', 17.0, False, 'False', 3/2




























