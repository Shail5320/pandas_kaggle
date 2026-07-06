import pandas as pd

# ometimes we have to do some more work ourselves to reformat it for the task at hand.
#  This tutorial will cover different operations we can apply to our data to get the
# input "just right".

bus_org = pd.read_csv("organizations-100.csv")

# Pandas provides many simple "summary functions" (not an official name) which 
# restructure the data in some useful way. For example, consider the describe() method:

(bus_org["Number of employees"].describe())

# This method generates a high-level summary of the attributes of the given column. 
# It is type-aware, meaning that its output changes based on the data type of the input. 
# The output above only makes sense for numerical data; for string data here's what we get:

(bus_org["Industry"].describe())

# To see a list of unique values we can use the unique() function:

(bus_org["Industry"].unique())

# To see a specific statistical feature

(bus_org["Number of employees"].mean())

# To see a list of unique values and how often they occur in the dataset,
#  value_counts() is used ,its just gives you the frequency of elements
(bus_org["Number of employees"].value_counts())

# A map is a term, borrowed from mathematics, for a function 
# that takes one set of values and "maps" them to another set of values. 
bus_org_founded_mean = bus_org.Founded.mean()
print(bus_org.Founded.map(lambda p: p - bus_org_founded_mean))

# The function you pass to map() should expect a single value from the Series (a point value, in the above example),
# and return a transformed version of that value. map() returns a new Series where all the values have been transformed by your function.
