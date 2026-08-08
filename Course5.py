import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv")

(reviews.describe())

# The data type for a column in a DataFrame or a Series is known as the dtype.
(reviews.dtypes)
(reviews.price.dtype)

# It's possible to convert a column of one type into another wherever 
# such a conversion makes sense by using the astype() function. For example, 
# we may transform the points column from its existing int64 data type into a 
# float64 data type:

(reviews.points.astype('float64'))

# Entries missing values are given the value NaN, short for "Not a Number".
# For technical reasons these NaN values are always of the float64 dtype.
# Pandas provides some methods specific to missing data. To select NaN entries
# you can use pd.isnull() (or its companion pd.notnull()). This is meant to be used thusly:

(reviews[pd.isnull(reviews.country)])

# we can fill the nan with any particular value by
reviews["region_2"] = reviews.region_2.fillna("Unknown", inplace=True)
# print(reviews.region_2)

# we may also replace the data in a field using the replace command
# we can fill the nan with any particular value by
reviews["taster_twitter_handle"] = reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
print(reviews.taster_twitter_handle)