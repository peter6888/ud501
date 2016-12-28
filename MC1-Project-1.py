"""
ud501 course (a.k.a CS7646 course) http://quantsoftware.gatech.edu/MC1-Project-1
Setup mentioned http://quantsoftware.gatech.edu/ML4T_Software_Setup
This file intent to be ml4t/mc1_p1/analysis.py file
"""
import unittest
import datetime as dt

class AssesssPortfolio(unittest.TestCase):
    def test_assess_portfolio(self):
        """
        This function intent to be test assess_portfolio() function, which will use below call to test on
        """
        cr, adr, sddr, sr, ev = \
            self.assess_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
            syms=['GOOG','AAPL','GLD','XOM'], \
            allocs=[0.1,0.2,0.3,0.4], \
            sv=1000000, rfr=0.0, sf=252.0, \
            gen_plot=False)
        self.assertTrue(True)

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
        return (None, None, None, None, None)