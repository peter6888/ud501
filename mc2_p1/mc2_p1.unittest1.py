__author__ = 'lauradhamilton'

import unittest
import datetime as dt
import marketsim


class Mc2P1Test(unittest.TestCase):
    def test_orders_short(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-short.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals) 

        self.assertAlmostEqual(998035.0, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(11, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))


    def test_orders(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1133860.0, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(240, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))


    def test_orders2(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders2.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1078752.6, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(232, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))


    def test_orders_leverage(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1087919.23, final_portfolio_value, 4, "Final portfolio value is {} incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(232, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))

if __name__ == '__main__':
    unittest.main()

