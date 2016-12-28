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
        #test case 01 - basic
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['GOOG','AAPL','GLD','XOM'], \
            allocs=[0.2,0.3,0.4,0.1], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.255646784534, 0.000957366234238, 1.51819243641)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))
        #test case 02 - One stock
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['AXP','HPQ','IBM','HNZ'], \
            allocs=[0.0,0.0,0.0,1.0], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.22483215628, 0.000763106152672, 1.44968707121)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 03 - six month
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,6,1), ed=dt.datetime(2010,12,31), \
            syms=['GOOG','AAPL','GLD','XOM'], \
            allocs=[0.2,0.3,0.4,0.1], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.205113938792, 0.00129586924366, 2.21259766672)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 04 - different allocations
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['GOOG','AAPL','GLD','XOM'], \
            allocs=[0.2,0.4,0.2,0.2], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.262285147745, 0.000993303139465, 1.3812384175)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 05 - Normalization check
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2013,05,31), \
            syms=['AXP','HPQ','IBM','GOOG'], \
            allocs=[0.3,0.5,0.1,0.1], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.138331232843, -6.50814806831e-05, 0.28383368517)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 06 - One month range
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,01,31), \
            syms=['AXP','HPQ','IBM','GOOG'], \
            allocs=[0.9,0.0,0.1,0.0], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (-0.0758725033871, -0.00411578300489, -2.76341822037)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 07 - Low Sharpe ratio
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2011,1,1), ed=dt.datetime(2011,12,31), \
            syms=['WFR','AN','MWW','FSLR'], \
            allocs=[0.25,0.25,0.25,0.25], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (-0.53245984720788297, -0.0021129359016185834, -1.0598514101147192)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 08 - All-in-one
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,1,1), ed=dt.datetime(2010,12,31), \
            syms=['AXP','HPQ','IBM','HNZ'], \
            allocs=[0.0,1.0,0.0,0.0], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (-0.191620333598, -0.000718040989619, -0.71237182415)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        #test case 09 - Mid-year to Mid-year
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2010,6,1), ed=dt.datetime(2011,6,1), \
            syms=['AAPL','GLD','GOOG','XOM'], \
            allocs=[0.1,0.4,0.5,0.0], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.177352039318, 0.000694756409052, 1.10895144722)
        self.assertTrue(abs(cr-desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr-desired_adr) < 0.001, '{} vs {}'.format(adr,desired_adr))
        self.assertTrue(abs(sr-desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

        # test case 10 - Two years
        (cr, adr, sddr, sr, ev) = self.assess_portfolio(sd=dt.datetime(2006, 1, 3), ed=dt.datetime(2008, 1, 2), \
                                                        syms=['MMM', 'MO', 'MSFT', 'INTC'], \
                                                        allocs=[0.0, 0.9, 0.1, 0.0], \
                                                        sv=1000000, rfr=0.0, sf=252.0, \
                                                        gen_plot=False)
        print((cr, adr, sddr, sr, ev))
        (desired_cr, desired_adr, desired_sr) = (0.43732715979, 0.00076948918955, 1.26449481371)
        self.assertTrue(abs(cr - desired_cr) < 0.001, '{} vs {}'.format(cr, desired_cr))
        self.assertTrue(abs(adr - desired_adr) < 0.001, '{} vs {}'.format(adr, desired_adr))
        self.assertTrue(abs(sr - desired_sr) < 0.01, '{} vs {}'.format(sr, desired_sr))

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
        df['portfolio'] = df[symbols].sum(axis=1)
        df.drop(symbols, axis=1, inplace=True)
        #s.plot_data(df)
        cr = df['portfolio'][-1] - 1
        adr = cr / len(df)
        df = df * sv
        #s.plot_data(df)
        daily_return = s.compute_daily_returns(df)
        sddr = daily_return.std()['portfolio']
        sr = np.sqrt(sf) * (daily_return['portfolio'].mean() - rfr) / sddr
        ev = df['portfolio'][-1]
        return (cr, adr, sddr, sr, ev)
