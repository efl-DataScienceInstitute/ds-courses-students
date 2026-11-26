# Preamble and Semantic Versioning
# -------
# Script the get the data for this project in a more user-friendly way.
# @author: Dr. Benjamin M. Henrich
# @since: 2025-12-10
# @update: 2025-12-10
# @version: 0.0.1
# @workload 60 min

import pandas as pd
import csv
import time
start_time = time.time()

str_input_file = '../../data/git/steamspy_insights.csv'

data = csv.DictReader(open(str_input_file))

# Create the DataFrame in a better readable form.
list_column_names = ['app_id', 'developer', 'publisher', 'owners_range', 'concurrent_users_yesterday', 'playtime_average_forever', 'playtime_average_2weeks', 'playtime_median_forever', 'playtime_median_2weeks', 'price', 'initial_price', 'discount', 'languages', 'genres']
df_steamspy_insights = pd.DataFrame(columns=list_column_names)

index = 0
for row in data:

    # Extract all columns in one row
    for jIndex in range(0, len(list_column_names)):
        df_steamspy_insights.loc[index, list_column_names[jIndex]] = row[list_column_names[jIndex]]

    index += 1
    if index % 10000 == 0:
        df_steamspy_insights.to_csv('../../data/raw_steamspy_insights.csv', sep=';', index=False)
        print('// complete ...... games loop %s backup created' % index)

df_steamspy_insights.to_csv('../../data/raw_steamspy_insights.csv', sep=';', index=False)

print('// complete .......  scrip took %s seconds' % round((time.time() - start_time), 2))
