# -*- coding: utf-8 -*-
# Code for the first Data Science Process according to the KDD Model.
# @author: Benjamin M. Abdel-Karim
# @since: 2025-12-01
# @version: 2025-12-01

# Import libraries for our data analysis.
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
import seaborn as sns

# --------------
# Setup
# --------------
# Import our data set.
# Check your working directory first.
print(os.getcwd())
# Is your file in the directory? What is its name?
print(os.listdir())

# Create output folder
now = datetime.now()
str_date_time = now.strftime('%Y-%m-%d_%H-%M-%S')
str_folder_output = 'logs/' + 'log' + '_' + str_date_time
if not os.path.exists(str_folder_output):
    os.makedirs(str_folder_output)
print('// complete ....... execute folder creation')

# --------------
# Import the Data
# --------------
# Now create a pandas dataframe.
df = pd.read_csv('vgsales.csv', sep=',')

# Let's have a first look at our dataset!
# Let's see what attributes/columns we have.
print(df.columns)

# That are quite some columns. How many, actually?
print(len(df.columns))

# We can also return a tuple representing the dimensionality of the DataFrame,
# to see how many records and columns we have.
# print('Dimensionality of the DataFrame')
df_shape = df.shape
print('Shape of df', df_shape)

# So that is the number of columns. Great! Still too little information actually.
# I wonder what datatypes those specific columns are.
df_info = df.info()
print('info', df_info)
print('// complete ....... import the data')

# %%
# --------------
# Pre-processing
# --------------
# Data pre-processing
# Let's check the dataset for missing values.
# @code: 0, or ‘index’: Drop rows which contain missing values.
# Let's see where the Null values are.
# Let's see the data shape and NaN values.
# This will give number of NaN values in every column.
df_null_values = df.isnull().sum()
print('NANs?', df_null_values)

# Drop all rows with NaN.
df = df.dropna(axis=0)

df_null_values = df.isnull().sum()
print('NANs_After_Update?', df_null_values)
print('// complete ....... pre-processing')


# %%
# --------------
# Explore the Data
# --------------
float_mean_global_sales = round(df['Global_Sales'].mean(), 2)
float_std_global_sales = round(df['Global_Sales'].std(), 2)

# Select a part of the DataFrame and let's have a look on some numbers
df_selected = df[['Global_Sales', 'Genre']]
df_selected_grouped_by_mean = df_selected.groupby(by="Genre", dropna=True).mean()
# Sorting
df_selected_grouped_by_mean = df_selected_grouped_by_mean.sort_values(by='Global_Sales', ascending=False)

# %%
# Get unique values in a column
list_brands = df['Publisher'].unique().tolist()
print(list_brands)

# %%
# Figure
# First of all, we want a scatter plot.
# Therefore, we need to extract the data.
# Extract the data by using DataFrame.
# Access to the data for pie plot.
# Data frame df['Genre']!
# @code: plt.pie()
list_count_genre = df['Genre'].value_counts()
list_count_genre_labels = df['Genre'].value_counts().index

# Try to create a Pie Plot with the data of df['Genre'].
plt.figure(figsize=(7, 7))
plt.pie(list_count_genre, labels=list_count_genre_labels, autopct='%1.1f%%')
plt.title('Games According to Genre')
# Output Folder
str_path = str_folder_output + '/' + 'fig_PieGamesGenre.pdf'
plt.savefig(str_path)
plt.close()

# %%
# Scatter Plot
# Try to create a scatter plot with the Global Sales and Year Information.
# Now we would like to use Matplotlib.
# Matplotlib is a Python 2D plotting library which produces.
# publication quality figures.
# Matplotlib can be used in Python scripts.
# Let's try it out.
# @code: plt.scatter(LYears, LGlobal_Sales)
# Access to the data for scatter.
# Warning: @code: .values is since 3.7
# @code: before that you need to use .get_values()
list_global_sales = df['Global_Sales'].values
list_years_values = df['Year'].values

plt.figure()
plt.scatter(list_years_values, list_global_sales, color='red', alpha=0.1)
plt.title('Scatter Global Sales and Year')
plt.ylabel('Global Sales')
plt.xlabel('Years')
str_path = str_folder_output + '/' + 'fig_ScatterUpdate.pdf'
plt.savefig(str_path)
plt.close()

# %%
# Seaborn
# For using seaborn we need to use the bib.
# Joint Plot
# Try to create a joint plot with the df.Year, df.Global_Sales.
# Use the optional parameters: height=8, ratio=9, color="blue", alpha=0.1
# @code: sns.jointplot
# Note: @code: size is changed to @code: height since: 0.9.0
plt.figure()
sns.jointplot(x='Year', y='Global_Sales', data=df, height=8, ratio=9, color="blue", alpha=0.1)
# plt.title('Global Sales Over the Years')
plt.ylabel('Global Sales')
plt.xlabel('Years')
str_path = str_folder_output + '/' + 'fig_JoinPlot.png'
plt.savefig(str_path)
plt.tight_layout()
plt.close()

# %%
# Bar Plot
# Access data for the bar plt.
# In our case we need the sum of the 'Global Sales' data for each year.
# @code: df_groupData Grouped data by years and summed up.
# @code: LIndexesOfGroupData years converted as int!
df_groupData = df.groupby(['Year']).sum()
LdfGroupSales = df_groupData['Global_Sales']
LIndexesOfGroupData = df_groupData.index.astype(int)


# %%
# Generate the bar plot
plt.figure()
sns.barplot(y=LdfGroupSales, x=LIndexesOfGroupData, color='darkblue')
plt.title('Global Sales Grouped by Year')
plt.xticks(rotation=45, fontsize=6)
plt.ylabel('Global Sales')
plt.xlabel('Years')
str_path = str_folder_output + '/' + 'fig_BarChart.pdf'
plt.savefig(str_path)
plt.close()

# %%
# Box Plot
# Access data for our box plot. We would like to create the plot
# for publisher Nintendo.
df_nintendo = df[df['Publisher'] == 'Nintendo']



# %%
# What is the problem in the plot?
plt.figure()
sns.boxplot(x='Genre', y='EU_Sales', data=df_nintendo)
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
str_path = str_folder_output + '/' + 'fig_Nintendo_BoxPlot.pdf'
plt.savefig(str_path)
plt.close()

# %%
# Update 2
plt.figure()
sns.boxplot(x='Genre', y='EU_Sales', data=df_nintendo, showfliers=False)
plt.xticks(rotation=45, fontsize=6)
str_path = str_folder_output + '/' + 'fig_BoxPlotUpdat2.pdf'
plt.savefig(str_path)
plt.close()

# %%
# Update 3
plt.figure()
sns.boxplot(x='Genre', y='EU_Sales', data=df_nintendo, showfliers=False,
            palette='flare')
plt.title('Nintendo EU_Sales by Genre')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
str_path = str_folder_output + '/' + 'fig_BoxPlotUpdat3.pdf'
plt.savefig(str_path)
plt.close()
print('// complete ....... explore the data')

print('// complete ....... scrip')
