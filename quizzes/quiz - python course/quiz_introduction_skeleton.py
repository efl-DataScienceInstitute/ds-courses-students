import pandas as pd
import numpy as np

df = pd.read_csv("vgsales.csv")

#%%
##Q1: In 2010, which gaming platform had the largest global sales?
##What is the magnitude of aggregated sales?

#filter the dataframe for the year 2010
sub_select = 

#group by platform and calculate the sum of global sales for each platform
platform_sales = 

#best platform
top_sales = 
top_platform = platform_sales[...].index[0]

print("The best platform is", top_platform, "with", top_sales, "sales.")

#worst platform
worst_sales = 
worst_platform = platform_sales[...].index[0]

print("The worst platform is", worst_platform, "with", worst_sales, "sales.")



#%%
##Q2: how many games are new in 2013, i.e., that are not listed in previous years?
##use set operators

#select the unique names of the games in 2013
new_games = df[...]["Name"]. ...()

#select the unique names of the games before 2013
old_games = df[...]["Name"]. ...()

#use set
unique_new_games = ...(new_games) - ...(old_games)

#number of new unique games
number_unique_games = 

print("We have", number_unique_games, "new unique games in 2013.")




#%%
##Q3: what is the name of the game with longest name?
#save all names in a list
game_names = 

#use a for loop
longest_name = ""
for name in game_names:
    if ... :
        ...
    else:
        pass

print("The longest name is", longest_name)

#Question: why do we define longest_name = "" ? 


#%%
##Q3.2: what is the name of the game with shortest  name?
#use a for loop
shortest_name = game_names[0]
for name in game_names:
    if ... :
        ...
    else:
        pass

print("The shortest name is", shortest_name)

#Question: why do we define shortest_name = game_names[0] ? 
#          Why is it different from the longest_name?




#%%
##Q4: Is Global_Sales = NA_Sales + EU_Sales + JP_Sales + Other_Sales always true?
##create a new column Calc_Sales
... = df["NA_Sales"] + df["EU_Sales"] + df["JP_Sales"] + df["Other_Sales"]

#create a column Diff_Sales


#count the number of rows that are not 0 --> Tipp: for-loop
counter = 0
for ...

print("There are", counter, "mismatches.")

#%%
##Q: create descriptive statistics
desc_diff_sales = 
print(desc_diff_sales)



#%%
##Q5: Find all games that contain the word Mario and write Name, Platform, and Year to a csv file in a new folder 'Mariogames'
import os
mario_games = df[... .str. ...(..., case=False, na=False)]

#how many mario games do we have
print("There are", ... , "Mario games.")

#%%
##write Name, Platform, and Year to a csv file in a new folder 'Mariogames'
#%%
##write Name, Platform, and Year to a csv file in a new folder 'Mariogames'
filtered_mario_games = mario_games[["Name", "Platform", "Year"]]

directory = os.getcwd()
... = directory + '/Mariogames'
if ... os.path.exists(string_log_folder):
    os.makedirs(...)

mario_games.to_csv('Mariogames/Mariogames.csv')

#%%
# Plot the Number of Mario Games per platform in a bar chart
import seaborn as sns
import matplotlib.pyplot as plt
mario_games_by_platform = 

indexes_of_mario_games = mario_games_by_platform. ...

# Generate the bar plot
plt.figure()
ax = sns.barplot(y=..., x=..., color='darkblue')
plt.xticks(rotation=45, fontsize=6)
plt.ylabel('Mario Games')
plt.xlabel('Platform')
plt.savefig('Mario games by platform.pdf')
plt.show()




#%%
#Q6: Name your 3 favorite games and save each as a string in a variable
#example:
#favorite_game = "Wii Sports"

favorite_game = 
second_place = 
third_place = 

#%%
#write function that checks if the game is part of our dataset
def check_name(...):

    








#%%
#test your function with the following games
game_1 = "Counter-Strike"
game_2 = "Destiny"
game_3 = "EFL DS Course"





#%%
#now check if your favorite games are included in the dataset




#%%
#if your favorite games are not included, you can use these games instead from here on (they exist in our dataset)
review_game_1 = "Mario Kart DS"
review_game_2 = "Pokemon Red/Pokemon Blue"
review_game_3 = "Nintendogs"

#write a short review of your favorite games and save them as variables
review_1 = 
review_2 = 
review_3 = 

#create a new dataframe with each name of the game as first column and your review as second column -->Tipp:use lists
my_games = 


my_reviews = 


my_ranking = pd. ...





#%%
#get the corresponding rows from our dataset
#Note: some games might be released on multiple platforms
#      if that is the case, you need to drop the additional rows from the following df
filtered_df = df.loc[(df["Name"] == my_games[0]) | (df["Name"] == my_games[1]) | (df["Name"] == my_games[2])]

#Question: What do we do in the row where we create the filtered_df?

#add the information from the filtered_df to our ranking --> Tipp: merge
my_ranking = 


































