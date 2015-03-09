import pandas as pd
from scipy import stats

""" measures of central tendency """

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''




# split data into a mega list
data = (data.split('\n'))


# split mega list to minor lists to identify lines
data = [i.split(', ') for i in data]



cols = data[0]

rows_sel = data[1::]


df = pd.DataFrame(rows_sel, columns = cols)

df['Alcohol'] = df['Alcohol'].astype(float)
df ['Tobacco'] = df['Tobacco'].astype(float)

#print(df['Alcohol')]
print 'The median of Alcohol in the regional alcohol and tobacco consumption data set is {0}'.format(df['Alcohol'].median())
print 'The mean of Alcohol in the regional alcohol and tobacco consumption data set is {0}'.format(round(df['Alcohol'].mean(),3))
print 'The mode of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(stats.mode(df['Alcohol']))
print 'The range of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(df['Alcohol'].max() - df['Alcohol'].min())
print 'The variance of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(round(df['Alcohol'].var(),3))
print 'The sd of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(round(df['Alcohol'].std(),3))


print ''
print 'The median of Tobacco in the regional alcohol and tobacco consumption data set is {0}'.format(df['Tobacco'].median())
print 'The mean of Tobacco in the regional alcohol and tobacco consumption data set is {0}'.format(round(df['Tobacco'].mean(),2))
print 'The mode of Tobacco in the regional alcohol and tobacco comsumption data set is {0}'.format(stats.mode(df['Tobacco']))
print 'The range of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(df['Tobacco'].max() - df['Tobacco'].min())
print 'The variance of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(round(df['Tobacco'].var(),3))
print 'The sd of Alcohol in the regional alcohol and tobacco comsumption data set is {0}'.format(round(df['Tobacco'].std(),3))