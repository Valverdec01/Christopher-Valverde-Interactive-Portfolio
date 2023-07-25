# Regression Analysis

## What is Regression analysis?

	1. Equation predicts **"unknown values"** (i.e dependent variables) based upon one or more known values (i.e, independent variable(s)).
	2. Dependent variables: response, outcome/output, or target variables (respond to changes in (an)other variables(s)).
	3. Independent variables: predicator, input, regressor, or explanatory variables (predict/explain changed values of dependent variables)
	4. Goal: find the best fitting line which can accurately predict the output.

Dependent variables (output on y-axis) are alwayas the one being studied-- that is, whose variation(s) is/are being modified somehow!

Independent variables (input on x-axis) are always the ones being manipulated, to study and compare the effects on the dependent variables(s).

https://www.statisticssolutions.com/independnt-and-dependent-variables/

https://www.scribbr.com/methodology/independent-and-dependent-variables/

*Note:* The designations independent and dependent variables are used to not imply "cause and effect" (as do "predictor" or "explanatory" terms)

*Note:* Based on the number of input and output variables, linear regression has three types:
	
	1. Simple linear regression (1 DV/1 IV)
	2. Multiple linear regression (1 DV/2 or more IVs)
	3. Multivariate linear regression (2 or more DVs/2 or more IVs)

Simple linear regression: Only *one* independent variable affecting *one* dependent variable.

Multiple linear regression: *Two or more* independent variables affecting *one* dependent variable.

Multivariate linear regression: *Two or more* independent variables affecting *two or more* dependent variable.

Linear Regression in Python:

https://realpython.com/linear-regression-in-python/

Linear Regression in 2 minutes:

https://www.youtube.com/watch?v=CtsRRUddV2s

##Regression in Machine Learning: What it is and examples of different modules:

https://builtin.com/data-science/regression-machine-learning

#Independent Variables vs. Dependent Variables

##independent Variables (predictors):

	* Can the variable(s) be manipulated or controlled?
	* Do(es) the variable(s) come before the other variable(s) chronologically?
	* is/are the variables being used to see the affects on (an)other variable(s)?

Project 1 - Predictive Analysis (Simple Linear Regression)

Developer:* Christopher Valverde

*Course:* Exploration into AI, Machine and Deep Learning

##Program Requirements:
	
	1. Contrast similarities/differences among AI vs Machine-Learning  vs Deep-Learning
	2. Identity correlations
	3. Use Seaborn (data visualization library built on top of matplotlib)
	4. Graph correlations
	5. Use simple linear regression
	6. Create linear model
	7. Plot regression line
	8. Make predictions - using simple linear regression model
	9. plot residuals 

# 1. import pandas and seaborn (built on top of matplotlib)
import pandas as pd
import seaborn as shns # Seaborn provides more visualzation patterns, with less syntax than matplotlib

# Get data - read cleaned .csv file 

# 2. assign cleaned .csv file to "housing_data" variable, then read .csv file to "housing" variable 
# Note: Here is a two-step process for demonstration purposes (two steps is easier than using long paths and/or long file names)
housing_data = "housing_data.csv"
housing = pd.read_csv(housing_data)

# Note: could have also accomplished the process in one step...
# housing = pd.read_csv("housing_data.csv") # must be in directory of ipynb file

# 3. find houses where sqft of living space is less than 8000 sqft and price is greater than $0, and less than $1,000,000
housing = housing.query('sqft_living < 8000 and price < 1000000 and price > 0')

# 4. Add additional attribute to "housing" dataframe called "has_basement"--*if* basement SQFT is greater than 0.
housing['has_basement'] = housing['sqft_basement'].apply(lambda x: True if x > 0 else False)

# 5. drop unconcerened columns 
housing = housing.drop(columns=['date','street','city','statezip','country','sqft_lat','yr_renovated','sqft_basement'])

## Housing dataset

# 6. print dataframe info
housing.info()

# 7. print first 5 records (glimpse new dataframe)
housing.head()

## Identifying correlations using scatterplot

# 8. See if there is any correlation (small) between "price" and living SQFT
sns.relplot(data=housing, x='sqft_living', y='price')

# 9. See if there is any correlation (essentially none) between "price" and year built.
sns.relplot(data=housing, x='yr_built', y='price')

## identifying correlation using grid of scatterplots

# 10. Faster way of displaying relationships between pairs of dataplots

sns.pairplot(data=housing, 
	y_vars=['price','sqft_living','sqft_above']
	x_vars=['price','sqft_living','sqft_above']
	diag_kind='kde')

## Identify correlations with r-values
*i.e, a measure of any linear trend between two variables*

# 11. Display pairwise correlations of *all* columns in the dataframe.
housing.carr().head()

# 12. Display one attribute's correlation ('price') to *all* other columns in dataframe, sorted in descending order by price.
housing.carr()[['price']].sort_values(by="price", ascending=False)

# 13. Visually display correlations using Seaborn's heatmap() function

sns.heatmap(data=housing.carr(), cmap="Reds", vmin=-1.0, vmax=1.0)

# 14. Visually condense the correlations of one variable to other variables.
sns.heatmap(data=housing.corr()[['price']].sort_values(by='price', ascending=False), annot=True, cmap='Blues', cbar=False, fmt=f'.2f')

## Create, validate, and use simple linear regression model

**Steps:**
	1. Split dataset(training vs. test datasets).
	2. *Create* model from "training" dataset.
	3. Validate model using "test" dataset.
	4. if valid predict values.

# 15. import sklearn (aka scikit-learn)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x_train, x_test, y_train, y_test = train_test_split(housing)[['sqft_living']], housing[['price']], test_size=0.33, random_state=42)

linearModel = LinearRegression()
linearModel.fit(x_train, y_train)

linearModel.score(x_test, y_test)

# iv. use model to make predictions on test data
y_predicted = linearModel.predict(x_test)
y_predicted

## Plot predicted data (preparation)

# 16. make dataframe of predicted prices
predicted = pd.DataFrame(y_predicted, columns=['price_predicted'])
predicted

# 17. combine test data and predicted data (reset index for test columns for accurate  comparison between test/predicted values)
combined = predicted.join([x_test.reset_index(drop=True), y_test.reset_index(drop=True)])
combined 

# 18. melt price and price_ppredicted columns into single column 

melted = pd.melt(combined, id_vars=['sqft_living'], value_vars=['price','price_predicted'], var_name='price_type', value_name='price_value')

melted.head

## plot predicted data

# 19. plot test (actual) and training (predicted) data
sns.relplot(data=melted, x='sqft_living', y='price_value', hue='price_type')

## plot linear regression (using simple estimation)

# 20. Similar to plot above; here, linear regression model automatically generated (simple "estimation")

sns.implot(data=housing, x='sqft_living', y='price', cl=None, scatter_kws={'s':5}, line_kws="lw":1, 'color':'red')

# 21. print dataframe summary to confirm attribute names and data types
combined.info()

# 22. plotting regression residuals can also be used to evaluate models, apart from the score() function.
combined['residual'] = combined.price - combined.price_predicted
combined.head()

## Plot residuals using Seaborn 

# 23. Plot residuals using Seaborn relplot(). Here, x-axis is IV and y-axis are the residuals.

g= sns.relplot(data=combined, x='sqft_living', y='residual')

for ax in g.axes.flat:
	ax.axhline(0,ls='--b')

# 24. Similar to relplot (fitted model) vs lmplot (simple estimation), residplot is simple residual estimation

sns.residplot(data=housing, x='sqft_living', y='price', scatter_kws=['s':5])