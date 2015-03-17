import pandas as pd
import statsmodels.api as sm
import math



# import data
df = pd.read_csv('/Users/PatrickCoryNichols/Desktop/LoanStats3c.csv', skiprows = 1)

#drop N/As
df.dropna(inplace = True)
# convert loan amount to int
df['loan_amnt'] = df['loan_amnt'].map(lambda x: int(x))
# strip and convert months from term
df['term'] = df['term'].map(lambda x: int(x.rstrip('months')))
# convert int rate to decimal notation, float
df['int_rate'] = df['int_rate'].map(lambda x: float(x.rstrip('%'))/100)
# set up home ownership dummy category (or use C() as part of statsmodels???)
df['home_ownership_cat'] = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x =='RENT' else 1 if x =='OTHER' else 0 for x in df['home_ownership']]
# set up grade dummy category (or use C() as part of statsmodels???)
df['grade_cat'] = [5 if x == 'A' else 4 if x == 'B' else 3 if x == 'C' else 2 if x == 'D' else 1 if x == 'E' else 0 for x in df['grade']]
# convert annual income to default log to test
df['annual_inc'] = df['annual_inc'].map(lambda x: math.log(x))

#chart int rate to check for normal dist
#plt.hist(df['int_rate'].values, histtype = 'bar')
#plt.figure()
#stats.probplot(df['int_rate'].values, dist= 'norm', plot = plt)

# quick reference for column names
columns = list(df)



# begin model set up for multivariate linear regression using sm.formula -- this is a very simple way
model = sm.formula.ols(formula ="int_rate ~ annual_inc + home_ownership_cat", data = df)
# fit model
results = model.fit()
print'\tRESULTS OF MODEL: Y: INTEREST RATE X: ANNUAL INCOME, HOME OWNERSHIP'
print
print results.summary()

# for Roy: this model has a poor RSQ and poor F stat, home ownership variables are not significant and residuals are high - not a good model, right? :)

print
print
# begin model set up for multivariate linear regression using sm.formula -- this is a very simple way
model = sm.formula.ols(formula ="int_rate ~ annual_inc + C(home_ownership)", data = df)
# fit model
results = model.fit()
print'\tRESULTS OF MODEL 2: Y: INTEREST RATE X: ANNUAL INCOME, HOME OWNERSHIP'
print
print results.summary()
# in this case, the built in C() function in statsmodels splits the categories out y = b0 + b1x1 + b1x2 + b2x2, how would I set this function up?

print
print
# begin model set up for multivariate linear regression using sm.formula -- this is a very simple way
model = sm.formula.ols(formula ="int_rate ~ annual_inc * C(home_ownership)", data = df)
# fit model
results = model.fit()
print'\tRESULTS OF MODEL 3: Y: INTEREST RATE X: ANNUAL INCOME, HOME OWNERSHIP'
print
print results.summary()
# how does this interaction work? our intercept starts almost four points higher than model two and the variables now work down to an interest
# rate for home ownership, while te interactions between annual income and home ownership are now part of the model, what
# advantage does this serve over model two or even one? 