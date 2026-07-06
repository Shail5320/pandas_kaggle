import pandas as pd

# Creating data
# There are two core objects in pandas: the DataFrame and the Series.

# DataFrame
# A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. Each entry corresponds to a row (or record) and a column.

min_dat = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(type(min_dat)) #'pandas.DataFrame'

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
coffee = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

# Series
# A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create one with nothing more than a list:

(pd.Series([1, 2, 3, 4, 5]))
(pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A'))

# Check datatypes of columns/features
# print(min_dat.dtypes)

# Reading data files
# Being able to create a DataFrame or Series by hand is handy. But, most of the time, we won't actually be creating our own data by hand. Instead, we'll be working with data that already exists.

dat = pd.read_csv("organizations-100.csv")
dat.head()

# The pd.read_csv() function is well-endowed, with over 30 optional parameters you can specify. 
# For example, you can see in this dataset that the CSV file has a built-in index, which pandas did not pick up on automatically.
# To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.

org_dat = pd.read_csv("organizations-100.csv", index_col=0)
# print(org_dat.head())

# we can also save data as a csv
# print(coffee)
coffee.to_csv("Coffee_BobSue.csv")