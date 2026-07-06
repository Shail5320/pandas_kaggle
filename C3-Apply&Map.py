import pandas as pd

# Series.map(): The Value Substituter
# map() operates element-wise on a single pandas Series (a single column). 
# It is highly optimized for substituting each value in a Series with another value.

# Accepts: A dictionary, a function, or another Series

df = pd.DataFrame({'Role': ['Admin', 'User', 'Guest', 'Admin']})
print(df)

# Using a dictionary to map values
role_codes = {'Admin': 1, 'User': 2, 'Guest': 3}
df['Role_Code'] = df['Role'].map(role_codes)
print(df)


# Series.apply(): The Complex Function Caller
# Like map, Series.apply() operates element-wise on a single column.
# However, it is designed specifically for applying functions (both built-in and custom).

# Accepts: Only a callable (a function, lambda, or method).

df = pd.DataFrame({'Price': [10.0, 20.0, 30.0]})
print(df)

# A custom function that takes an extra argument
def add_tax(price, tax_rate):
    return price + (price * tax_rate)

# We can pass the 'tax_rate' argument using apply
df['Price_with_Tax'] = df['Price'].apply(add_tax, tax_rate=0.05)
print(df)


# DataFrame.apply(): The Row/Column Aggregator
# When you call apply() on an entire DataFrame (rather than just one column)
# ,it no longer operates element-by-element. Instead, it operates axis-wise. 
# It passes entire rows or entire columns to your function as a Series.

# Accepts: A callable.

df = pd.DataFrame({'Math': [90, 80], 'Science': [85, 95]})

# Calculate the difference between Math and Science for each row
df['Difference'] = df.apply(lambda row: row['Math'] - row['Science'], axis=1)
print(df)


# If you want to apply a function to every single element across
# an entire DataFrame (multiple columns at once), you use DataFrame.map().

df = pd.DataFrame({'A': [1.123, 2.456], 'B': [3.789, 4.012]})

# Format every single number in the DataFrame to 1 decimal place
df_rounded = df.map(lambda x: f"{x:.1f}")
print(df_rounded)

# The function you pass to map() should expect a single value from the Series 
# (a point value, in the above example), and return a transformed version of that value.
# map() returns a new Series where all the values have been transformed by your function.
# apply() is the equivalent method if we want to transform a whole DataFrame by 
# calling a custom method on each row.

