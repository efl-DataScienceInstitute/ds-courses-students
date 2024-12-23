# -*- coding: utf-8 -*-

# Import libraries for our data analysis.
import pandas as pd
import numpy  as np
import os

# Import our data set.

# Check your working directory first.
os.getcwd()
#%%
# Is your file in the directory? What is its name?
os.listdir()
#%%
# Change your working directory to where the file is, if the file is not in the current directory
os.chdir(r"...")
#%%
# Now create a pandas dataframe.
df = pd.read_csv('dataset_small.csv', sep=',')

# Let's have a first look at our Dataset! Let's see what attributes/columns we
# have.
#%%
print(df.columns)

# That's quite some columns. How many, actually?
#%%
print(len(df.columns))

# We can also return a tuple representing the dimensionality of the DataFrame,
# to see how many records and columns we have.
#%%
print('Dimensionality of the DataFrame')
df_shape = df.shape
print(df_shape)

# So that is the number of columns. Great! Still too little information actually.
# I wonder, what datatypes those specific columns are.
#%%
print('info')
df_info = df.info()
print(df_info)


# Now we're talking. We do have a lot of float values. Also some 'object' types.
# This resembles the look of categorical values, e.g. 'purpose', which we might 
# have to convert to numericals for our statistics later. A more intruiging 
# problem is that some attributes appear to have no records. This describes 
# NaN/Null Values. Let's see where the Null values are.

#%%
# Let's see the data shape and NaN values.
# This will give number of NaN values in every column.

print('There are nan')
df_null_values = df.isnull().sum()
print(df_null_values)

# Some attributes are droppable, since they do not provide any value to us.
# Let's drop these attributes. This will reduce computational complexity and
# improve clarity of our dataset.

#%%
df = df.drop(columns=['id', 'member_id', 'url', 'desc'])

# Now that we have taken care of this issue, we can proceed with our analysis.


# Why did we not drop the other attributes containing NaN values? Because they
# still might be insightful.

# Let's have a deeper look at the top 5 records now
# to get a better feeling for the dataset.


# DataFrame Manipulations: Remember to save manipulated states as variables,
# so you can look them up again or work on their basis.

# Use the head function from df object to get the top 5 records.
#%%
print('Show head')
df_top = df.head(5)
print(df_top)

# It looks like these are too many columns to show at once.
# Let's use a slice to only show the attributes between 'loan_amnt' and 'sub_grade'
# Remember, we want to see the rows 1-5.

# Slicing and indexing
#%%
df_top_slice = df.loc[0:4, 'loan_amnt':'sub_grade']
print(df_top_slice)

# We already see in this subsample, that the loan_amounts greatly diverge.
# Furthermore, the interest rates are also quite different. Referring to our
# research questions, we could take a short look at the different interest
# rates and and loan_amounts.

# Maximum, Minimum measures
#%%
print(df.int_rate.max())
print(df.int_rate.min())

# Dataset subselection, similar to SQL statements
# We want to show a subset of the dataframe, where the loan_amnt is >$16000 
# and the int_rate is higher than 28 %. We also want to see the respective grades.
#%%
subselect_df = df[(df.loan_amnt > 16000) & (df.int_rate > 28.0)]
print(subselect_df[['loan_amnt', 'int_rate', 'grade', 'sub_grade']])


# We can see that in this relatively high interest rate area only low credit
# score ratings are present. We will take a closer look at the two ratings 
# grade and subgrade.
#%%
# Grouping is a way to arrange the data accordingly.
# Group by the attribute 'sub_grade' and provide the mean score.
# sub_grade: The specific subclass of a credit score rating, i.e. A - A1,A2...

df_sub_grade = df.groupby('sub_grade').mean(numeric_only=True)
print(df_sub_grade)
#%%
# Group by the attribute 'grade'. 

df_grade = df.groupby('grade').mean()
print(df_grade)

# Would it not also be interesting to see, what kind of purposes people 
# get a loan for? Let's find out by getting (1) the number of unique values for the
# 'purpose' attribute, then the values. Print them.
#%%
# Return number of distinct observations. Can ignore NaN values.
print(df['purpose'].nunique())
#%%
# initialize a list with unique values of the dataframe object and print it.
Lunique_purpose = df['purpose'].unique().tolist()
print(Lunique_purpose)

# That is quite a list of purposes. What are the average sums of the loans?
# Initialize a dictionary for the purpose of holding the mean loan sum
# per loan purpose. Then print it.
#%%
Dmean_purpose = dict()

for purpose in Lunique_purpose:
    Dmean_purpose[purpose] = df[df.purpose == purpose].loan_amnt.mean()

print(Dmean_purpose)

# Here we can see that there are both larger investments, such as 'car' 
# and 'small_business', but also seemingly smaller investments, 
# such as 'vacation'.


#%%
#### Final part of this section ####

# Now that we got a grip and first understanding of the dataset, 
# we will view some sample descriptive statistics to gain further insights 
# for statistical relations in our data.

    
# Print simple stats
print('Simple stats')
df_description = df.describe()
print(df_description)


# Finally, we want to get an overview over insightful correlations. This will
# bring us a step forward in answering our research questions.
#%%
corr = df.corr(numeric_only=True)
#corr = df.corr()
#depending on your version of numpy and pandas you need to use numeric_only or not

# As we can see, the categorical variables will not show up. This is because
# they are of the object type. Yet we want to see especially the correlations
# of the credit score ratings. Let's convert them and rerun our analysis.
# Convert the 'grade' and 'sub_grade'
# object types to categorical, then apply codes to category.
#%%
for col_name in df.columns:
    if((df[col_name].dtype == 'object') & (col_name in ['grade','sub_grade'])):
        df[col_name]= df[col_name].astype('category')
        df[col_name]= df[col_name].cat.codes

#%%
corr_2 = df.corr(numeric_only=True)
#corr2 = df.corr()
#depending on your version of numpy and pandas you need to use numeric_only or not


# Great! We have found first evidence about a correlation between important 
# attributes in our lending system! We will further investigate from here on
# using visualizations.