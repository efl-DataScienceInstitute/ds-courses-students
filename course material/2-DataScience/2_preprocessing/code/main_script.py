# -------
# Preamble and Semantic Versioning
# -------
# Main script
# @author: Dr. Benjamin M. Henrich
# @since: 2024-12-13
# @update: 2024-12-19
# @version: 1.2.0
# @workload 120 min
# View for yesterday means (e.g., 2024-10-27)

# %%
# -------
# Part I: Skeleton
# -------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import datetime
import time
start_time = time.time()

# %%
# Folder Management
# Create an output folder for artifacts using today's date
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d')

# Our storage folder for the artifacts.
string_artifacts_folder = '../artifacts/' + 'artifacts' + '_' + date_time
if not os.path.exists(string_artifacts_folder):
    os.makedirs(string_artifacts_folder)
print('// Folder creation complete: ', string_artifacts_folder)

# %%
# Logging Setup
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

# %%
# --------------
# Data Loading
# --------------
# Load raw data from CSV files
df_games = pd.read_csv('../data/raw_games.csv', sep=';', encoding='utf-8', low_memory=False)
df_steam_spy = pd.read_csv('../data/raw_steamspy_insights.csv', sep=';', encoding='utf-8',
                           low_memory=False)
df_scores = pd.read_csv('../data/raw_scores.csv', sep=';', encoding='utf-8', low_memory=False)
df_games_price = pd.read_csv('../data/raw_games_price.csv', sep=';', encoding='utf-8', low_memory=False)

logging.info('// Data successfully loaded...')
print('// Data successfully loaded...')

# %%
# --------------
# Data Pre-Processing
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

# %%
# Ownership Estimation
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

# %%
# --------------
# Data Exploration
# --------------
# Count distinct games based on 'app_id'
print('Number of unique games (App IDs): ', df['app_id'].nunique())

# Display the range of game release dates
print('Earliest game release date: ', df['release_date'].min())
print('Latest game release date: ', df['release_date'].max())

# %%
# --------------
# Research Questions
# --------------
# You can write your code here!

# %%
# -------
# Part II: Solution
# -------

# %%
# A) What are the top ten and lowest ten games according to the owners? (Tip: Use owners_conservative.)
# Sort games by conservative ownership estimate
df_game_top_twenty = df.sort_values(by=['owners_conservative'], ascending=False)[0:20]
df_game_last_twenty = df.sort_values(by=['owners_conservative'], ascending=True)[0:20]

# %%
# B) Which publishers are the most successful in the dataset based on the number of published games?
df_publisher_num_games = df.groupby('publisher')['name'].nunique().reset_index()
df_publisher_num_games = df_publisher_num_games.sort_values(by='name', ascending=False)
df_publisher_num_games.to_csv(string_artifacts_folder + '/' + 'df_publisher_game_count.csv',
                              index=False, header=True)

# %%
# C) How does the number of published games change over time?
df['year'] = df['release_date'].dt.year
fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
sns.countplot(x="year", data=df, color='gray')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_count_release_year.pdf')
plt.close()
print('// complete ....... figure: fig_count_release_year')

# %%
# D) What do the prices look like?
# Plot price trends over time.
# But before that lets check the NAN values!
plt.figure(figsize=(15,5))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='winter')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_heatmap_missing_values.png', dpi=300)
plt.close()
print('// complete ....... figure: fig_heatmap_missing_values')

# %%
df['price_clean'] = df['price_clean'].fillna(0).astype(float)

fig, ax = plt.subplots()
sns.scatterplot(x="year", y='price_clean', data=df)
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_scatter_year_price.pdf')
plt.close()
print('// complete ....... figure: fig_scatter_year_price')


# %%
# -------
# Part III: Further Ideas
# -------
# %%
fig, ax = plt.subplots()
sns.pairplot(df, corner=True)
plt.savefig(string_artifacts_folder + '/' + 'fig_pairplot_data_set.png', dpi=300)
plt.close()
print('// complete ....... figure: fig_pairplot_data_set')

# %%
# Extract top games with overwhelmingly positive reviews, sorted by ownership
df_game_top_and_Overwhelmingly = df[df['review_score_description'] == 'Overwhelmingly Positive'] \
    .sort_values(by=['owners_conservative'], ascending=False)[0:20]

# Calculate the average review score for publishers
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
df['review_score_description_label_encoder'] = label_encoder.fit_transform(df['review_score_description'])
df_publisher_review_score = df.groupby('publisher')['review_score_description_label_encoder'].mean().reset_index()
df_publisher_review_score = df_publisher_review_score.sort_values(by=['review_score_description_label_encoder'], ascending=False)

# %% Genre Overview
# Extract the first genre from the 'genres' column
def get_first_genre(str_genres):
    if isinstance(str_genres, str) and ',' in str_genres:
        list_genres = str_genres.split(',')
        return list_genres[0]
    else:
        return str_genres

