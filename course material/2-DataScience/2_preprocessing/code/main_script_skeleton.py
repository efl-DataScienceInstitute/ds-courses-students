# -------
# Preamble and Semantic Versioning
# -------
# Main script
# @author: Dr. Benjamin M. Henrich
# @since: 2024-12-13
# @update: 2024-12-17
# @version: 1.0.0
# @workload 120 min
# View for yesterday means  (e.g., 2024-10-27)
# Today’s date: 2024-10-28

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime
import time

start_time = time.time()
now = datetime.datetime.now()

# %% Folder Management
# Create an output folder for artifacts using today's date
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d')

string_artifacts_folder = '../artifacts/' + 'artifacts' + '_' + date_time
if not os.path.exists(string_artifacts_folder):
    os.makedirs(string_artifacts_folder)
print('// Folder creation complete: ', string_artifacts_folder)

# %% Logging Setup
import logging
logging.basicConfig(
    filename=string_artifacts_folder + '/' + 'log.log',
    encoding='utf-8',
    filemode='a',
    format='{asctime} - {levelname} - {message}',
    style='{',
    datefmt='%Y-%m-%d %H:%M',
)
logging.getLogger().setLevel(logging.INFO)
logging.info('// Starting main script execution...')

# --------------
# %% Data Loading
# --------------
# Load raw data from CSV files
df_games = pd.read_csv('../data/raw_games.csv', sep=';', encoding='utf-8', low_memory=False)
df_steam_spy = pd.read_csv('../data/raw_steamspy_insights.csv', sep=';', encoding='utf-8',
                           low_memory=False)
df_scores = pd.read_csv('../data/raw_scores.csv', sep=';', encoding='utf-8', low_memory=False)
df_games_price = pd.read_csv('../data/raw_games_price.csv', sep=';', encoding='utf-8', low_memory=False)

logging.info('// Data successfully loaded...')
print('// Data successfully loaded...')

# --------------
# %% Data Pre-Processing
# --------------
# Merge dataframes into a single dataframe on 'app_id'
df = df_games.merge(df_steam_spy, how='left', on='app_id')
df = df.merge(df_scores, how='left', on='app_id')
df = df.merge(df_games_price, how='left', on='app_id')

# Create a backup of the raw merged dataframe for verification purposes
df_raw = df
print(df.info())

# %% Convert Release Date
# Convert 'release_date' column to datetime format
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d', errors='coerce')

# %% Extract Specific Game
# Extract data for the game 'Satisfactory' for testing purposes
df_Satisfactory = df[df['name'] == 'Satisfactory']

# %% Ownership Estimation
# Define a function to estimate ownership (conservative approach)
# This function parses the ownership range string and extracts the lower bound.
# Handles invalid inputs using try-except for safety.
# @author: Ben, @since: 2024-12-15, @version: 1.0.0
def get_lower_bound_ownership(string_input):
    if not isinstance(string_input, str) or len(string_input) <= 3:
        return None
    try:
        list_lower = string_input.split('..')
        str_lower = list_lower[0]
        str_lower = str_lower.replace(',', '')
        float_lower = float(str_lower)
    except:
        return None
    return float_lower

# Apply the function to extract lower-bound ownership estimates
df['owners_conservative'] = df['owners_range'].apply(get_lower_bound_ownership)

# %% Replace Missing Values
# Replace all occurrences of '\\N' with NaN
df = df.replace({'\\N': None})

# %% Convert Prices
# Identify and list unique price values
list_price = df['price'].unique()

# --------------
# %% Data Exploration
# --------------
# Count distinct games based on 'app_id'
print('Number of unique games (App IDs): ', df['app_id'].nunique())

# Display the range of game release dates
print('Earliest game release date: ', df['release_date'].min())
print('Latest game release date: ', df['release_date'].max())

# --------------
# %% Research Questions
# --------------
# You can write your code here!

# --------------
# %% Data Modeling
# --------------
# ToDo ...

# --------------
logging.info('// complete ....... script')
print('// complete ....... script')