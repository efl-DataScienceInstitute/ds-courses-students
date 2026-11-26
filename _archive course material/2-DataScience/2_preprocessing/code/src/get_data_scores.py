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

str_input_file = '../../data/git/reviews.csv'

data = csv.DictReader(open(str_input_file))

# Create the DataFrame in a better readable form.
list_column_names = ['app_id', 'review_score', 'review_score_description', 'positive', 'negative', 'total', 'metacritic_score', 'reviews', 'recommendations', 'steamspy_user_score', 'steamspy_score_rank', 'steamspy_positive', 'steamspy_negative']
scores = pd.DataFrame(columns=list_column_names)

index = 0
for row in data:

    # skip trash rows, if the app_id is not an IDs
    if not row['app_id'].isdigit():
        print(row['app_id'])
        continue

    # Extract all columns in one row
    for jIndex in range(0, len(list_column_names)):
        scores.loc[index, list_column_names[jIndex]] = row[list_column_names[jIndex]]

    index += 1
    if index % 10000 == 0:
        scores.to_csv('../../data/raw_scores.csv', sep=';', index=False, encoding='utf-8')
        print('// complete ...... raw_scores loop %s backup created' % index)

# Whe need encoding="utf-8".
scores.to_csv('../../data/raw_scores.csv', sep=';', index=False, encoding='utf-8')
print('// complete ....... script took %s seconds' % round((time.time() - start_time), 2))
