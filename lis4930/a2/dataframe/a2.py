# Assignment 2

## Developer: Christopher Valverde

### Program Requirements (data analysis and visualization steps):

1. Get
2. Clean
3. Prepare
4. Analyze
5. Display/Visualize (preparation)

# 1. import pandas (open source data analysis/science and AI package)
import pandas as pd

# Get Data

# 2. get mortality data: National Center for health Statistics (NCHS childhood mortality rates)
# info: https://data.cdc.gov/NCHS/NCHS-Childhood-Mortality-Rates/v6ab-adf5
mortality_url = "https://data.cdc.gov/api/views/v6ab-adf5/rows.csv"

# 3. read csv file into DataFrame
mortality_data = pd.read_csv(mortality_url)

# Save DataFrame to pickle file
# 4. save DF to Pickle file
# Why?
# https://towardsdatascience.com/stop-using-csvs-for-storage-pickle-is-an-80-times-faster-alternative-832041bbc199
mortality_data.to_pickle('mortality_data.pkl')

# 5. read pickle file
# Note: Below, data in mortality_data variable changed--no longer csv data, now pickle data!
mortality_data = pd.read_pickle('mortality_data.pkl')

# (First - examine, then...), clean, prepare, analyze, and display data

## Cleaning

### Note: Generally, the following items are done during "cleaning" process:

	1. Drop duplicate rows
	2. Drop rows and columns not needed
	3. Rename columns

# ways to print an entire Pandas DataFrame:
# https://www.geeksforgeeks.org/how-to-print-an-entire-pandas-dataframe-in-python/
# Or...
# display Pandas DataFrame in table style:
# https://www.geeksforgeeks.org/display-the-pandas-dataframe-in-table-style/
# 6. Display first and last five rows with one command!
# mortality_data # Note: *only* works in Jupyter Notebooks
print(mortality_data)

# 7. first 5 rows only
print(mortality_data.head())

# 8. last 3 rows only
mortality_data.tail(3)

# 9. using pandas option_context() function display 6 rows (first 3 and last 3) and all cols (Note: using odd numbers doesn't appear to work)
# Note: option_context() - executes codeblock with set of options that revert to prior settings after execution
# Note: 'None' value for 'display.max_colums' propeerty returns *all* cols.
with pd.option_context(
	'display.max_rows', 6,
	'display.max_columns', None):
	print(mortality_data)

# Display Dataframe attributes

# 10. print following DataFrame attributes: index, columns, size, and shape
print("Index:	", mortality_data.index)
print("Columns:", mortality_data.columns)
print("Size:	", mortality_data.size)
print("Shape:	", mortality_data.shape)

# 11. display DataFrame values in array format
print(mortality_data.values)

# Use columns attribute to change column names (i.e., remove any spaces)

# 12. Use columns attribute, and replace() function to remove spaces in column names
# removing spaces in column names good practice (otherwise, processing commands limited)
mortality_data.columns = mortality_data.columns.str.replace(" ", "")

# 13. print column names
print(mortality_data.columns)

# 14. print print column names with first 5 records
print(mortality_data.head())

# Use info(), nunique(), and describe() methods
# 15. print DataFrame information
mortality_data.info()

# 16. print DataFrame information, including accurate memory usage (using 'deep' value)
mortality_data.info(memory_usage='deep')

# 17. summarize unique values (i.e, no duplicates) in each column
mortality_data.nunique()

# 18. display generic stats for each numeric column - using describe() function
mortality_data.describe()

# 19. transpose stats so that stat names are displayed in columns (using T property)
mortality_data.describe().T

# 20. save cleaned DataFrame to pickle file (mortality_cleaned.pkl)
mortality_data.to_pickle('mortality_cleaned.pkl')

# 21. read cleaned pickle file to mortality_data variable
mortality_data = pd.read_pickle('mortality_cleaned.pkl')

# 22. display first 5 rows of cleaned pickle file
print(mortality_data.head())

# Accessing data

## Access data (columns)

# using dot notation
# Note: can't use dot notation with more than one column--or column names with spaces!
# 23. Display first two records of DeathRate column using dot notation.
print(mortality_data.DeathRate.head(2))

# 24. Same as above using single brackets
print(mortality_data['DeathRate'].head(2))

# 25. Same as above using double brackets
print(mortality_data[['DeathRate']].head(2))

# Note difference in types!
# 26. Display DeathRate type using dot notation.
# note type (Series)
print(type(mortality_data.DeathRate))

# 27. Display DeathRate type using single brackets.
# note type single brackets (Series)
print (type(mortality_data['DeathRate']))

# 28. Display DeathRate type using double brackets.
# note type double brackets (DataFrame)
print(type(mortality_data[['DeathRate']]))

