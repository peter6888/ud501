__author__ = 'snasar'

import unittest
import datetime as dt
import optimization as o


class Mc1P2Test(unittest.TestCase):
    def test_example1(self):
        start_date = dt.datetime(2010,01,01)
        end_date = dt.datetime(2010,12,31)
        symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']

        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252.0

        # Assess the portfolio
        allocations, cr, adr, sddr, sr = o.optimize_portfolio(sd = start_date, 
                                                              ed = end_date, 
                                                              syms = symbols, 
                                                              gen_plot = False)        

        self.assertAlmostEqual(0.360090826885, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(2.00401501102, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.00127710312803, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.0101163831312, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)

    def test_example2(self):
        start_date = dt.datetime(2004,01,01)
        end_date = dt.datetime(2006,01,01)
        symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']

        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252.0

        # Assess the portfolio
        allocations, cr, adr, sddr, sr = o.optimize_portfolio(sd = start_date, 
                                                              ed = end_date, 
                                                              syms = symbols, 
                                                              gen_plot = False)        

        self.assertAlmostEqual(0.255021425162, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(0.842697383626, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.000494944887734, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.0093236393828, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)



    def test_example3(self):
        start_date = dt.datetime(2004,12,01)
        end_date = dt.datetime(2006,05,31)
        symbols = ['YHOO', 'XOM', 'GLD', 'HNZ']

        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252.0

        # Assess the portfolio
        allocations, cr, adr, sddr, sr = o.optimize_portfolio(sd = start_date, 
                                                              ed = end_date, 
                                                              syms = symbols, 
                                                              gen_plot = False)        

        self.assertAlmostEqual(0.315973959221, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(1.5178365773, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.000762170576913, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.00797126844855, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)


    def test_example4(self):
        start_date = dt.datetime(2005,12,01)
        end_date = dt.datetime(2006,05,31)
        symbols = ['YHOO', 'HPQ', 'GLD', 'HNZ']

        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252.0

        # Assess the portfolio
        allocations, cr, adr, sddr, sr = o.optimize_portfolio(sd = start_date, 
                                                              ed = end_date, 
                                                              syms = symbols, 
                                                              gen_plot = False)        

        self.assertAlmostEqual(0.229471589743, cr, 3, "Cumulative Return {} is incorrect".format(cr), delta=None)
        self.assertAlmostEqual(3.2334265871, sr, 3, "Sharpe Ratio {} is incorrect".format(sr), delta=None)
        self.assertAlmostEqual(0.00171589132005, adr, 5, "Avg Daily Return {} is incorrect".format(adr), delta=None)
        self.assertAlmostEqual(0.00842416845541, sddr, 5,
                               "Volatility (stdev of daily returns) {} is incorrect".format(sddr), delta=None)

 

if __name__ == '__main__':
    unittest.main()
