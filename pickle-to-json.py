import pickle
import pandas as pd
from sys import argv

script, filename = argv

# Load the pickle format file
input_file = open(filename, 'rb')
new_dict = pickle.load(input_file)

# Create a Pandas DataFrame
df = pd.DataFrame.from_dict(new_dict, orient='index')

# Copy DataFrame index as a column
df['index1'] = df.index

# Move the new index column to the front of the DataFrame
index1 = df['index1']
df.drop(labels=['index1'], axis=1, inplace=True)
df.insert(0, 'index1', index1)

# Convert to json values
json_df = df.to_json(orient='values', date_format='iso', date_unit='s')

# Create and record the JSON data in a new .JSON file
with open('data.json', 'w') as js_file:
    js_file.write(json_df)
