"""
ud501 course (a.k.a CS7646 course) http://quantsoftware.gatech.edu/MC1-Project-1
Setup mentioned http://quantsoftware.gatech.edu/ML4T_Software_Setup
This file intent to be ml4t/mc1_p1/analysis.py file
"""
import unittest
import datetime as dt
import pandas as pd
from stocks import stocks
import numpy as np

class AssesssPortfolio(unittest.TestCase):
    def test_assess_portfolio(self):
        """
        This function intent to be test assess_portfolio() function, which will use below call to test on
        """
        ret = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['GOOG','AAPL','GLD','XOM'], \
            allocs=[0.2,0.3,0.4,0.1], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        """ Example result
        Start Date: 2010-01-01
        End Date: 2010-12-31
        Symbols: ['GOOG', 'AAPL', 'GLD', 'XOM']
        Allocations: [0.2, 0.3, 0.4, 0.1]
        Sharpe Ratio: 1.51819243641
        Volatility (stdev of daily returns): 0.0100104028
        Average Daily Return: 0.000957366234238
        Cumulative Return: 0.255646784534

        with diagram "SPY" and "Portfolio"
        """
        print(ret)
        (cr, adr, sddr, sr, ev) = ret
        self.assertTrue(True)

    def test_all(self):
        """
        http://quantsoftware.gatech.edu/MC1-Project-1-Test-Cases-spr2016
        :return: None
        """
        #test case 01
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['GOOG','AAPL','GLD','XOM'], \
            allocs=[0.2,0.3,0.4,0.1], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        (desired_cr, desired_adr, desired_sr) = (0.255646784534, 0.000957366234238, 1.51819243641)
        self.assertTrue(abs(cr-desired_cr) < 0.001)
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01)
        #test case 02
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['AXP','HPQ','IBM','HNZ'], \
            allocs=[0.0,0.0,0.0,1.0], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        (desired_cr, desired_adr, desired_sr) = (0.22483215628, 0.000763106152672, 1.44968707121)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

    def assess_portfolio(self, sd, ed, syms, allocs, sv, rfr, sf, gen_plot):
        """
        http://quantsoftware.gatech.edu/MC1-Project-1#API_specification
        :param sd: A datetime object that represents the start date
        :param ed: A datetime object that represents the end date
        :param symb: A list of symbols that make up the portfolio (note that your code should support any symbol in the data directory)
        :param allocs: A list of allocations to the stocks, must sum to 1.0
        :param sv: Start value of the portfolio
        :param rfr: The risk free return per sample period for the entire date range (a single number, not an array).
        :param sf: Sampling frequency per year
        :param gen_plot: If True, create a plot named plot.png
        :return: (cr, adr, sddr, sr, ev)
                cr: Cumulative return
                adr: Average period return (if sf == 252 this is daily return)
                sddr: Standard deviation of daily return
                sr: Sharpe ratio
                ev: End value of portfolio
        """
        symbols = list(syms)
        s = stocks()
        dates = pd.date_range(sd,ed)
        df = s.get_datas(syms,dates)
        df = df.div(df.ix[0])
        df = df.multiply([1.0] + allocs)
        df['portfolio'] = df.sum(axis=1) - df['SPY']
        df.drop(symbols, axis=1, inplace=True)
        #s.plot_data(df)
        cr = df['portfolio'][-1] - 1
        adr = cr / sf
        df = df * sv
        #s.plot_data(df)
        daily_return = s.compute_daily_returns(df)
        #s.plot_data(daily_return)
        sddr = daily_return.std()['portfolio']
        sr = np.sqrt(sf) * (daily_return-rfr)['portfolio'].mean() / sddr
        ev = df['portfolio'][-1]
        return (cr, adr, sddr, sr, ev)
