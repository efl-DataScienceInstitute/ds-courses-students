# -------
# Preamble and Semantic Versioning
# -------
# Script the get the data for this project in a more user-friendly way.
# @author: Dr. Benjamin M. Henrich
# @since: 2024-12-13
# @update: 2024-12-13
# @version: 0.0.1
# @workload 60 min

# Access to the raw data
#@source: https://www.youtube.com/watch?v=qiNv3qv-YbU
#@source: https://github.com/NewbieIndieGameDev/steam-insights

import pandas as pd
import time
start_time = time.time()
import datetime
now = datetime.datetime.now()
import logging

logging.basicConfig(
    filename='../../log/log_' + now.strftime('%Y-%m-%d_%H-%M') + '.log',
    encoding='utf-8',
    filemode='a',
    format='{asctime} - {levelname} - {message}',
    style='{',
    datefmt='%Y-%m-%d %H:%M',
)
logging.getLogger().setLevel(logging.INFO)
logging.info('// start ....... script')

# Extreme Fast, and in this cast helpful
# @source: https://medium.com/casual-inference/
# the-most-time-efficient-ways-to-import-csv-data-in-python-cc159b44063dle due to the data structure.
import csv
import re

str_input_file = '../../data/git/games.csv'
data = csv.DictReader(open(str_input_file))
logging.info('// complete ....... csv.DictReader')
print('// complete ....... csv.DictReader took %s seconds' % round((time.time() - start_time), 2))

# @param: row from csv.DictReader object
# @since: 2024-12-14
# @update: 2024-12-14
# @version: 0.0.1
# @workload 10 min
# df_steamspy_insights.to_csv('../../data/raw_steamspy_insights.csv', index=False)
# note: No need this data are in Steamspy!
def get_first_release_price_when_available(row):
    str_row_data = str(row)
    # list_release_price = re.findall('[,0-9]{1,10}€{1}', str_row_data)

    list_release_price = re.findall('[,0-9]{1,10}€', str_row_data)
    if len(list_release_price) > 1:
        first_release_price = str(list_release_price[0])
        first_release_price = first_release_price.replace('€', '')
    else:
        first_release_price = None
    return first_release_price

# Define a storage Pandas DataFrame.
# We will use the same column names as the raw data structure from gitHub.
# Don't repeat yourself (DRY). Therefore, the list.
# list_column_names = ['app_id', 'name', 'release_date', 'is_free', 'price_overview', 'languages', 'type']
list_column_names = ['app_id', 'name', 'release_date', 'is_free']
df_games = pd.DataFrame(columns=list_column_names)

# We need an index for the DataFrame. But the data is not iterrows.
index = 0
for row in data:
    df_games.loc[index, list_column_names[0]] = row[list_column_names[0]]
    df_games.loc[index, list_column_names[1]] = row[list_column_names[1]]
    df_games.loc[index, list_column_names[2]] = row[list_column_names[2]]
    df_games.loc[index, list_column_names[3]] = row[list_column_names[3]]

    index += 1
    if index % 10000 == 0:
        df_games.to_csv('../../data/raw_games.csv', sep=';', index=False)
        logging.info('// complete ...... games loop %s backup created' % index)
        print('// complete ...... games loop %s backup created' % index)

# Save the file once it is done
df_games.to_csv('../../data/raw_games.csv', sep=';', index=False)
logging.info(
    '// complete script .......  main_get_the_data_games took %s seconds' % round((time.time() - start_time), 2))
print('// complete ....... converting loop data to DataFrame took %s seconds' % (time.time() - start_time))

print('// complete ....... script took %s seconds' % round((time.time() - start_time), 2))
