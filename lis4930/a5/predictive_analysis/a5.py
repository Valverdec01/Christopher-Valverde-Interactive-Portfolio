# Regression Analysis

### *Goal*: Find the best fitting line which can accurately predict the output.

*Fundamentals:*

Dependant variables (DVs) (*output on y-axis): always variables being studied-- that is, whose variation(s) is/aare being modified somehow!
Independent variables (IVs) (*input on x-axis*): always variables being manipulated, to study and compare effects on DV(s).

*Note:* the designations independent and dependent variables are used to not imply "cause and effect" (as do "predictor" or "explanatory" terms).

*Note:* Based on the number of input and output variable, linear regression has three types:

    1. Simple linear regression (1 DV/1 IV)
    2. Multiple linear regression (1 DV/2 or more IVs)
    3. Multivariate linear regression (2 or more DVs/2 or more IVs)

*Simple linear regression:* Only *one* independent variable affecting *one* dependent variable.

*Multiple linear regression: Two or more* independent variable affecting *one* dependent variable.

*Multivariate linear regression: Two or more* independent variables affecting *two or more* dependent variable

# Supervised vs. Unsupervised Learning

    * Supervised learning: prior knowledge of what output values for samples should be.
    * Unsupervised learning: does not have labeled outputs. Goal is to infer natural structure present within a set of data points

# Assignment 5 - Predictive Analysis (Multiple Linear Regression)

*Developer:* Christopher Valverde

*Course:* Exploration into AI, Machine and Deep Learning

*Program Requirements:

	1. Contrast Similarities/differences among AI vs. Machine-Learning vs. Deep-Learning
	2. Identify correlations
	3. Use Seaborn (data visualization library built on top of matplotlib)
	4. Graph correlations
	5. Use simple linear regression
	6. Create linear model
	7. Plot regression line
	8. Make predictions - using simple linear regression model
	9. plot residuals

# Import libraries

# 1. necesary libraries:
# pandas and numpy libraries to perform mathematical functions
# matplotlib and seaborn libraries to visualize data
# linearRegression: models relationship between DVs, and given set of IVs
# train_test_split: splits datasets into training and test datasets

# Note: seaborn provides more visualization patterns, with less syntax than matplotlib

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Get data

# 2. assign cleaned .csv file to "fish" variable
# Read given CSV file, and view some sample records
fish = pd.read_csv('fish.csv')

# display first and last 5 records
fish

# fish.head() # display first 5 records 
# fish.tail() # dsiplay last 5 records

# Clean Data

# 3. Rename cols to differentiate "length" properties, then display 1st 5 records
fish.rename(columns=("Length1":"VerticalLength",
					 "Length2":"DiagonalLength",
					 "Length3":"CrossLength"), implace=True)
fish.head()

# Analyze dataset

# 4. print number of rows and columns
fish.shape

# 5. print dataframe info (Note: also, indicates null values, which, if present, would need to be remidied)

fish.info()

# 6. print dataframe statistics summary
fish_describe = fish.describe()

# format entire dataframe to two decimal places
pd.option.display.float_format = "{:,.2f}".format

print(fish_describe)

# Identify correlations

# 7. Display pairwise correlations of *all* columns in datframe. 
fish.corr(numeric_only = True).head()

# 8. Visualize data for correlations using pairplot(). y=DV(s), x=IV(s)
# pairplot(): Plot pairwise relationships in dataset.

