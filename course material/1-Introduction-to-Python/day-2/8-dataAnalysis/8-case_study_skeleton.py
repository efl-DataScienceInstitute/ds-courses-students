

# %% making the data ready for analysis


# Import libraries
import pandas as pd
import numpy as np

# %%
#read data to dataframe
df = pd.read_csv("vgsales.csv")

# %%
#perform cleaning from the pandas lecture
#get information on dataframe
print()

# %%
#check missing values
df_null_values = 
print(df_null_values)

# %%
#drop missing values
df = 
df.info()

# %%
#convert year to int
df['Year'] = 


#reset the index
df = 


# %% data analysis 1) information about the data set

# how does the data look like (show first rows - head)
df.

# %%
# shape of the DataFrame
df.

# %%
# information of the DataFrame
df.



# %% excursus groupby statements
#group data by genre
dfGenre = 

#get keys of groups
dfGenre.

#return indexes of the observations for a specific group
dfGenre.

#return DataFrame of all observations within a specific key
dfGenreAction = 

#perform some aggregate functions on the groups
#sum
print( )
#min
print( )
#max
print()


#descriptive statistics on the global sales for the year 2010
descriptives = 




# %% data analysis 2) some first statistics

# Question: How many unique Games, Publishers, Platforms, Genres, and Years are in the data set?

#overall statistics, get unique elements for the specific columns
games = 
publisher = 
platforms = 
genres = 
years = 

print('Games '+ str(len(games)),
      'Publishers '+str(len(publisher)),
      'Platforms '+str(len(platforms)),
      'Genres '+str(len(genres)),
      'Years '+str(len(years)),
      sep = '\n')



# %% data analysis 3) Year wise analysis

###

# Question: How have Video Game Sales and Releases developed over time?

# Global sales grouped by year (See lecture visualization)
import matplotlib.pyplot as plt
import seaborn as sns

# group data per year and calculate the sum
df_groupData = 
# get the sum per year for Global Sales
LdfGroupSales = 
LIndexesOfGroupData = 

### Please skip this block, visualization will be presented in the last lecture 
### Solutions will be provided
# Generate the bar plot


# %%
# video game releases by year
LdfReleases =  
LdfReleases.name = 
LIndexesOfReleases = 


### Please skip this block, visualization will be presented in the last lecture 
### Solutions will be provided
# Generate the bar plot


# %% data analysis 4) Publisher wise analysis

# Who are the most succesfull publishers?

#top 10 publishers by video game releases
LdfPubReleases =  df.groupby('')[''].count().reset_index()
LdfPubReleases.columns = 
LdfPubReleases =  # drop drops the old index, otherwise it is saved as a new column

#print the top 10 publishers by releases
print()


# %%
#top 10 publishers by video game sales
LdfPubSales =  df.groupby('')[''].sum().reset_index()
LdfPubSales = 

#print the top 10 publishers by sales
print()


# %%
#top 10 publishers by video game sales in europe and North America
LdfPubSalesEu =  
LdfPubSalesEu = 

LdfPubSalesNa =  
LdfPubSalesNa = 

#print the top 10 publishers by sales
print('EU_Sales:',
      ,
      'NA_Sales:',
     ,
      sep = '\n')

# %%
#top 10 publishers by video game sales between 2010 and 2015
LdfPubSalesYears = f[(df['']>= ) & (df['']<=)].groupby('')[''].sum().reset_index()
LdfPubSalesYears = 

#print the top 10 publishers by sales
print()


# %% data analysis 5) Platform wise analysis

# Question: Which platforms are the most (least) successful by sales

LdfPlatSales = 
LdfPlatSales =


print('The most successful platform is ' + )
print('The least successful platform is ' + )

# %% data analysis 6) Genre wise analysis

# Question: What is the most popular Genre by game releases of the ten most succesful platforms?

#get the 10 most successful platforms
Platforms = 

#save results in dictionary
results = dict()

#get most popular Gerne for each platform
for  in :
    LdfGenre = 
    LdfGenre = 
    results[platform] = 

#print results
print()





