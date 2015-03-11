import pandas as pd
import collections as col
import scipy


data = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

data.dropna(inplace = True)

freq = col.Counter(data['Open.CREDIT.Lines'])

sumfreq = sum(freq.values())


print 'n degrees of freedom: ' + str(sumfreq - 1)

chi, p = scipy.stats.chisquare(freq.values())

print chi, p 
