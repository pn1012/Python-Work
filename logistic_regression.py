# logistic Regression Example
import pandas as pd
import statsmodels.api as sm
import math


loandata = pd.read_csv('/Users/PatrickCoryNichols/Desktop/loandata_cleaned.csv')

loandata['IR_TF'] = [True if x < .12 else False for x in loandata['Interest.Rate']] 

loandata['Constant'] = 1

ind_vars = ['Constant','Amount.Requested','FICO.Score']

logit = sm.Logit(loandata['IR_TF'],loandata[ind_vars])

result = logit.fit()

coeff = result.params[:]

print coeff



def decision_maker(amt, score,coeff):
    prob = 1 - 1/(1+math.exp(coeff[0]+coeff[1]*amt+coeff[2]*score))
    if prob > 0.5:
        p = 'Accept'
    else:
        p = 'Reject'
    return prob, p
 
print decision_maker(10000,720,coeff)
