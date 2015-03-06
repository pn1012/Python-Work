import pandas as pd
import sqlite3 as lite

month = str(input("What month?")

months = ['January','February','March','April','May','June','July','August','September','October','November','December']


if month in months:

    cities = (("San Francisco","CA"),("Austin", "TX"),("Dallas","TX"),("New York City","NY"),("Los Angeles","CA"))
    weather = (("San Francisco","January", "July",72),("Austin", "December","August",81),("Dallas", "December","August",79),
           ("New York City","January","May",68),("Los Angeles","December","July",71))
#connect to the database

    con = lite.connect('/users/patrickcorynichols/getting_started.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS cities")
        cur.execute("DROP TABLE IF EXISTS weather")
        cur.execute("CREATE TABLE cities(name text, state text)")
        cur.execute("CREATE TABLE weather(city text, cold_month text, hot_month text, avg_temp integer)")
        cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
        cur.executemany("INSERT INTO weather VALUES(?,?,?,?)",weather)
        data = cur.execute("SELECT name, state, cold_month, hot_month, avg_temp FROM cities LEFT JOIN weather ON name = city where \
        hot_month = " + "'" + str(month) + "'" +" ORDER BY avg_temp DESC").fetchall()
        columns = [desc[0] for desc in cur.description]
        dframe = pd.DataFrame(data, columns = columns)


    print "The cities that are warmest in July are:", 

    for name in dframe['name']:
        print name,',',

else: print 'Not a valid month'

#print 'The cities that are warmest in July are:', 
#   dframe['name'][0]