sns.pairplot(fish, x_vars=['Height','Width','VerticalLength'], y_vars='Weight', height=4, aspect=1, kind='scatter'
plt.show()

# Custom visualizations
# Color palettes:

# display all colors from current default color cycle
sns.color_palette()

# 10. display color pallete refrenced by name
sns.color_palette("pastel")

# 11. display color values as hex codes:
print(sns.color_palette("pastel").as_hex())

# 12. Custom plotting
sns.pairplot(fish, hue="Species", diag_kind="hist", markers=["o", "s", "D", "*", "<", "p", "v"], palette = "husl")

# 13. Display one attribute's correlation ("Weight") to all other columns in dataframe, sorted in descending order by height.

fish.corr(numeric_only = True)[['Weight']].sort_values(by='Weight', ascending=False)

# 14. Visually display correlations using Seaborn's heatmap() function.
ax=sns.heatmap(data=fish.corr(numeric_only = True), annot=True, cmap='viridis')
ax.tick_params(axis='both', rotation=45, labelsize=8, labelcolor='blue', color='green')#customize ticks and labels

# 15. Visually condense correlations of one variable to other variables.
sns.heatmap(data=fish.corr(numeric_only = True)[['Weight']].sort_values(by='Weight', ascending=False), annot=True, cmap="PuBuGn", fmt=f'.2f')

# Note: "annot" property set to "True" so that r-values are displayed in each cell.
# Here, display color bar.

# Create multiple regression model

## Multiple Regression Steps

	1. identify x(IVs) and y (DV): x=Height,Width,VerticalLength, y=Weight
	2. Creaete Train and Test datasets
	3. Train model
	4. Evaluate model

# 16. Focus on one species: Bream
bream = fish.query('Species == "Bream')

# 17. Identify x (IVs) and y (DV)
x = bream[['Height','Width','VerticalLength']]
y = bream[['Weigth']]

# Note: Combination of 'Height', 'Width','VerticalLength' returns a higher correlation score than individual attributes by themselves (below)
# compare multiple regression model "x" above, againt simple regression model, that is, using each of the following attributes individually:

# x = bream[['VerticalLength']]
# x = bream[['Width']]
# x = bream[['Height']]

# *BE SURE* when comparing "x" values, only one should be uncommented!
# see #22 for model.score results!

# 18. create train and test datasets
# a. split variables into training and testing sets
# b. build model using training set, then run model on testing set

# Note: Training dataset used to "fit" the model, and test dataset is used to *evaluate* model 
# Training data is the biggest subset of original dataset--used to train or fit the model
# test dataset is another (smaller) subseet of *original* data, independent of training dataset--validates model's accuracy

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.75, test_size = 0.25, random_state = 100)

# 19. Display x training dataset (IVs)

x_train 

# 20. Display y training dataset (DV)
y_train/454

# Fitting model: Find best fitting line -- to accurately predict output
# 21. fit regression line to plot
model = linearRegression().fit(x_train, y_train)

# 22. display R2 correlation values--validates model through correlation score
# score() function: accepts test dataset and returns R2 correlation value--i.e., percent of change in DV attributed to IV(s)
# higher score indicates better fit!
model.score(x_test, y_test)

# 23. predict weight and display predicted values based upon IVs
# predict() method accepts x values from test dataset and returns predicted y values.
# predicts labels of data values, based on trained model
y_predicted = model.predict(x_test)

# create "predicted" DataFrame with "PredictedWeight" column using y_predicted values
# Note: DataFrames are two-dimensional data structures, whic include indexes along with their associated values.
predicted = pd.DataFrame(y_predicted, columns = ["PredictedWeight"])

# display data structure type and "predicted" weight DataFrame values
# type(predicted) # pandas.core.frame.DataFrame
predicted

# 24. display data structure type and values
# type(x_test) # pandas.core.frame.DataFrame
x_test #IVs

# 25. display data structure type and values
# type(y_test) # pandas.core.frame.DataFrame
y_test #DV

# 26. Join and display all columns, including PredictedWeight column
# pandas.Dataframe.join(): join multiple DataFrame objects by index at once by passing a list
# Note: "drop" parameter removes old index values being added as a column
final = predicted.join([x_test.reset_index(drop=True),
						y_test.reset_index(drop=True)])

# reset_index: Resets index values back to defualt values (0,1,2, etc.)
# display PredictedWeight and actual weight (DVs), with IVs 
# Note: Very close predictions!
final

# Residuals

	* R2 value returned by score() method for test dataset provides good indication of regression model validity
	* Also, plotting residuals helps to evaluate models.

	# 27. calculate and display residual values
	# Note: "Residuals" are simply differences between DV test values and DV predicted values.
	# Residual = Actual - predicted
	# positive values indicate prediction is too low, negative values indicate prediction too high

	fianl['Residual'] = final.Weight - final.PredictionWeight

	final 

# 28. plot residuals
# KDE (Kernel Density Estimate) plot: Estimates data distribution
# Visual representation of underlying distribution of data--helps to understand shape and spread of data, and indentify unusual outliers.
# Produces small continous curve (also called kernel) for every individual data paint along axis.
# Scale of "density" axis depends on data values

# Note: here, most residuals w/in +100 and -100 of zero, and closely centered on zero (0)--indicating a decent model!
# Plot reveals that outliers affecting regression are on negative side of curve.
sns.kdeplot(data=final, x="Residual")

# Note: "Ideal" KDE plot displays a bell-shaped curve and centered over, on the X-axis, with most of the datapoints closed to zero (0).
