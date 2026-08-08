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
(reviews)

# Both the row index and the column index can have their own name attribute.
# The complimentary rename_axis() method may be used to change these names

(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

# Combining

# he simplest combining method is concat(). Given a list of elements, this function will 
# smush those elements together along an axis.

canadian_youtube = pd.read_csv("CAvideos.csv")
states_youtube = pd.read_csv("USvideos.csv")

print(canadian_youtube.shape)
print(states_youtube.shape)

print(pd.concat([canadian_youtube, states_youtube]))

# The middlemost combiner in terms of complexity is join(). 
# join() lets you combine different DataFrame objects which have an
# index in common.

left = canadian_youtube.set_index(['title', 'trending_date'])
right = states_youtube.set_index(['title', 'trending_date'])

joined_df = left.join(right, lsuffix='_CAN', rsuffix='_US')
print(joined_df)