# Apply the function and calculate genre distribution
df['genre_first'] = df['genres'].apply(get_first_genre)

# We have 'Free to Play' and 'Free To Play'. Therefore, replace operation
df['genre_first'] = df['genre_first'].str.replace('To', 'to')
int_genres = df['genre_first'].unique()
print('Number of unique genres: ', int_genres)

# %%
list_count_genre = df['genre_first'].value_counts()
list_count_genre_labels = df['genre_first'].value_counts().index

# Create a pie chart showing genre distribution
plt.figure()
plt.pie(list_count_genre, labels=list_count_genre_labels, autopct='%1.1f%%')
plt.title('Game Distribution by Genre')
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_pie_plot_genres.pdf')
plt.close()
print('// complete ....... figure: fig_pie_plot_genres')

# %%
# Filtering the DataFrame according to conditions
df_review = df[(df['review_score_description'] == 'Overwhelmingly Positive') |
               (df['review_score_description'] == 'Very Positive') |
               (df['review_score_description'] == 'Mostly Positive') |
               (df['review_score_description'] == 'Positive') |
               (df['review_score_description'] == 'Negative') |
               (df['review_score_description'] == 'Very Negative') |
               (df['review_score_description'] == 'Very Negative') |
               (df['review_score_description'] == 'Overwhelmingly Negative')]

fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
sns.histplot(
    df_review,
    x="year", hue="review_score_description",
    multiple="stack",
    #palette="light:m_r",
    palette="rocket",
    edgecolor=".3",
    linewidth=.5,
)
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_histplot.pdf')
plt.close()

# Number of Players over time!
df_group_by_owners = df.groupby('year')['owners_conservative'].sum().reset_index()
df.reset_index()

fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
sns.barplot(data=df_group_by_owners, x='year', y='owners_conservative', color='gray')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_bar_owners_conservative.pdf')
plt.close()
print('// complete ....... figure: fig_bar_owners_conservative')


# %%
# --------------
# Feature Scaling: Normalization Vs. Standardization
# --------------
# Creating Plots to show the impact.

# Normalization Example:
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_normalized = pd.DataFrame(scaler.fit_transform(df[['price_clean']]), columns=['Observation'])

# Standardize data
# Z-Score Method.
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df[['price_clean']]), columns=['Observation'])

fig, ax = plt.subplots(3, sharex=False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].spines['top'].set_visible(False)

sns.histplot(data=df, x='price_clean', fill=False, color='black', ax=ax[0])
sns.histplot(data=df_normalized, x='Observation', fill=False, color='black', ax=ax[1])
sns.histplot(data=df_standardized, x='Observation', fill=False, color='black', ax=ax[2])

ax[0].set_title('Observation - price_clean')
ax[1].set_title('Observation - price_clean (Normalized [0 - 1])')
ax[2].set_title('Observation - price_clean (Standardized [(x - µ) / std ])')
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_normalized_standardized_price_clean' + '.pdf')
plt.close()
print('// complete ....... figure: fig_normalized_standardized_price_clean')

# %%
# --------------
# Outlier Detection and Removal
# --------------
# Find max Number of unique values in Plot.
SUnique_value_count = df['price_clean'].value_counts()
iMax_count = SUnique_value_count.max()

# Set Boundary
dMean = df['price_clean'].mean()
dStd = df['price_clean'].std()
iK = 3

dLowerBound = dMean - iK * dStd
dUpperBound = dMean + iK * dStd

df_price_clean_outlier = df[(df['price_clean'] < dLowerBound) | (df['price_clean'] > dUpperBound)]

fig, ax = plt.subplots()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
sns.histplot(data=df, x='price_clean', fill=False,color='black')

# @source: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html#matplotlib.axes.Axes.axvline
iPositionFactor = 1
ax.axvline(x=dMean, ymin=0, ymax=iMax_count, color='gray', linewidth=0.2)
plt.text(dMean, iMax_count*iPositionFactor, r'$\mu$', rotation=90)

# Lower and Upper Bounds
ax.axvline(x=dLowerBound, ymin=0, ymax=iMax_count, color='gray', linewidth=0.2)
plt.text(dLowerBound, iMax_count*iPositionFactor, r'$\mu + k * \sigma$', rotation=90)

ax.axvline(x=dUpperBound, ymin=0, ymax=iMax_count, color='gray', linewidth=0.2)
plt.text(dUpperBound, iMax_count*iPositionFactor,  r'$\mu + k * \sigma$', rotation=90)

ax.legend(prop={'size': 10}, frameon=False, loc='upper right')
plt.xlabel('Values')
plt.tight_layout()
plt.savefig(string_artifacts_folder + '/' + 'fig_histplot_outliers' + '.pdf')
plt.close()
print('// complete ....... fig_histplot_outliers')


# --------------
# %% Data Modeling
# --------------


# --------------
logging.info('// complete ....... script')
print('// complete ....... script took %s seconds' % round((time.time() - start_time), 2))

