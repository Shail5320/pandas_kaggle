import pandas as pd

# Iterating through data gives us the attributes or the columns (features)
bus_org = pd.read_csv("organizations-100.csv")
for i in bus_org:
    # print(i)
    pass

# In Python, we can access the property of an object by accessing it as an attribute.
bus_org.Country # gives indexed countries value 

# If we have a Python dictionary, we can access its values using the indexing ([]) operator.
#  We can do the same with columns in a DataFrame:
bus_org["Country"]

# NOTE : for a column with a space seperated name dont use the attribute method to fetch value

# Accessing Values
bus_org["Founded"][1]
# bus_org["Industry"][1]
# bus_org["Country"][2]

# index-based selection: selecting data based on its numerical position in the data.
#  iloc follows this paradigm.

# To select the first and second row of data in a DataFrame
bus_org.iloc[0]
bus_org.iloc[1]

# Both loc and iloc are row-first, column-second. 
# This is the opposite of what we do in native Python, which is column-first, row-second.

# print(bus_org)

# This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns.
bus_org.iloc[1:6, 2:4]
# we are getting the first column with the rows (just that column )as well

# It's also possible to pass a list:
bus_org.iloc[[0, 1, 2], [2,3,5]]

# Finally, it's worth knowing that negative numbers can be used in selection.
#  This will start counting forwards from the end of the values
bus_org.iloc[-4:, 2:6]

# Label-based selection
# The second paradigm for attribute selection is the one followed by the loc operator: label-based selection. 
# In this paradigm, it's the data index value, not its position, which matters.

bus_org.loc[0, ["Description", "Name"]]

# iloc is conceptually simpler than loc because it ignores the dataset's indices. '
# 'When we use iloc we treat the dataset like a big matrix (a list of lists), '
# 'one that we have to index into by position. loc, by contrast, uses the information '
# 'in the indices to do its work. Since your dataset usually has meaningful indices, '
# 'it's usually easier to do things using loc instead

# iloc uses the Python stdlib indexing scheme, where the first element of the range is included 
# and the last one excluded. So 0:10 will select entries 0,...,9. loc, 
# meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

# Label-based selection derives its power from the labels in the index. 
# Critically, the index we use is not immutable. We can manipulate the index in any way we see fit.
# The set_index() method can be used to do the job

bus_org.set_index("Organization Id")
# if you dont use the inplace parameter, the func returns a new dataframe instad of making changes to real one


# Conditional Selections

# this returns the rows or entries which satisfy the conditional statement
bus_org.loc[bus_org["Number of employees"] == 4000]

# This just returns a series of Booleans corresponding to the conditional statement
bus_org.loc[:, "Number of employees"] == 4000


bus_org.dtypes

# type conversion of a column/feature
bus_org["Number of employees"] = bus_org["Number of employees"].astype(int)

# use the ampersand (&) to bring the two questions together:
# data frame filtering using multiple conditionals
bus_org.loc[(bus_org["Number of employees"] >= 2500) & (bus_org["Founded"] >= 2010)]

# we can use the or as well
bus_org.loc[(bus_org["Number of employees"] >= 2500) | (bus_org["Founded"] >= 2015)]

# Conditional Sectors : isin is lets you select data whose value "is in" a list of values.
bus_org.loc[bus_org.Industry.isin(['Plastics', 'Transportation'])]

# The second is isnull (and its companion notnull). 
# These methods let you highlight values which are (or are not) empty (NaN)

bus_org.loc[bus_org.Industry.notnull()]
bus_org.loc[bus_org.Industry.isnull()]


# Assigning Values
# makes a new colums named profits and assigns True or any other value to it
bus_org["Profitable"] = True
bus_org['index_backwards'] = range(len(bus_org), 0, -1)

# print(bus_org)