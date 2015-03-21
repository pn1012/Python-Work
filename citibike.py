import pandas as pd
import pandas.io.json as pdj
import json
import os
import requests 
import sqlite3 as lite


con = lite.connect(database = '/Users/PatrickCoryNichols/citi_bike.db')
cur = con.cursor()

# get connection to json
r = requests.get('http://www.citibikenyc.com/stations/json')

# normalize json file
df = pdj.json_normalize(r.json()['stationBeanList'])

# add execution time
df['time'] = r.json()['executionTime']
df['total_usage'] = 1 - (df['availableBikes']/df['totalDocks'])




#cur.execute('DROP TABLE IF EXISTS citibike_reference')


"""
query_ref = '''CREATE TABLE citibike_reference (
                id INT,
                time DATETIME,
                totalDocks INT,
                availableDocks INT,
                availableBikes INT,
                city TEXT,
                altitude INT,
                stAddress2 TEXT,
                longitude NUMERIC,
                postalCode TEXT,
                testStation TEXT,
                stAddress1 TEXT,
                stationName TEXT,
                landMark TEXT,
                latitude NUMERIC,
                location TEXT,
                total_usage NUMERIC
                )'''
                
             
with con:
   cur.execute(query_ref)
"""

dfload = df[['id','time','totalDocks','availableDocks','availableBikes','city',
             'altitude','stAddress2','longitude','postalCode',
             'testStation','stAddress1','stationName',
             'landMark','latitude','location','total_usage']]
           
dfload.to_sql('citibike_reference',con, flavor = 'sqlite', if_exists = 'append', index = False)





