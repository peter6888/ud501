import unittest
from optimization import optimize_portfolio
import datetime as dt
import numpy as np

# Dynamic test injection adapted from ideas found at:
# http://stackoverflow.com/questions/347109/how-do-i-concisely-implement-multiple-similar-unit-tests-in-the-python-unittest

# Test class for mc1-p2 adapted from @lauradhamilton's test_mc1_p1.py

# We will be generating test methods from a data structure, so our TestCase
# class doesn't actually contain any test_* methods yet.
class PortfolioTestCase(unittest.TestCase):
    # Check_analysis defines what we will actually do for each injected test case.
    def check_analysis(self, name, start_date, end_date, symbols,
                       v_cr, v_adr, v_sddr, v_sr, v_allocs):
        print name
        allocs, cr, adr, sddr, sr = optimize_portfolio(sd=start_date, ed=end_date,
                                                       syms=symbols, gen_plot=False)
        np.testing.assert_almost_equal([v_cr, v_adr, v_sddr, v_sr],
                                       [cr, adr, sddr, sr], 5)
        np.testing.assert_almost_equal(v_allocs, allocs, 5)
        print allocs
        print sr


# This is a function that generates and returns a method, suitable
# for inclusion in the PortfolioTestCase class, that calls check_analysis
# with the given parameters.
def generate_test_method(description, start_date, end_date, symbols,
                         v_cr, v_adr, v_sddr, v_sr, v_allocs):
    def test_method(self):
        self.check_analysis(description, start_date, end_date, symbols,
                            v_cr, v_adr, v_sddr, v_sr, v_allocs)

    return test_method


# This function loops through a data structure of desired test cases and
# dynamically injects test_* methods into the PortfolioTestCase class.
def add_test_cases():
    # Iterate through descriptions of test cases
    for name, start_date, end_date, \
        symbols, \
        v_cr, v_adr, v_sddr, v_sr, v_allocs in [

        # Example #1 from the course wiki
        ("example_1", '2010-01-01', '2010-12-31',
         ['GOOG', 'AAPL', 'GLD', 'XOM'],
         0.360090826885, 0.00127710312803, 0.0101163831312, 2.00401501102,
         [float('5.38105153e-16'), float('3.96661695e-01'), float('6.03338305e-01'), float('-5.42000166e-17')]),

        # Example #2 from the course wiki
        ("example_2", '2004-01-01', '2006-01-01',
         ['AXP', 'HPQ', 'IBM', 'HNZ'],
        0.255021425162, 0.000494944887734, 0.0093236393828, 0.842697383626,
         [float('7.75113042e-01'), float('2.24886958e-01'), float('-1.18394877e-16'), float('-7.75204553e-17')]),

        # Example #3 from the course wiki
        ("example_3", '2004-12-01', '2006-05-31',
         ['YHOO', 'XOM', 'GLD', 'HNZ'],
         0.315973959221, 0.000762170576913, 0.00797126844855, 1.5178365773,
         [float('-3.84053467e-17'), float('7.52817663e-02'), float('5.85249656e-01'), float('3.39468578e-01')]),

        # Example #4 from the course wiki
        ("example_4", '2005-12-01', '2006-05-31',
         ['YHOO', 'HPQ', 'GLD', 'HNZ'],
         0.229471589743, 0.00171589132005, 0.00842416845541, 3.2334265871,
         [float('-1.67414005e-15'), float('1.01227499e-01'), float('2.46926722e-01'), float('6.51845779e-01')]),
    ]:
        # For each test case, dynamically generate a method and inject it into
        # the PortfolioTestCase class, with a name starting with 'test' so it
        # will be picked up by unittest.main().
        setattr(PortfolioTestCase, 'test_' + name,
                generate_test_method(name, start_date, end_date, symbols,
                                     v_cr, v_adr, v_sddr, v_sr, v_allocs))


# Inject our test cases into PortfolioTestCase
add_test_cases()

# Run Unittest only if we are the main module
if __name__ == '__main__':
    unittest.main()

