import unittest
from analysis import assess_portfolio
import datetime as dt
import numpy as np


class PortfolioTestCase(unittest.TestCase):
    def test_results1(self):
        start_date = dt.datetime(2010, 1, 1)
        end_date = dt.datetime(2010, 12, 31)
        symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
        allocations = [0.2, 0.3, 0.4, 0.1]
        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252

        cr, adr, sddr, sr, ev = assess_portfolio(sd=start_date, ed=end_date, \
                                                 syms=symbols, \
                                                 allocs=allocations, \
                                                 sv=start_val, \
                                                 gen_plot=False)
        np.testing.assert_almost_equal([0.255646784534, 0.000957366234238, 0.0100104028, 1.51819243641, 1255646.78453],
                                       [cr, adr, sddr, sr, ev], 5)

    def test_results2(self):
        start_date = dt.datetime(2010, 1, 1)
        end_date = dt.datetime(2010, 12, 31)
        symbols = ['AXP', 'HPQ', 'IBM', 'HNZ']
        allocations = [0.0, 0.0, 0.0, 1.0]
        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252

        cr, adr, sddr, sr, ev = assess_portfolio(sd=start_date, ed=end_date, \
                                                 syms=symbols, \
                                                 allocs=allocations, \
                                                 sv=start_val, \
                                                 gen_plot=False)
        print ev
        np.testing.assert_almost_equal(
                [0.198105963655, 0.000763106152672, 0.00926153128768, 1.30798398744, 1198105.96365],
                [cr, adr, sddr, sr, ev], 5)

    def test_results3(self):
        start_date = dt.datetime(2010, 6, 1)
        end_date = dt.datetime(2010, 12, 31)
        symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
        allocations = [0.2, 0.3, 0.4, 0.1]
        start_val = 1000000
        risk_free_rate = 0.0
        sample_freq = 252

        cr, adr, sddr, sr, ev = assess_portfolio(sd=start_date, ed=end_date, \
                                                 syms=symbols, \
                                                 allocs=allocations, \
                                                 sv=start_val, \
                                                 gen_plot=False)
        print ev
        np.testing.assert_almost_equal(
                [0.205113938792, 0.00129586924366, 0.00929734619707, 2.21259766672, 1205113.93879],
                [cr, adr, sddr, sr, ev], 5)


if __name__ == '__main__':
    unittest.main()
