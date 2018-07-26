import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import csv

###Since Yahoo pulled their API the DataReader will not longer work. Can still work with a .csv###

#GFC Peak to trough dates#
##start = dt.datetime(2007, 10, 9)
##end = dt.datetime(2009, 3, 9)

#Custom#
start = dt.datetime(2017, 1, 1)
end = dt.datetime(2018, 3, 24)


#SPDR Main Sector Tickers#
#tickers = ['XLV', 'XLU', 'XLE', 'XLB', 'XLI', 'XLP', 'XLRE', 'XLF', 'XLY', 'XLK', 'AGG', 'SPY']

#Defense Tickers#
#tickers = ['BA', 'UTX', 'LMT', 'GD', 'RTN', 'COL', 'LLL', 'TDG', 'HII', 'SPR', 'XAR', 'ITA', 'SPY', 'NOC']

#Custom Tickers#
tickers = ['MTUM', 'VLUE', 'USMV', 'SPY', 'EEM', 'AGG', 'GLD']

#Start to pull data#
df = web.DataReader(tickers, 'yahoo', start, end)

price = df['Adj Close'] #Use 'Adj Close' to account for dividends and splits.#
#price= df['Close'] #Use just 'Close' when calculating inside periods not going to present#

dev = price.std()
var = price.var()

returns = price.pct_change()
ret = price.rolling(252).mean() #Annual rolling percent change#

#Calculate Percent Change#
#Manipulate data to pull change from start to end. Still working out how to best accomplish this#

df1 = price.iloc[[0, -1]]
#print(df1)

pct = df1.pct_change()*100
#pct.to_csv('da.csv')

df2 = df1.iloc[[0, -1]] = df1.iloc[[-1, 0]]
#print(df2)
change = df2.pct_change()*100
#change.to_csv('Pct.csv')


#Pull and plot just daily percent change#

##df3 = price.pct_change()

##df3.plot()
##plt.title('Daily Sector Percent Change')
##plt.show()


#change.to_csv('Defense.csv')

#Calculate Correlation#

z = returns.corr()*100
corr = returns.rolling(5, min_periods=1).corr(price)*100
x = returns.cov()

#print (returns)

#print(corr)


#print (ret)
#print (pct)
#print (price)
#print (returns)

##returns.plot()
##plt.show()

#z.plot()
#plt.show()

##corr.plot()
##plt.show()

print ('Standard Deviation\n',(dev))
print ('Variance\n', (var))
print ('Covariance\n', (x))
print ('Correlation\n', (z))
#print (pct)
print ('Percent Returns\n', (change))

##Combine all of them into one dataframe#
##df4 = dev
##df5 = pct
##df6 = change
##df7 = z
##df8 = x
##df9 = 
