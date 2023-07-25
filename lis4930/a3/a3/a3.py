#1 import pandas
import pandas as pd 

#2
mortality_data = pd.read_pickle('mortality_cleaned.pkl')

#3
print(mortality_data)

#4
mortality_data.info()

#5
print("Index: ", mortality_data.index)
print("Columns:", mortality_data.columns)
print("Size: ", mortality_data.size)
print("Shape: ", mortality_data.shape)

#6
print(mortality_data.sort_values('DeathRate').head(3))

#7
print(mortality_data.sort_values('DeathRate', ascending=False).head(3))

#8
print(mortality_data.sort_values(['Year','DeathRate']).head(3))

#9
print(mortality_data.sort_values(['DeathRate', 'Year']).head(3))

#10
print(mortality_data.sort_values(['Year','DeathRate'],
ascending=[True,False]).head())

#11
print(mortality_data.sort_values(['DeathRate','Year'],
ascending=[False,True]).head())

#12
print(mortality_data.DeathRate.mean())

#13
print("DeathRate meand: " + str(mortality_data.DeathRate.mean()))

#14
print("DeathRate meand: "
 + str(format(mortality_data.DeathRate.mean(), ".2f")))

 #15
 print(mortality_data[['AgeGroup','DeathRate']].max())

 #16
 print(mortality_data.count())

 #17
 print(mortality_data[['Year']].quantile([.5]))
 print(mortality_data[['Year']].median())

 #18
 print(mortality_data[['Year','DeathRate']].quantile([.5]))
 print(mortality_data[['Year','DeathRate']].median())

 #19
 print(mortality_data.quantile([.1,.9], numeric_only=True))

 #20
 print(mortality_data['DeathRate'].cumsum())

 #21
 print(mortality_data['DeathRate'].head(5))

 #22
 mortality_data['Mean'] = mortality_data.DeathRate.mean()
 mortality_data['MeanCentered'] = \
 mortality_data.DeathRate - mortality_data.DeathRate.mean()

 #23
 print(mortality_data)

 #24
 mortality_data.AgeGroup.replace(
    {'1-4 Years':'01-04 Years','5-9 Years':'05-09 Years'},
    inplace=True
 )
 
 #25
 mortality_data.to_pickle('mortality_prepped.pkl')

 #26
 mortality_data = pd.read_pickle('mortality_prepped.pkl')
 mortality_data.head()

 #27
 mortality_data.head(2)

 #28
 mortality_data = mortality_data.set_index('Year')
 mortality_data.head(2)

 #29
 mortality_data.reset_index(inplace=True)
 mortality_data.head(2)

 #30
 mortality_data = mortality_data.set_index(
    ['Year', 'AgeGroup'], verify_integrity=True)
    mortality_data.head(2)
 
 #31
 mortality_data.reset_index(inplace=True)
 mortality_data.head(2)

 #32
 mortality_wide = mortality_data.pivot(index="Year",columns="AgeGroup")
 mortality_wide.head(3)

 #33
 mortality_wide = mortality_data.pivot(index="Year",columns="AgeGroup", values="DeathRate")
 mortality_wide.head(3)

 #34
 mortality_wide.to_excel('mortality_wide.xlsx')

 #35
 mortality_wide = pd.read_excel('mortality_wide.xlsx')
 print(mortality_wide.head(4))

 #36
 mortality_wide.to_pickle('mortality_wide.pkl')

 #37
 mortality_wide = pd.read_pickle('mortality_wide.pkl')
 mortality_wide.head

 #38
 mortality_long = mortality_wide.melt(
    id_vars='Year',
    value_vars= '01-04 Years', '05-09 Years',
    var_name='AgeGroup',
    value_name='DeathRate')
    mortality_long.head(4)
 
 #39
 with pd.option_context(
    'display.max_rows', 6,
    'display.max_columns', None):
    print(mortality_long)
 
#40
mortality_data.head()

#41
mortality_data.groupby('AgeGroup').mean()

#42
mortality_data.groupby('Year').median(numeric_only=True).head(4)

#43
mortality_data.groupby(['Year', 'AgeGroup']).count().head()

#44
mortality_data.groupby('AgeGroup')['DeathRate'].describe()

#45
mortality_data.groupby('AgeGroup').agg(['mean','median'])

#46
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean','median','std','nunique'])

#47
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean','median','std','min','max','var','nunique'])

#48
mortality_data.pivot(index='Year',columns='AgeGroup')['DeathRate'].plot()

#49
mortality_wide = mortality_wide.set_index('Year')

mortality_wide.to_pickle('mortality_wide.pkl')
mortality_wide = pd.read_pickle('mortality_wide.pkl')
mortality_wide.head()

#50
mortality_wide.plot.box()

#51
mortality_wide.plot(xlabel='Year', ylabel='Deaths per 100,000', title='DeathRate by AgeGroup')

#52
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean', 'median', 'std']).plot.bar(rot=45)

#53
mortality_data.groupby('AgeGroup')['DeathRate'].agg(['mean', 'median', 'std']).plot.barh()

#54
mortality_data.query('Year in (1900, 1925, 1950, 1975, 2000)').groupby('Year').DeathRate.sum().plot.pie()

#55
mortality_wide.query('Year in (1900, 1925, 1950, 1975, 200)').plot.barh(
    title=['Child Mortality: 01-04', 'Child Mortality: 05-09',
    'Child Mortality: 10-14', 'Child Mortality: 15-19'],
    sharey=True, legend=False, subplots=True, layout=(2,2), figsize=(8,5))


#56
mortality_data.query('AgeGroup == "01-04 Years"').plot.scatter(x='Year', y='DeathRate', c='Blue')

