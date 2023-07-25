# Regression Analysis

## What is Regression analysis?

	1. Equation predicts **"unknown values"** (i.e dependent variables) based upon one or more known values (i.e, independent variable(s)).
	2. Dependent variables: response, outcome/output, or target variables (respond to changes in (an)other variables(s)).
	3. Independent variables: predicator, input, regressor, or explanatory variables (predict/explain changed values of dependent variables)
	4. Goal: find the best fitting line which can accurately predict the output.

Dependent variables (output on y-axis) are alwayas the one being studied-- that is, whose variation(s) is/are being modified somehow!

Independent variables (input on x-axis) are always the ones being manipulated, to study and compare the effects on the dependent variables(s).

**Note:** The designations independent and dependent variables are used to not imply "cause and effect" (as do "predictor" or "explanatory" terms)

**Note:** Based on the number of input and output variables, linear regression has three types:
	
	1. Simple linear regression (1 DV/1 IV)
	2. Multiple linear regression (1 DV/2 or more IVs)
	3. Multivariate linear regression (2 or more DVs/2 or more IVs)

Simple linear regression: Only **one** independent variable affecting **one** dependent variable.

Multiple linear regression: **Two or more** independent variables affecting **one** dependent variable.

Multivariate linear regression: **Two or more** independent variables affecting **two or more** dependent variable.

# Independent Variables vs. Dependent Variables

## Independent Variables (predictors):

	* Can the variable(s) be manipulated or controlled?
	* Do(es) the variable(s) come before the other variable(s) chronologically?
	* is/are the variables being used to see the affects on (an)other variable(s)?

## Dependent variables (outcomes):
	
	* is/are the varaible(s) being used as (a) measured outcomes(s)?
	* do(es) the variables(s) depend upon an(other) variables(s)?
	* is/are this/these variable(s) measaured after (an)other variable(s) is/are modified?

# Assignment 4 - Predictive Analysis (Simple Linear Regression)


**Developer:** Christopher Valverde

**Course:** Exploration into AI, Machine and Deep Learning

## Program Requirements:
	
	1. Contrast similarities/differences among AI vs Machine-Learning vs Deep-Learning
	2. Identity correlations
	3. Use Seaborn (data visualization library built on top of matplotlib)
	4. Graph correlations
	5. Use simple linear regression
	6. Create linear model
	7. Plot regression line
	8. Make predictions - using simple linear regression model
	9. plot residuals 

# 1. Import pandas and numpy libraries to perform mathematical functions

import numpy as rp 
import pandas as pd 

# Note: The following *can* be used to supress warnings (though, best to fix them!).
# import warnings
# warnings.filterwarnings("ignore")

# Get data - read cleaned .csv file

# 2. assign cleaned .csv file to "advertising_data" variable, then read .csv file to "housing" variable
# Read the givn CSV file, and view some sample records
advertising_data = pd.read_csv("my_company_data.csv")

# display first and last 5 records
advertising_data

# Advertising dataset

# 3. print number of rows and columns
advertising_data.shape

# 4. print dataframe info (Note: also, indicates null values, which, if present, would need to be remedied.)
advertising_data.info()

# 5. print dataframe statistics summary
advertising_data.describe()

# 6. Display pairwise correlations of *all* columns in the dataframe.
advertising_data.corr().head()

# 7. import matplotlib and seaborn libraries to visualize data
# Note: # Seaborn probides more visualization patterns, with less syntax than matplotlib

import matplotlib.pyplot as plt
import seaborn as sns

