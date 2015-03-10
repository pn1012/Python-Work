import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data = pd.read_csv("https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv")

data.dropna(inplace = True)

data.boxplot(column = 'Amount.Requested')
plt.savefig('/Users/PatrickCoryNichols/Desktop/Box_Amount_Requested.jpg')
data.hist(column = 'Amount.Requested')
plt.savefig('/Users/PatrickCoryNichols/Desktop/Hist_Amount_Requested.jpg')

plt.figure()
graph = stats.probplot(data['Amount.Requested'], dist = 'norm', plot = plt)
plt.savefig('/Users/PatrickCoryNichols/Desktop/QQ_Norm_Amount_Requested.jpg')