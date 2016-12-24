import pandas as pd
import matplotlib.pyplot as plt
import unittest
import numpy as np
from stocks import stocks
from datetime import datetime

class UdaCity_MLT(unittest.TestCase):

    def test_run(self):
        df = pd.read_csv("data/aapl.csv")
        df[['Adj Close', 'Close']].plot()
        plt.show()

    def test_run2(self):
        start_date='2016-12-01'
        end_date='2016-12-15'
        dates=pd.date_range(start_date,end_date)
        df1=pd.DataFrame(index=dates)
        #print(df1)

        #read SPY data
        ds_spy = pd.read_csv('data/spy.csv', index_col='Date',
                             parse_dates=True, usecols=['Date', 'Adj Close'],
                             na_values=['nan'])

        #print(ds_spy)
        df1=df1.join(ds_spy, how='inner') #left, right, inner, outer
        #df1 = df1.dropna()
        df1.plot()
        plt.show()

    def test_np(self):
        a = np.random.randint(0,500,10)
        print('for a = {} max(a)=a[{}]={}'.format(a, a.argmax(), a.max()))
        print('a.size={}'.format(a.size))
        print('a slice [:5] = {}'.format(a[:5]))

    def test_incompletdata_01_05(self):
        s = stocks()
        s.get_data('JAMN', start=datetime(2005,12,31), end=datetime(2014,12,07))
        spy = s.get_data('SPY')
        print('-----------------')
        print(spy)
        pass

    def test_plot_spy(self):
        s = stocks()
        spydata = s.get_data('SPY')
        #print(type(spydata))
        print(spydata.axes)
        #spydata.plot()
        #plt.show()
        dates = pd.date_range('2012-01-01', '2012-12-31')
        df = pd.DataFrame(index=dates)
        print(df.axes)
        spydata.rename(columns={'Adj Close':'SPY'})
        df.join(spydata)
        spydata.to_csv('data/{}.csv'.format('SPY'))
        spydata.plot()
        plt.show()

    def test_1_6(self):
        daily_returns = self.get_daily_returns()
        self.plot_data(daily_returns, title='Daily returns') #, ylabel='Daily returns')

        daily_returns.hist(bins=20)
        plt.show()

        daily_returns['SPY'].hist(bins=20, label='SPY')
        daily_returns['XOM'].hist(bins=20, label='XOM')
        daily_returns['GLD'].hist(bins=20, label='GLD')
        plt.legend(loc='upper right')
        plt.show()

    def test_1_6_scatterplots(self):
        daily_returns = self.get_daily_returns()
        daily_returns.plot(kind='scatter', x='SPY', y='XOM')
        beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
        plt.plot(daily_returns['SPY'], beta_XOM * daily_returns['SPY'] + alpha_XOM, '-', color='r')
        plt.show()

    def plot_data(self, df, title="Stock prices"):
        """Plot stock prices with a custom title and meaningful axis labels."""
        ax = df.plot(title=title, fontsize=12)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        plt.show()

    def compute_daily_returns(self, df):
        """
        compute daily returns
        :param df:
        :return:
        """
        daily_returns = df.copy()
        daily_returns[1:] = (df[1:] / df[:-1].values) - 1
        daily_returns.ix[0, :] = 0 # set daily returns for row 0 to 0
        return daily_returns

    def get_daily_returns(self):
        s = stocks()
        dates = pd.date_range('2009-01-01', '2012-12-31')
        symbols = ['SPY', 'XOM', 'GLD']
        df = s.get_datas(symbols,dates)
        #self.plot_data(df)
        return self.compute_daily_returns(df)
    