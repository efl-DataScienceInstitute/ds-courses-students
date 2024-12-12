# Examples discussed in the lecture on "Helpful functions for data preprocessing: Libraries os, re, csv"

# ---- (1) Basics about libraries in Python ----
# All examples do the same thing!
lst = [2, 7, 13, 99]

#%%
# Import library with plain import statement
import numpy




#%%
# Import library using alias





#%%
# Import submodule from library 





#%%
# Import submodule from library using alias





#%%
# Generate module with x1=1, x3=3 and a function fct1 that sums up two elements

















#%%
# ---- (2) Library os ----
import os

#%%
# 2.1 Basic commands 

#%%
# Show current working directory you operate in
print(os.getcwd())

#%%
# Change current working directory, insert your own directory
path = r"C:\Users\Tino\GitHub\ds-courses-students\course material\1-Introduction-to-Python\day-2\5-basicLibs"  # your own path
os.chdir(path)  # change current working dir
print(os.getcwd())

#%%
# List all files in current working directory


#%%
# create a folder in current working directory


#%%
# delete a folder in current working directory


#%%
# create a folder at a specific path



#%%
# delete a folder at a specific path


#%%
# 2.2 Some Applications

#%%
# Automatically generate folders


#%%
# Automatically delete folders



#%%
# Iterate through directory
# path_content =   # TODO: list of all dirs and files in path
# print(path_content)
  # TODO: iterate trough all files and folders in path
    # joined = os.path.join(path, f)  # join various path components
    # print(joined)  # print all file and folder names in path

#%%
# Outlook:
# Walk through directory and subdirectories and print files only
path_content = os.walk(path)
for root, dirs, files in path_content:  # walk the tree
    for name in files:
        joined = os.path.join(root, name)  # join various path components
        print(joined)  # print all filenames in path+depper


#%%
# ---- (3) numpy (np) ----
import numpy as np

#%%
# Create vector
lst = [1, 2, 3]
vec1 = np.array(lst)
vec2 = np.array([4,5,6])

#%% 
# Print shape of both vectors
print()

#%%
# Vector indexing
print()  # second element
print()  # first element when counting from the end

#%%
# Addition of both vectors



#%%
# Create matrix
mtrx1 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
mtrx2 = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
#%% 
# Print shape


#%%
# Matrix indexing
print()  # print first row
print()  # print second column
print()  # value in last row and second column

#%%
# Addition of both matricies

#print(mtrx3)

#%%
# Element-wise multiplication of both matricies

#print(mtrx4)

#%%
# Matrix multiplication of both matricies

#print(mtrx5)

#%%
# Calculate means of mtrx1
#result0 = 
#result1 =
#result2 = 
#print(result0)
#print(result1)
#print(result2)


#%%
# ---- EXERCISE ----

#%%
# download the provided zip-file numpy_data.zip and extract it to create a directory that e.g. looks like this
# /mypath/to/folder/numpy_data and contains customer1.csv, customer2.csv, customer3.csv

import numpy as np
import os

# path = r'C:\your\path\here\numpy_data'
# files = # TODO: set equal to list of all filenames
# print(files)
overall_consumption = np.zeros(shape=(5, 3))  # store data of each customer

#%%
# for file in files: TODO: iterate through list of files
    # filepath = # TODO: join path and filename
    # customer_data = np.genfromtxt(filepath, delimiter=',')  # read data
    # TODO: Continue