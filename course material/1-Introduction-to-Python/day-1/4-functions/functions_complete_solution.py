# Examples discussed during the lecture Functions - Structure of Functions and Applications

#%%
# (1) Function that takes an integer as input an doubles it
def double_me(int1):
    factor = 2
    result = factor * int1
    return result

# Experiment with the function!
res = double_me(3)  # Store in variable res
print(res)
print(double_me(4))  # print immediately with positional argument
print(double_me(int1=6))  # keyword argument


#%%
# (2) Function that calculates the base to the power of ex
def expo(base, ex=2): 
    result = base**ex
    return result

print(expo(4))  # 1 positional argument
print(expo(base=5))  # 1 keyword argument
print(expo(4, 3))  # 2 positional arguments
print(expo(ex=3,base=5))  # 2 keyword arguments
print(expo(5, ex=3))  # 1 positional, 1 keyword argument


#%%
# (3) Function that checks whether number is positive or negative
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
# Solutions
def sum_elems(list1):
    # use a loop
    list_sum = 0
    for x in list1:
        list_sum += x
    return list_sum

def square_elems(lst):
    sq_list = []
    for e in lst:
        sq_list.append(e**2)
    return sq_list

def square_elems_alternative(list1):
    # use a list comprehension
    sq = [x*x for x in list1]
    return sq


print(sum_elems(mylist))
print(square_elems(mylist))
print(square_elems_alternative(mylist))


#%%
def f_mean(list2):
    n = len(list2)
    average = sum_elems(list2) / n
    return average

print(f_mean(mylist))


#%%
def f_variance(list3):
    # Var(X) = E[(X-E[X])²] = E[X²] - (E[X])²
    variance = f_mean(square_elems(list3)) - f_mean(list3)**2  
    return variance

print(f_variance(mylist))

#%%
# Alternative Solution
def f_variance_alternative(list4):
    
    var_sum = 0
    sq_list = square_elems(list4)
    
    for s in sq_list:
        var_sum += s - f_mean(list4)**2
    
    variance = var_sum / len(list4)
    
    return variance

print(f_variance_alternative(mylist))

#%%
# Outlook:

# (1) lambda operator for a quick function implementation
square_me = lambda x: x*x

print(square_me(5))

# (2) map operator to apply function to all list elements
res = list(map(square_me, mylist))
print(res)

# In combination
res = list(map(lambda x: x*x, mylist))
print(res)