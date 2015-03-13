import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

loandata = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loandata.dropna(inplace = True)
# clean data

#loandata['FICO.Score'] = loandata['FICO.Range'].map(lambda x: (x.split('-')))
#loandata['FICO.Score'] = loandata['FICO.Score'].map(lambda x: int(x[1]) -2)

loandata['FICO.Score'] = [x.split('-') for x in loandata['FICO.Range']]
loandata['FICO.Score'] = [int(x[1]) - 2 for x in loandata['FICO.Score']]


#clean interest rate to decimal notation
loandata['Interest.Rate'] = loandata['Interest.Rate'].map(lambda x: round(float(x.rstrip('%'))/100,4))

# clean loan length
loandata['Loan.Length'] = loandata['Loan.Length'].map(lambda x: int(x.rstrip('months')))

# clean employment length
loandata['Employment.Length'] = loandata['Employment.Length'].map(lambda x: x.lstrip('<').lstrip())
loandata['Employment.Length'] = loandata['Employment.Length'].map(lambda x: x.rstrip('years').rstrip())
loandata['Employment.Length'] = loandata['Employment.Length'].map(lambda x: (x.rstrip('+').rstrip()))
loandata['Employment.Length'] = loandata['Employment.Length'].map(lambda x: x.replace('n/','1'))
loandata['Employment.Length'] = loandata['Employment.Length'].map(lambda x: int(x))
#loandata['Employment.Length'] = loandata['Employment.Length'].map(lambda x: int(x.rstrip('year')))

#plt.hist(loandata['FICO.Score'].values)
#pd.scatter_matrix(loandata, alpha = 0.05, figsize = (22,22), diagonal = 'sde')


intrate = loandata['Interest.Rate'].values
loanamt = loandata['Amount.Requested'].values
fico = loandata['FICO.Score'].values


y = np.matrix(intrate).transpose()

x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()


x = np.column_stack([x1,x2])

X = sm.add_constant(x)

print X

model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R Squared: ', f.rsquared