# 29. Access moree than one column--*must* use brackets
print(mortality_data[['Year','DeathRate']].head(2))

# 30. Display Year and DeathRate type using double brackets.
# note type (DataFrame)
type(mortality_data[['Year','DeathRate']])

# Accessing rows

# 31. Access data using query() function (Year=1900)
print(mortality_data.query('Year==1900'))

# 32. Access data using query() function (Year=2000 and AgeGroup != 1 - 4 Years)
print(mortality_data.query('Year == 2000 and AgeGroup != "1-4 Years"'))

# 33. Access data using query() function (Year=1900 or Year=2000), display first 5 records
print(mortality_data.query('Year == 1900 or Year == 2000').head())

# Acess subset of rows and columns

# Note: use backticks if a column name contains spaces
# mortality_data.query('Year == 2000 and `Age Group` != "1-4 Years"')
# Note: after using query method on  subset can use either dot notation or brackets
# Generally, use brackets, return a DataFrame (easier to perform some operations), instead of Series object.

# 34. Using dot notation, access data using query() function (year=1900), only for DeathRate column, display first 5 records
print(mortality_data.query('Year == 1900').DeathRate.head())

# 35. Using single bracket notation, access data using query() function (year=1900), only for DeathRate column, display first 5 records
print(mortality_data.query('Year == 1900')['DeathRate'].head())

# 36. Using double bracket notation, access data using query() function (Year-1900), only for DeathRate column, display first 5 records
print(mortality_data.query('Year == 1900')[['DeathRate']].head())

# 37. Display data type of dot notation used above
print(type(mortality_data.query('Year == 1900').DeathRate.head()))

# 38. Display data type of single bracket notation used above
print(type(mortality_data.query('Year == 1900')['DeathRate'].head()))

# 39. Display data type of double bracket notation used above
print(type(mortality_data.query('Year == 1900')[['DeathRate']].head()))

# 40. using double bracket notation, access data using query() function (year=1900), for AgeGroup and DeathRate columns, display first 5 records
# Note: *must* use brackets with more than one column (return DataFrame)
print(mortality_data.query('Year == 1900')[['AgeGroup', 'DeathRate']].head())

# Access rows with loc[] accesor

# https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label
# Access rows with loc[] accessor (by labels) using list or slice, here using list
# 41. Display row values for 0,5 and 10 index 'labels'(Note: loc[] interpreted as 'label' of index--*not* integer position!)
# Note: here, they are the first, sixth, and 11th rows
mortality_data.loc[[0,5,10]]

# 42. verify index 'labels' and row values
mortality_data.head(11)

# 43. Access rows using *slice* (loc[] accessor includes stop values)
# generic syntax: loc[start:stop:step]
mortality_data.loc[4:6]

# 44. Acess rows using *slice*, include start, stop, and step values
mortality_data.loc[0:20:5]

# 45. Access rows using conditional expression (year=1917)
mortality_data.loc[mortality_data.Year == 1917]

# Access rows and columns with loc[] accessor
# 46. Display first and last 5 rows, of Year and Agegroup colums using loc[] accessor, with slice and list")
# Note: Here, includs all rows. However, will only display first and last 5 records
mortality_data.loc[:,['Year', 'AgeGroup']]

# Access subset of rows and columns with loc[] accessor
# 47. using loc[] accessor with lists for row and column labels, display row values for 0, 5, and 10 index 'labels',
# only for AgeGroup and Dethrate column labels)
mortality_data.loc[[0,5,10],['AgeGroup','DeathRate']]

#48. Here, using slices of rows and column labels
mortality_data.loc[4:6,'AgeGroup':'DeathRate']

# Access rows with iloc[] accessor
# https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-position
# access rows with iloc[] accessor (by positions) using list or slice, here using list
# 49. Display first, sixth, and 11th rows (Note: iloc[] interpreted as 'integer' position of indx--not label!)
mortality_data.iloc[[0,5,10]]

# 50. verify index 'positions' and row values
mortality_data.head(11)

# 51. Access rows using *slice* (Note:iloc[] accessor does *not* include stop value!)
# generic syntax: loc[start:stop:step]
mortality_data.iloc[4:6]

# 52. Access rows using *slice*, include start, stop, and step values (Note: iloc[] accessor does *not* include stop value!)
mortality_data.iloc[0:20:5]

# Access subset of rows and columns with iloc[] accessor--can use negative values
# 53. Display rows and colums using index positions and lists
mortality_data.iloc[[0,5,10],[1,2]]

# 54. Display rows and columns  using index postions and slices
mortality_data.iloc[4:7,1:3]

# 55. use iloc[] accessor with negative value
mortality_data.iloc[-10:]