# 8. visualize data for correlations using pairplot().
sns.pairplot(advertising_data, x_vars=['TV', 'Radio','Newspaper'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()

# 9. Display one attribute's correlation ("price") to *all* other columns in dataframe, sorted in descending order by price.
advertising_data.corr()[['Sales']].sort_values(by='Sales', ascending=False)

# 10. Focus on correlation bbetween "TV" (ads) and "Sales."
sns.relplot(data=advertising_data, x='TV', y='Sales')

# 11. Visually display correlations using Seaborn's heatmap() function.
sns.heatmap(advertising_data.corr(), cmap="YlGnBu", annot = True)
plt.show()

# 12. Visually condense correlations of one variable to other variables
sns.heatmap(data=advertising_data.corr()[['Sales']].sort_values(by='Sales', ascending=False), annot=True, cmap='YlGnBu', cbar=False, fmt=f'.2f')

# Simple Linear Regression Steps

	1. identify x(IV) and y(DV):x=TV, y=Sales
	2. Create Train and Test datasets
	3. Train model
	4. Evaluate model

# 13. Identify x (IV) and y (DV)
x = advertising_data["TV"]
y = advertising_data["Sales"]

# 14. Create train and test datasets
# a. split variables into training and testing sets
# b. build model using training set, then run modl on testing set

# split variables into train and test datasets into 7:3 ratio, respectively, by importing train_test_split 
# Translation: 70% of observations for training, and remaining 30% for testing
# train_test_split():

# random_state: controls randomization during splitting (deefualt value None).
# random_state value not important -- can be any non-negative integer.
# Generally, *only* used to make tests reproducible--provides fixed seed value.

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.7, test_size= 0.3, random_state = 100)

# Review train datasets after splitting

# 15. Display x training dataset
x_train

# 16. Display y training dataset
y_train

### **Add column to perform regression fit properly for simple linear regression:**

# Prepare Model
 
# 18. add additional column to train and test datasets
# By "reshaping" we can add or remove dimensions.

# reshape() concept: First, raveling array (using given index order),
# then inseerting/deleting elements from raveled array into new array, using same index order for raveling
x_train = x_train.values.reshape(-1,1)
x_test = x_test.values.reshape(-1,1)

# 19. display shape for x trin and test data, *after* adding column (Now, 2 dimension array.)
print(x_train.shape)
print(x_test.shape)

# Fitting model: Find best fitting line -- to accurately predict output 
# 20. fit regression line to plot
from sklearn.linear_model import  LinearRegression

# Note: Can create linear regression model object (instantiation) and fit in two steps, or at the same time
# 1. Instantiate linear regression model object 
# ln = linearRegression()

# 2. fit model using fit() method
# ln.fit(x_train, y_train)

# or...both at same time...
ln = LinearRegression().fit(x_train, y_train)

# Intercept and Slope - Why?

# print model coefficients

# 21. print intercept value (aka the "constant") Represents mean value of DV when all of IV(s) in model are equal to zero.
print("Intercept :",ln.intercept_)

# 22. print slope value: Indicates how much DV expected to change, as IV(s) increase(s)/decrease(s).
print('Slope :',lm.coef_)

# 23. simple linear regression formula from above values
# Y = mX + b
# Y = DV, X = IV, m = estimated slope, b = estimated intercepet 

# Note : parentheses not needed.
# Sales = (0.054 = IV) + 6.948

# r2 values - how well regression line approximates actual data

# 24. predict y_value
y_train_predict = ln.predict(x_train)
y_test_predict = ln.predict(x_test)

from sklearn.metrics import r2_score

# 25. print and compare r2 values of both train and test data
print(r2_score(y_train,y_train_predict))
print(r2_score(y_test,y_test_predict))

# Note (r2): Statistical measure of how well regression line approximates actual data
# Represents the proportion of varianc for a DV that's explained by IV(s) in a regression model 

# Bottom-Line: r2 values on test data within 5% of r2 values on training data. model looks good!

# Plot Linear Regression (using simple estimation)

# 26. Plot data and linear regression model fit.
# Note: Goal of seaborn is to help find and emphasize patterns through quick and easy visualizations.
# There are "many" ways to find relationships and determine patterns. Provided here are "some" ways of doing so.

sns.regplot(data=advertising_data, x='TV', y='Sales', ci=95, scatter_kws={'s':5}, line_kws={"lw":1, 'color':'orange'})

# Plot residuals using Seaborn

# 27. Residual plot: used to plot residul values after plotting linear regression model.
# What is a residual plot? Helps to identify regression model fit

# Lowess (aka "loess") line stands for "locally weighted scatterplot smoothing."
# Creates smooth line to help better understand relationship between variables and trends

sns.residplot(data=advertising_data, x='TV', y='Sales', scatter_kws={'s':5}, lowess=True, line_kws={"color":'green'})

