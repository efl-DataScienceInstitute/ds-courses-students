# -*- coding: utf-8 -*-
"""
Solutions
"""

####Tuples####

# Create a tuple with the entries 1, 2 and print it
example_tuple = 1, 2
print(example_tuple)
#%%
# Create a tuple with the entries 1, 2, 3, 4, 5 and print it
example_tuple_2 = 1, 2, 3, 4, 5
print(example_tuple_2)
#%%
# Create a tuple with the entries 1, 2, 3.0, 'hey', True (different data types) and print it
example_tuple_3 = 1, 2, 3.0, "hey", True
print(example_tuple_3)
#%%
# Print the element at index 1 of example_tuple
print(example_tuple[1])
#%%
# Print the first element of example_tuple (index 0)
print(example_tuple[0])
#%%
# Print the element at index 4 of example_tuple_2
print(example_tuple_2[4])
#%%
# Print the index of the value 4 in example_tuple_2
print(example_tuple_2.index(4))
#%%
# Given: a tuple that contains the value 4 several times. Print the index of the value 4. Which index do you get?
example_tuple_4 = 1,4,3,4,4,5
print(example_tuple_4.index(4))
#%%
# Given: a tuple with three values. Assign its values to float_a, float_b and float_c at once
example_tuple_5 = 3.0,4.0,12.0
float_a, float_b, float_c = example_tuple_5
#%%
# Given: a tuple. Try to change the element at index 1 to 12.0. What happens?
example_tuple_6 = 4.0,8.0,16.0
example_tuple_6[1] = 12.0  # TypeError: 'tuple' object does not support item assignment
#%%
####Lists####

# Create a list with the entries 1, 2, 3, 4, 5 and print it
numbers_list = [1,2,3,4,5]
print(numbers_list)
#%%
# Create a list with the entries 1, 2, 3.0, 'hey', True and print it
various_list = [1, 2, 3.0, "hey", True]
print(various_list)
#%%
# Create an empty list and print it
empty_list = list()
print(empty_list)
#%%
# Print the element at index 1 of various_list
print(various_list[1])
#%%
# Print the index of the value 2 in various_list
print(various_list.index(2))
#%%
# Print the elements at indices 1, 2 and 3 of various_list (slice)
print(various_list[1:4])
#%%
# Assign this slice to a new list variable, various_part_list, and print it
various_part_list = various_list[1:4]
print(various_part_list)
#%%
# Given: spotify_list. Reassign the element at index 0 to 'Aktuelle Charts'
spotify_list = ["Charts","Neuheiten","Podcasts & Video Shows", "Entdecken", "Konzerte"]

spotify_list[0] = "Aktuelle Charts"
#%%
# Append the element 'Deine Songs' to spotify_list
spotify_list.append("Deine Songs")
#%%
# Remove the last element of spotify_list and print the list
spotify_list.pop()
print(spotify_list)
#%%
# Remove the element at index 3 and print the list
spotify_list.pop(3)
print(spotify_list)
#%%
# Remove the value 'Neuheiten' (by value, not index) and print the list
spotify_list.remove("Neuheiten")
print(spotify_list)
#%%
# Insert 'Neuheiten' at index 1 and 'Entdecken' at index 3, then print the list
spotify_list.insert(1,"Neuheiten")
spotify_list.insert(3,"Entdecken")
print(spotify_list)
#%%
# Print the length of spotify_list
print(len(spotify_list))
#%%
# Print how often 'Neuheiten' occurs in spotify_list
print(spotify_list.count("Neuheiten"))
#%%
# Reverse spotify_list and print it
spotify_list.reverse()
print(spotify_list)
#%%
# Reverse it again and print it
spotify_list.reverse()
print(spotify_list)
#%%
# Given: a string. Strings and lists share many operations
test_string = "Lists are awesome and so are Strings!"
#%%
# Print the character at index 3 of test_string
print(test_string[3])
#%%
# Print the first five characters of test_string. Play a little! Change the first and the second value.
print(test_string[0:5])
#%%
# Get the length of test_string
len(test_string)
#%%
####Sets####

