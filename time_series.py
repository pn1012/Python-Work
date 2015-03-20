
import pandas as pd
import statsmodels as stats


df = pd.read_csv('/Users/PatrickCoryNichols/Desktop/LoanStats3c.csv', skiprows=1, parse_dates = ['issue_d'], 
                  index_col = ['issue_d'])

#pull out loan amounts, loan counts, drop nas or unlreated records
df = df['loan_amnt'].dropna()
df = df.resample('M', how = ['count'], kind = 'period')

df['count'].plot()
stats.api.graphics.tsa.plot_acf(df['count'])
stats.api.graphics.tsa.plot_pacf(df['count'])
