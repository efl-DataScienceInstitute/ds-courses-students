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

# We need an index for the DataFrame. But the data is not iterrows.
index = 0
int_error_count = 0
# Define a storage Pandas DataFrame.
# We will use the same column names as the raw data structure from gitHub.
# Don't repeat yourself (DRY). Therefore, the list.
# list_column_names = ['app_id', 'name', 'release_date', 'is_free', 'price_overview', 'languages', 'type']
list_column_names = ['app_id', 'is_free_control', 'price_clean']
df_games_price = pd.DataFrame(columns=list_column_names)

for row in data:

    if row['is_free'] == '1':
        continue

    str_row = str(row)
    # Clean the hole row by using the row as String
    str_row = str_row.replace('\\"', '')
    str_row = str_row.replace('\\', '')
    str_row = str_row.replace(': [', '')
    str_row = str_row.replace("'", "")

    # Get the final formatted price using regex.
    # @source: https://stackoverflow.com/questions/3368969/find-string-between-two-substrings
    if 'final_formatted' in str_row and '€' in str_row:
        result = re.search('final_formatted:(.*)€,', str_row)
        str_price_final_formatted = result.group(1)
        if ', --' in str_price_final_formatted:
            str_price_final_formatted = str_price_final_formatted.replace(', --', ',00')

        str_price_final_formatted = str_price_final_formatted.replace(" ", "")
        str_price_final_formatted = str_price_final_formatted.replace(",", ".")

    #    print(str_row)
    #    print(str_price_final_formatted)
    try:
        float_price = float(str_price_final_formatted)
    except:
        print('error: ', row)
        continue

    df_games_price.loc[index, list_column_names[0]] = row['app_id']
    df_games_price.loc[index, 'is_free_control'] = row['is_free']
    df_games_price.loc[index, 'price_clean'] = float_price

    index += 1
    if index % 10000 == 0:
        df_games_price.to_csv('../../data/raw_games_price.csv', sep=';', index=False)
        logging.info('// complete ...... games loop %s backup created' % index)
        print('// complete ...... games loop %s backup created' % index)

# Save the file once it is done
df_games_price.to_csv('../../data/raw_games_price.csv', sep=';', index=False)
logging.info(
    '// complete script .......  main_get_the_data_games took %s seconds' % round((time.time() - start_time), 2))
print('// complete ....... converting loop data to DataFrame took %s seconds' % (time.time() - start_time))

print('// complete ....... script took %s seconds' % round((time.time() - start_time), 2))