# Given: a set with a repeated value. Print it. What happens to the duplicate 1?
numbers_set = {1,2,3,4,5,1}
print(numbers_set)
#%%
# Given: a set with values of different types. Print it
various_set = {1, 2, 3.0, "hey"}
print(various_set)
#%%
# Create an empty set and print it
empty_set = set()
print(empty_set)
#%%
# Check whether the value 4 is in various_set
print(4 in various_set)
#%%
# Check whether the value 2 is in various_set
print(2 in various_set)
#%%
# Convert source_list into a set (set_from_list) and print it. What do you notice?
source_list = [1,2,3,5,2,4,12,523,123,21]
set_from_list = set(source_list)
print(set_from_list)
#%%
# Convert set_from_list back into a list (list_from_set) and print it. What do you notice?
list_from_set = list(set_from_list)
print(list_from_set)
#%%
# Print the unique values in numbers_set
numbers_set = {1,2,3,4,5,1}
various_set = {1, 2, 3.0, "hey"}

print(numbers_set)
#%%
# Print the values in numbers_set but not in various_set
print(numbers_set - various_set)
#%%
# Print the values in numbers_set or in various_set or both
print(numbers_set | various_set)
#%%
# Print the values in both numbers_set and various_set
print(numbers_set & various_set)
#%%
# Print the values in numbers_set or in various_set but not in both
print(numbers_set ^ various_set)
#%%
####Dictionaries####

# Given: a dict with the keys 'One', 'Two', 'Three' and the values 1, 2, 3
numbers_dict = {"One":1,"Two":2,"Three":3}
print(numbers_dict)
#%%
# Given: a dict with the int keys 1, 2, 3 and the values 1, 2, 3
num_keys_dict = {1:1,2:2,3:3}
print(num_keys_dict)
#%%
# Given: a dict with the int keys 1, 2, 3 and the string values 'One', 'Two', 'Three'
str_vals_dict = {1:"One",2:"Two",3:"Three"}
print(str_vals_dict)
#%%
# Print the value stored under key 3 and under key 1 of str_vals_dict
print(str_vals_dict[3])
print(str_vals_dict[1])
#%%
# Change the value of key 3 to 'I made this.' and print it
str_vals_dict[3] = "I made this."
print(str_vals_dict[3])
#%%
# Get the value of key 1; if the key does not exist, return the message 'This is the message, if no such key is in the dict.'
print(str_vals_dict.get(1,'This is the message, if no such key is in the dict.'))
#%%
# Do the same for key 11
print(str_vals_dict.get(11,'This is the message, if no such key is in the dict.'))
#%%
# Print the value of key 4. What happens?
print(str_vals_dict[4])  # KeyError: 4
#%%
# Given: some_dicts holds numbers_dict and num_keys_dict under string keys
some_dicts = {"numbers_dict":numbers_dict, "num_keys_dict": num_keys_dict}
print(some_dicts)
#%%
# Get the data structure numbers_dict from some_dicts, once with brackets and once with the get method
print(some_dicts["numbers_dict"])
print(some_dicts.get("numbers_dict"))
#%%
# Change the value of the key 'numbers_dict' to the list [1,2,3] and print some_dicts
some_dicts["numbers_dict"] = [1,2,3]
print(some_dicts)
#%%
# Add the key 'SomeInt' with the value 1337 to numbers_dict and print it
numbers_dict["SomeInt"] = 1337
print(numbers_dict)
#%%
# Remove the key 'SomeInt' from numbers_dict and print numbers_dict
numbers_dict.pop("SomeInt")
print(numbers_dict)
#%%
#### Exercises ####

# Create a variable of type list "exercise_list" with the contents: "Anna", "Charles", "Peter", "Santa", "Eric"
exercise_list = ["Anna", "Charles", "Peter", "Santa", "Eric"]
# Get the index of the element named "Santa"
exercise_list.index("Santa")
# Get the element with the index 4
exercise_list[4]
# Get the last element
exercise_list[-1]
# Assign a string Variable with the contents of element with index 3, but only get the first three letters from the element!
exercise_string = exercise_list[3][:3]
####
# Create a variable of type dictionary "exercise_dict" with the key-value pairs: 4213-"Epic", 532-"Exclusive", 213-"Good", 5321-"Job"
exercise_dict = { 4213:"Epic", 532:"Exclusive", 213:"Good", 5321:"Job"}
# print the contents of the dictionary.
print(exercise_dict)
# Retrieve the list of keys.
list(exercise_dict.keys())
# Retrieve the value for the key 532
exercise_dict[532]
####
# Create a list variable "container_list" with the elements: [231,421,324,646],[21423,634,132],[123,765]
container_list = [[231,421,324,646],[21423,634,132],[123,765]]
# Create a new variable example_multiplication and assign the value of the multiplication between the 
# first element of the first list in container_list and the third element of the second list in container_list.
example_multiplication = container_list[0][0]*container_list[1][2]