# Examples discussed during the lecture
# Structure of Functions and Applications
# --- COMPLETE SOLUTIONS ---

#%%
# (1) Function that takes an integer as input and doubles it
def double_me(int1):
    factor = 2
    result = factor * int1
    return result

# Experiment with the function!
res = double_me(3)
print(res)
print(double_me(4))
print(double_me(int1=6))


#%%
# (2) Function that calculates the base to the power of ex
def expo(base, ex=2): 
    result = base ** ex
    return result

print(expo(4))
print(expo(base=5))
print(expo(4, 3))
print(expo(ex=3, base=5))
print(expo(5, ex=3))


#%%
# (3) Function that checks whether a number is positive or negative
def is_positive(number):
    if number >= 0:  # zero is defined as positive
        return True
    elif number < 0:
        return False

print(is_positive(5))
print(is_positive(-10))


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

print(double_me(3))
print(double_me(4.5))


#%%
# ------------ EXERCISES IN THE LECTURE  ------------

# Test all functions using this list
mylist = [1, 6, 20, 12]

#%%
# Task 1: sum_elems
def sum_elems(lst):
    total = 0
    for x in lst:
        total += x
    return total

print(sum_elems(mylist))   # 39


#%%
# Task 2: square_elems
# Version A – classic loop
def square_elems(lst):
    sq_list = []
    for e in lst:
        sq_list.append(e ** 2)
    return sq_list

# Version B – list comprehension
def square_elems_alternative(lst):
    return [x * x for x in lst]

print(square_elems(mylist))              # [1, 36, 400, 144]
print(square_elems_alternative(mylist))  # [1, 36, 400, 144]


#%%
# Task 3: f_mean
def f_mean(lst):
    n = len(lst)
    average = sum_elems(lst) / n
    return average

print(f_mean(mylist))   # 9.75


#%%
# Task 4: f_variance
def f_variance(lst):
    # Var(X) = E[X²] - (E[X])²
    variance = f_mean(square_elems(lst)) - f_mean(lst) ** 2
    return variance

print(f_variance(mylist))


#%%
# Optional: lambda & map
square_me = lambda x: x * x

print(square_me(5))

res = list(map(square_me, mylist))
print(res)

# In combination
res = list(map(lambda x: x * x, mylist))
print(res)
