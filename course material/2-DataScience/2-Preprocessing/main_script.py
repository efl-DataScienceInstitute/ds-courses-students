# -------
# Preamble and Semantic Versioning
# -------
# Script for a first Data Science Look in regards to the steps 
# import, pre-processing, data exploring. 
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2023-11-03
# @update: 2023-11-03
# @version: 1.0.2
# @workload 60 min


# --------------
# Imports and Setup
# --------------
# Import libraries for our data analysis.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import datetime
import time

# # Check your working directory first.
# Show current working directory (cwd)
# And list all filies
print(os.getcwd())
print(os.listdir())

# Create output folder
# Import our data set.
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d_%H-%M-%S')
string_log_folder = 'logs/' + 'log' + '_' + date_time
if not os.path.exists(string_log_folder):
    os.makedirs(string_log_folder)
print('// complete ....... execute folder creation: ', string_log_folder)

# %%
# --------------
# Import the data set
# --------------
# Is your file in the directory? What is its name?
# Now create a pandas dataframe.
float_time = time.time()
float_elapsed = time.time() - float_time
df_raw = pd.read_csv('dataset_small.csv', sep=',')
print('//complete ....... import data, run time in seconds: ', str(round(float_elapsed, 4)))

# %%
# --------------
# First Look
# --------------
# Let's have a first look at our dataset!
# Let's see what attributes/columns we have.
print(df_raw.info())

# %% Export df_raw.info()
# The return value from open is a file handle, 
# given out from the operating system to Python application.
# Using @code: open, @param: w = Open a file for writing. 
# Creates a new file if it does not exist or truncates the file if it exists.
# @param: 'w+' Open a file for updating (reading and writing).
# @param: buf=TextIOWrapper Where to send the output. => here text object. 
str_output_file_name = string_log_folder + '/'+ 'df_raw_info.txt'
TextIOWrapper = open(str_output_file_name, 'w+', encoding='utf-8')
df_raw.info(buf=TextIOWrapper)
TextIOWrapper.close()

# %%
# --------------
# Pre-Processing: Overview
# --------------
# Data preprocessing is an important step in the data mining process.
# The phrase "garbage in, garbage out" is particularly applicable
# to data mining and machine learning projects.
# So that is the number of columns. Great! Still too little information, actually.
# I wonder what data types those specific columns are.
# Now we're talking. We do have a lot of float values.
# Sum all NaN Values
df_null_values = df_raw.isnull().sum()
print(df_null_values)

# %%
# Create a plot to take another view.
# Warning: This plot requires relatively much computing time.
float_time = time.time()
plt.figure(figsize=(15, 5))
sns.heatmap(df_raw.isnull(), cbar=False, yticklabels=False, cmap='Greys')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'fig_missing_values.png', dpi=300)
plt.close()

df_raw = pd.read_csv('dataset_small.csv', sep=',')
print('//complete ....... ifigure: heatmap Missing Values: ', str(round( time.time() - float_time, 4)))
# Note: We see columns without values. 


# %%
# Drop all useless columns
# Some attributes are droppable because they do not provide any value.
# Let's drop these attributes. This will reduce computational complexity and
# improve clarity of our dataset.
df_raw = df_raw.drop(columns=['id', 'member_id', 'url', 'desc'])
print(df_raw.columns)


# %%
# --------------
# Pre-Processing: Handling Missing Values With Python Pandas (None)
# --------------
# NaN can be used as a numerical value on mathematical operations, 
# while None cannot (or at least shouldn't). NaN is a numeric value, 
# as defined in IEEE 754 floating-point standard. 
# None is an internal Python type (NoneType) and would be more like 
# "inexistent" or "empty" than "numerically invalid" in this context
# Fill NA/NaN values using the specified method.
# Some examples:
# isnull() -> Checking for missing values using isnull()
# notna() -> Indicate existing (non-missing) values

# notnull() -> function gives a dataframe of Boolean values which are False for NaN values.
# dropna() -> Drop NA/NaN row or columns wise

# Filling missing values using fillna(), replace() and interpolate()
# fillna() -> since 2.1.0 
# --> ffill() -> Fill values by propagating the last valid observation to next valid.
# --> bfill() Fill values by using the next valid observation to fill the gap.
# replace() -> Replace values given in to_replace with value.
# interpolate()


# %%
# Our approach
df = df_raw.fillna(0)
print('// complete ....... data pre-processing')


# %%
# --------------
# Data Exploring
# --------------
# Get all columns with numeric values.
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
df_numbers = df.select_dtypes(include=numerics)
print(df_numbers.columns)

