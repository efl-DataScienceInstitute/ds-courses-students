# Examples discussed during the lecture
# Structure of Functions and Applications

#%%
# (1) Function that takes an integer as input and doubles it
def double_me(int1):
    factor = 2
    result = factor * int1
    return result

# Experiment with the function!




#%%
# (2) Function that calculates the base to the power of ex
def expo(base, ex=2): 
    result = base ** ex
    return result




#%%
# (3) Function that checks whether a number is positive or negative
def is_positive(number):
    if number >= 0:  # zero is defined as positive
        return True
    elif number < 0:
        return False




#%%
# (4) Making double_me more robust by checking the type of int1
def double_me(int1):
    if type(int1) is int:
        factor = 2
        result = factor * int1
        return result
    else:
        print("int1 must be of type int.")
        return




#%%
# ------------ EXERCISES IN THE LECTURE  ------------

# Test all functions using this list
mylist = [1, 6, 20, 12]

#%%
# Task 1: sum_elems
# Write a function that sums all elements in a list and returns a scalar.




#%%
# Task 2: square_elems
# Write a function that squares every element and returns a new list.
# (You can use a classic loop or a list comprehension)




#%%
# Task 3: f_mean
# Calculate the arithmetic mean of a list.
# Tip: Reuse sum_elems




#%%
# Task 4: f_variance
# Calculate the variance.
# Formula: Var(X) = E[X²] - (E[X])²
# Tip: Reuse square_elems and f_mean




#%%
# Optional: Quick look at lambda & map
# square_me = lambda x: x * x
# result = list(map(square_me, mylist))
# print(result)
