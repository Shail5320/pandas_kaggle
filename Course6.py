import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv")

(reviews.describe())

# rename lets you change index names and/or column names
reviews.rename(columns={'points': 'score'}, inplace=True)
# print(reviews.columns)

# rename() lets you rename index or column values by specifying 
# a index or column keyword parameter, respectively. It supports a
# variety of input formats, but usually a Python dictionary is the 
# most convenient. 

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
print(reviews)

# Both the row index and the column index can have their own name attribute.
# The complimentary rename_axis() method may be used to change these names

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')