# Get all models
list_unique_grade = df['grade'].unique()
int_unique_count_grade = len(list_unique_grade)
print('// complete ........ data: unique grade: ', list_unique_grade)
print('// complete ........ data: number of grades: ', int_unique_count_grade)

# Super important: Slicing over column names with condition:
# Fore more details see Pandas DataFrame operations from day 2.
# With .iloc and loc als common approach
df_all_a_grades = df[df['grade'] == 'A']

# Select data where people have a high income.
df_high_income = df[df['annual_inc'] >= 75000]

# High income and high grade
df_high_income_and_grade = df[(df['annual_inc'] >= 75000) & (df['grade'] == 'A')]

# Get the interest rats
dMean_int_rate = df['int_rate'].mean()
dMax_int_rate = df['int_rate'].max()
dMin_int_rate = df['int_rate'].min()
print('// complete ........ data int_rate min: ', dMean_int_rate)
print('// complete ........ data int_rate max: ', dMax_int_rate)
print('// complete ........ data int_rate min: ', dMin_int_rate)


# Plot pairwise relationships in a dataset.
# Warning: This plot requires relatively much computing time.
# Therefore, here only a small selection of data
# If True, don’t add axes to the upper (off-diagonal)
# triangle of the grid, making this a “corner” plot.
plt.figure()
sns.pairplot(df[['loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti']], corner=True)
plt.savefig(string_log_folder + '/' + 'fig_pair_plot.png', dpi=300)
plt.close()

#%%  Label Encoding:
# But How can we deal with other informations? 
# Do it yourself

# Check column: "home_ownership"
print(df['home_ownership'].unique())

# Using Assigment based on conditions.
# Idea based on the unique()
# 'MORTGAGE' => 1, 'RENT' => 2, 'OWN' => 3, 'ANY' => 4], defualt is 0.     
# 
#df['home_ownership_label_endcoded'] = 0

# Execute: 
#Syntax:   df.loc[df['Column'] Condition Operation 'Condition', 'new_column'] = value
df['home_ownership_label_endcoded'] = 0
df.loc[df['home_ownership'] == 'MORTGAGE', 'home_ownership_label_endcoded'] = 1
df.loc[df['home_ownership'] == 'RENT', 'home_ownership_label_endcoded'] = 2
df.loc[df['home_ownership'] == 'OWN', 'home_ownership_label_endcoded'] = 3
df.loc[df['home_ownership'] == 'ANY', 'home_ownership_label_endcoded'] = 4


# %% Scaling
# Scaling Incoming and Plot the Data
# Min Max Scaling
# Keep it simple
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

df[['loan_amnt_scaled']] = scaler.fit_transform(df[['loan_amnt']]) 
print('// complete ....... scaling')

fig, ax = plt.subplots(2, sharex=False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)
#ax[1].yaxis.set_ticks_position('left')
#ax[1].xaxis.set_ticks_position('bottom')

sns.histplot(data=df, x='loan_amnt', fill=False, color='black', ax=ax[0])
sns.histplot(data=df, x='loan_amnt_scaled', fill=False, color='black', ax=ax[1])

ax[0].set_title('Loan Amnt  (Absolut)')
ax[1].set_title('Loan Amnt  (Max and Min Scaled)')
plt.tight_layout()
sNameFigure = string_log_folder + '/' + 'fig_MinMaxScaled' + '.pdf'
plt.savefig(sNameFigure)
plt.close()
print('// complete ....... figure')




# %%
# --------------
# Count Plot
# --------------
# Question: What is the purpose distribution of loans?
# Why is this question relevant?
# Show the counts of observations in each category.
# We use bars to split our dataset by setting breakpoints.
# In Spyder the quality could be a problem. Therefore, we use dpi param.
# You can also save the image as pdf
plt.figure()
ax = sns.countplot(x='purpose', data=df)
plt.savefig(string_log_folder + '/' + 'fig_Purpose.png')
plt.close()

# Upgrade: Without borderlines
fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax = sns.countplot(x='purpose', data=df, palette='Greys')
plt.xticks(rotation=45, fontsize=6)
plt.xlabel('Purpose')
plt.ylabel('Count')
plt.title('Purpose of Use')
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'fig_PurposeImprove_300.png', dpi=300)
plt.close()

# %%
# --------------
# Boxplot
# --------------
# Question:
# What is the interest rate per class?
plt.figure()
sns.boxplot(x='grade', y='loan_amnt', data=df, showfliers=False, palette='Greys')
plt.xticks(rotation=45, fontsize=6)
plt.title('Loan Amount by Class')
plt.savefig(string_log_folder + '/' + 'fig_GradesLoanAmountImprove.png')
plt.close()


