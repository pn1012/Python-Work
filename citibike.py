import pandas as pd
import pandas.io.json as pdj
import json
import requests 
import sqlite3 as lite
import time
import matplotlib.pyplot as plt

con = lite.connect(database = '/Users/PatrickCoryNichols/citi_bike.db')
cur = con.cursor()

"""

for i in range(2):
     # get connection to json
    r = requests.get('http://www.citibikenyc.com/stations/json')

    # normalize json file into pandas dataframe
    df = pdj.json_normalize(r.json()['stationBeanList'])

    # add execution time to dataframe, add high level utilization metric to dataframe
    df['time'] = r.json()['executionTime']
    df['total_usage'] = 1 - (df['availableBikes']/df['totalDocks'])
    
    # establish load columns to SQLite
    dfload = df[['id','time','totalDocks','availableDocks','availableBikes','city',
                 'altitude','stAddress2','longitude','postalCode',
                 'testStation','stAddress1','stationName',
                 'landMark','latitude','location','total_usage']]
               
    dfload.to_sql('citibike_reference',con, flavor = 'sqlite', if_exists = 'append', index = False)

    time.sleep(60)

con.close()
"""

df = pd.read_sql('SELECT * FROM citibike_reference', con)
df = df.sort(columns = ['id', 'time'])

df['activity'] = abs(df.availableBikes - df.availableBikes.shift()).fillna(0)
df['tracker'] = (df.id - df.id.shift())
df = df.drop(df['tracker'] != 0)
df = df.drop('tracker',1)
df['time'] = pd.to_datetime(df['time'])

#group by to get results in different dataframe
df2 = df.groupby(by = ['id'], as_index = False)['activity'].sum()
df2 = df2.sort('activity', ascending=False)
df3 = df.groupby(by = ['id','time'], as_index = False)['activity'].sum()

print 'The station with the highest amount of activity is: ', df2['id'].values[0], 'with an activity level of: ', df2['activity'].values[0]

# plot top 5
df2[0:5].plot(x = 'id', y='activity', kind = 'bar')
plt.figure()

# plot line of top station over time
df3[df3['id']== 490].plot(x='time', y ='activity', ylim = (0, 7))
