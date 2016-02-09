__author__ = 'lauradhamilton'

import unittest
import datetime as dt
import marketsim


class Mc2P1Test(unittest.TestCase):
    def test_orders_short(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-short.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:]   

        self.assertAlmostEqual(998035.0, final_portfolio_value, 4, "Final portfolio value is incorrect".format(final_portfolio_value), delta=None)

    def test_orders(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:]

        self.assertAlmostEqual(1133860.0, final_portfolio_value, 4, "Final portfolio value is incorrect".format(final_portfolio_value), delta=None)

    def test_orders2(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders2.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:]

        self.assertAlmostEqual(1078752.6, final_portfolio_value, 4, "Final portfolio value is incorrect".format(final_portfolio_value), delta=None)

if __name__ == '__main__':
    unittest.main()

