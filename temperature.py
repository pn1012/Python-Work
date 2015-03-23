# this script reads data from darksky api for weather forecasts and performs basic data analysis
# and distribution fits. Data is read over the past thirty days for five cities

import datetime as dt

import pandas as pd
import requests as rq
import pandas.io.json as pj
import sqlite3 as lite
import matplotlib.pyplot as plt
import scipy.stats as stats

darksky = '6d50b466512e0593d16e495bf0db72fc'
paths = '/Users/patrickcorynichols/'
dbpath = paths.join([ '','weather.db'])
con = lite.connect(dbpath)
cur = con.cursor()


cities = { "Atlanta": '33.762909,-84.422675',
            "Austin": '30.303936,-97.754355',
            "Boston": '42.331960,-71.020173',
            "Chicago": '41.837551,-87.681844',
            "Cleveland": '41.478462,-81.679435'
         }

"""
query = 'CREATE TABLE temps_max (period DATETIME, city TEXT, temperatureMax NUMERIC)'
con.execute(query)
"""      

# iterate through dict and grab data from API feed for last 30 days for five cities based on L&L
for k,v in cities.iteritems():
    counter = 30
    for i in range(30):
        try:
            start = dt.datetime.now() - dt.timedelta(days=counter)
            start = str(start.replace(microsecond=0)).replace(" ",'T') #insert local timezone to api call
            call = 'https://api.forecast.io/forecast/'+darksky+'/'+ str(v) + ',' + str(start) # set up call
            data = rq.get(call) #get data
            df = pj.json_normalize(data.json()['daily']['data']) # pull into dataframe
            start = [int(x) for x in start[0:10].split('-')] # convert date
            start = dt.date(start[0],start[1],start[2]) # convert date redux
            df['period'] = start # add period/date
            df['city'] = k # add city
            df2 = df.groupby(['period', 'city'], as_index = False)['temperatureMax'].sum() # transform
            df2.to_sql('temps_max',con, flavor = 'sqlite', if_exists = 'append', index = False) # load to SQLite
            counter -= 1 # reduce sentry by 1
        except: 'fail blog -- too lazy to catch errors -- just investigate the shit and shut up'

# begin data analysis
df2 = pd.read_sql('SELECT * FROM temps_max',con)

# cities and range table - what city had the largest weather range over the last month?
print 'Cities\t\t\tRange'
for k in cities.keys():
    print k,'  \t\t',df2[df2['city'] == str(k)]['temperatureMax'].max() - \
                     df2[df2['city'] == str(k)]['temperatureMax'].min()

#daily weather shift patterns, bring into new dataframe, discard original record as it 
#influences data incorrectly, show by city, daily delta mean
df3 = df2
df3['daily_delta'] = abs(df3['temperatureMax'] - df3['temperatureMax'].shift())
df3 = df3.drop(df3['daily_delta'] < 0)
df4 = df3
df3 = df3.groupby('city', as_index = False)['daily_delta'].mean().sort('daily_delta', \
                                                                        ascending = False)
print df3



# plot basic line chart of Austin
df2[df2['city'] == 'Austin'].plot(x ='period', y='temperatureMax')
plt.figure()
df2[df2['city'] == 'Austin'].plot(x ='period', y='daily_delta')

# does univariate analysis show normal distribution?
plt.hist(df2['temperatureMax'])
plt.figure()
stats.probplot(df2['temperatureMax'], dist = 'norm', plot = plt)
# does not show norm dist, data set too small to analyze appropriately
# check chi squared value to see if data fits chi sqr distribution
chi, p = stats.chisquare(df2['temperatureMax'])
print chi, p

# data set does not look stationary, weather forecasts over time and seasons would need to be 
# differenced