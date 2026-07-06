import pandas as pd

# Groupwise analysis
# One function we've been using heavily thus far is the value_counts() function.
#  We can replicate what value_counts() does by doing the following:

# Value count returns the frequency of elements 

bus_org = pd.read_csv("organizations-100.csv")
# for i in bus_org:
#     print(i, bus_org[i].dtype)

(bus_org.dtypes)
(bus_org.Country.value_counts)
(bus_org.Country.is_unique)

reviews = pd.read_csv("winemag-data-130k-v2.csv")
print(reviews.dtypes)

# groupby() created a group of reviews which allotted the same point values to the 
# given wines. Then, for each of these groups, we grabbed the points() column and 
    # counted how many times it appeared. value_counts() is just a shortcut to this
#  groupby() operation.

(reviews.groupby('points').points.count())

# We can use any of the summary functions we've used before with this data.
# For example, to get the cheapest wine in each point value category, we can do
# the following:

print(reviews.groupby('points').price.min())

# each group we generate as being a slice of our DataFrame containing only data 
# with values that match. This DataFrame is accessible to us directly using the
#  apply() method, and we can then manipulate the data in any way we see fit

# one way of selecting the name of the first wine reviewed from each winery in the dataset
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# For even more fine-grained control, you can also group by more than one column
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# Another groupby() method worth mentioning is agg(), which lets you run a
#  bunch of different functions on your DataFrame simultaneously. 
reviews.groupby(['country']).price.agg([len, min, max])

# A multi-index differs from a regular index in that it has multiple levels.
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

# in general the multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method:
countries_reviewed.reset_index()

# To get data in the order want it in we can sort it ourselves.
#  The sort_values() method is handy for this.
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

# For Descending Order
countries_reviewed.sort_values(by='len', ascending=False)

# sort by more than one column at a time
countries_reviewed.sort_values(by=['country', 'len'])