# %%
# --------------
# plot.bar
# --------------
# Selected all loan status.
print(df['loan_status'].unique())

LBad_indicators = ['Charged Off',
                    'Default',
                    'Does not meet the credit policy. Status:Charged Off',
                    'In Grace Period',
                    'Default Receiver',
                    'Late (16-30 days)',
                    'Late (31-120 days)']

# Define a bad loan in our DataFrame.
# Add all bad loans in our DataFrame.
df['bad_loan'] = 0
df.loc[df.loan_status.isin(LBad_indicators), 'bad_loan'] = 1

# Using croup by
dict_risk = df.groupby(['grade'])['bad_loan'].mean().sort_values().to_dict()
print(dict_risk)

plt.figure()
df.groupby(['grade'])['bad_loan'].mean().sort_values().plot.bar()
plt.ylabel('Percentage of Bad Debt')
plt.savefig(string_log_folder + '/' + 'fig_RiskProfile.png')
plt.close()


# %%
# --------------
# Boxplot
# --------------
# Question: Loan interest by class
# Why is this question relevant?

plt.figure()
sns.boxplot(x='grade', y='int_rate', data=df)
plt.savefig(string_log_folder + '/' + 'fig_GradesIntRate.png')
# plt.show()
plt.close()

# # Final plot.
plt.figure()
sns.boxplot(x='grade', y='int_rate', data=df,
             showfliers=False, palette='Blues',
             order=['A', 'B', 'C', 'D', 'E', 'F', 'G'])
plt.xticks(rotation=45, fontsize=6)
plt.title('Interest Rat and Grade in Order')
plt.savefig(string_log_folder + '/' + 'fig_GradesIntRateOrder.png')
# plt.show()
plt.close()
print('// complete ....... data exploring part I')


# %%
# --------------
# Heatmap
# --------------
# Create a Heatmap for corr()
#  # or df.loc[:, ['C', 'D', 'E']
# Rember data:
# loanAmnt = The listed amount of the loan applied for by the borrower.
# If at some point in time, the credit department
# reduces the loan amount, then it will be reflected in this value.

# installment = The monthly payment
# owned by the borrower if the loan originates.

# annualInc = The self-reported annual income provided
# by the borrower during registration.

# dti = A ratio calculated using the borrower’s total monthly
# debt payments on the total debt obligations,
# excluding mortgage and the requested LC loan,
# divided by the borrower’s self-reported monthly income.

df_ForCorr = df[['loan_amnt', 'int_rate', 'installment', 'annual_inc', 'dti']]
corr = df_ForCorr.corr()

# Create Corr figure with headmap.
plt.figure()
sns.heatmap(corr,
        xticklabels=corr.columns,
        yticklabels=corr.columns, annot=True)
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'fig_CoreHeatmap.pdf')
# plt.show()
plt.close()


# %%
# Update the corr plot with mask.
# Generate a mask for the upper triangle.
# @source: https://seaborn.pydata.org/examples/many_pairwise_correlations.html
# @code: np.zeros_like() return an array of zeros with the same shape and type as a given array.
# @code: np.triu_indices_from() return the indices for the upper-triangle of arr.

plt.figure()
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corr,
        xticklabels=corr.columns,
        yticklabels=corr.columns, annot=True, mask=mask)
plt.tight_layout()
plt.savefig(string_log_folder + '/' + 'fig_CoreHeatmapUpdate.pdf')
plt.close()
print('// complete ....... data exploring part II')


# %%
# --------------
# cloroplot
# --------------
# More plots here
# We define a function for plotting the data on a cloropleth plot. A cloropleth
# plot allows us to plot data on an (interactive) map. Why should we use a function?
# Because we will use it multiple times, so we make our code cleaner.
# Type in your terminal: pip3 install plotly

state_mean = pd.DataFrame(df.groupby('addr_state')['loan_amnt'].mean())
from plotly.offline import plot
import plotly.graph_objects as go

def cloroplot(data, z, title):
    fig = go.Figure(data=go.Choropleth(
        locations=data.index,  # Spatial coordinates
        z=data[z].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="in USD",
    ))

    fig.update_layout(
        title_text=title,
        geo_scope='usa',  # limite map scope to USA
    )
    plot(fig)
cloroplot(state_mean, 'loan_amnt', 'Mean loans by State')
print('// complete ....... data exploring part III')
