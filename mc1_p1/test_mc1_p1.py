import unittest
from analysis import assess_portfolio
import datetime as dt
import numpy as np


# Dynamic test injection adapted from ideas found at:
# http://stackoverflow.com/questions/347109/how-do-i-concisely-implement-multiple-similar-unit-tests-in-the-python-unittest


# We will be generating test methods from a data structure, so our TestCase
# class doesn't actually contain any test_* methods yet.
class PortfolioTestCase(unittest.TestCase):

    # Check_analysis defines what we will actually do for each injected test case.
    def check_analysis(self, name, start_date, end_date, symbols,
                       allocations, sv, rfr, sf,
                       v_cr, v_adr, v_sddr, v_sr, v_ev):
        print name
        cr, adr, sddr, sr, ev = assess_portfolio(sd=start_date, ed=end_date,
                                                 syms=symbols, allocs=allocations,
                                                 sv=sv, rfr=rfr, gen_plot=False)
        np.testing.assert_almost_equal([v_cr, v_adr, v_sddr, v_sr, v_ev],
                                       [cr, adr, sddr, sr, ev], 5)
        print ev


# This is a function that generates and returns a method, suitable
# for inclusion in the PortfolioTestCase class, that calls check_analysis
# with the given parameters.
def generate_test_method(description, start_date, end_date, symbols,
                         allocations, sv, rfr, sf,
                         v_cr, v_adr, v_sddr, v_sr, v_ev):
    def test_method(self):
        self.check_analysis(description, start_date, end_date, symbols,
                            allocations, sv, rfr, sf,
                            v_cr, v_adr, v_sddr, v_sr, v_ev)
    return test_method


# This function loops through a data structure of desired test cases and
# dynamically injects test_* methods into the PortfolioTestCase class.
def add_test_cases():

    # Iterate through descriptions of test cases
    for name, start_date, end_date,\
        symbols, \
        allocations, sv, rfr, sf, \
        v_cr, v_adr, v_sddr, v_sr, v_ev in [

            # Example #1 from the course wiki
            ("example_1", '2010-01-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1], 1000000, 0, 252,
             0.255646784534, 0.000957366234238, 0.0100104028, 1.51819243641, 1255646.78453),

            # Example #2 from the course wiki
            ("example_2", '2010-01-01', '2010-12-31',
             ['AXP', 'HPQ', 'IBM', 'HNZ'],
             [0.0, 0.0, 0.0, 1.0], 1000000, 0, 252,
             0.198105963655, 0.000763106152672, 0.00926153128768, 1.30798398744, 1198105.96365),

            # Example #3 from the course wiki
            ("example_3", '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1], 1000000, 0, 252,
             0.205113938792, 0.00129586924366, 0.00929734619707, 2.21259766672, 1205113.93879),

            # Risk free rate with 1.5% daily return
            ("rfr_1", '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1], 1000000, 0.015, 252,
             0.205113938792, 0.00129586924366, 0.00929734619707, -23.3987556107, 1205113.93879),

            # Risk free rate with 1.5% equivalent annual return
            ("rfr_2", '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1], 1000000, 0.00005908, 252,
             0.205113938792, 0.00129586924366, 0.00929734619707, 2.11171703734, 1205113.93879),

            # Additional test #6
            ("test_6", '2010-01-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.2, 0.4, 0.2], 1000000, 0, 252,
             0.213526797808, 0.000814502803749, 0.00930020797913, 1.39027333521, 1213526.79781),

            # Additional test #7
            ("test_7", '2009-01-01', '2011-12-31',
             ['CBS', 'DIS', 'VIAB'],
             [0.33, 0.34, 0.33], 1000000, 0, 252,
             1.39455419951, 0.00143518275443, 0.0236414905805, 0.963679504361, 2394554.19951),

            # Additional test #8
            ("test_8", '2009-01-01', '2011-12-31',
             ['WFC', 'IBM', 'KO', 'WMT'],
             [0.4, 0.3, 0.2, 0.1], 1000000, 0, 252,
             0.499431577786, 0.00068515522105, 0.0172994353627, 0.628720054628, 1499431.57779),

            ]:

        # For each test case, dynamically generate a method and inject it into
        # the PortfolioTestCase class, with a name starting with 'test' so it
        # will be picked up by unittest.main().
        setattr(PortfolioTestCase, 'test_' + name,
                generate_test_method(name, start_date, end_date, symbols,
                                     allocations, sv, rfr, sf,
                                     v_cr, v_adr, v_sddr, v_sr, v_ev))


# Inject our test cases into PortfolioTestCase
add_test_cases()

# Run Unittest only if we are the main module
if __name__ == '__main__':
    unittest.main()
