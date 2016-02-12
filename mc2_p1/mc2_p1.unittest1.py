__author__ = 'lauradhamilton'

import unittest
import datetime as dt
import marketsim
from analysis import get_portfolio_stats, compute_daily_returns

class Mc2P1Test(unittest.TestCase):
    def test_orders_short(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-short.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals) 

        self.assertAlmostEqual(998035.0, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(11, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))
        
        cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        
        expected_value = -0.446948390642
        self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
        
        expected_value = -0.001965
        self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
        
        expected_value = 0.00634128215394
        self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
        
        expected_value = -0.000178539446839
        self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
    
        '''
        Sharpe Ratio of Fund: -0.446948390642
        Sharpe Ratio of $SPX: 0.882168679776
        
        Cumulative Return of Fund: -0.001965
        Cumulative Return of $SPX: 0.00289841448894
        
        Standard Deviation of Fund: 0.00634128215394
        Standard Deviation of $SPX: 0.00544933521991
        
        Average Daily Return of Fund: -0.000178539446839
        Average Daily Return of $SPX: 0.000302827205547
        
        Final Portfolio Value: 998035.0
        '''
        
    def test_orders(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1133860.0, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(240, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))
        
        cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        
        expected_value = 1.21540888742
        self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
        
        expected_value = 0.13386
        self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
        
        expected_value = 0.00720514136323
        self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
        
        expected_value = 0.000551651296638
        self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
    
        '''
        Sharpe Ratio of Fund: 1.21540888742
        Sharpe Ratio of $SPX: 0.0183389807443
        
        Cumulative Return of Fund: 0.13386
        Cumulative Return of $SPX: -0.0224059854302
        
        Standard Deviation of Fund: 0.00720514136323
        Standard Deviation of $SPX: 0.0149716091522
        
        Average Daily Return of Fund: 0.000551651296638
        Average Daily Return of $SPX: 1.7295909534e-05
        
        Final Portfolio Value: 1133860.0
        '''

    def test_orders2(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders2.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1078752.6, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(232, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))

        cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        
        expected_value = 0.788982285751
        self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
        
        expected_value = 0.0787526
        self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
        
        expected_value = 0.00711102080156
        self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
        
        expected_value = 0.000353426354584
        self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
                
        '''
        Sharpe Ratio of Fund: 0.788982285751
        Sharpe Ratio of $SPX: -0.177203019906
        
        Cumulative Return of Fund: 0.0787526
        Cumulative Return of $SPX: -0.0629581516192
        
        Standard Deviation of Fund: 0.00711102080156
        Standard Deviation of $SPX: 0.0150564855724
        
        Average Daily Return of Fund: 0.000353426354584
        Average Daily Return of $SPX: -0.000168071648902
        
        Final Portfolio Value: 1078752.6
        '''

    def test_orders3(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders3.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1050160.0, final_portfolio_value, 4, "Final portfolio value {} is incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(141, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))

        cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        
        # TODO: Fails
        expected_value = 1.03455887842
        self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
        
        expected_value = 0.05016
        self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
        
        expected_value = 0.00560508094997
        self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
        
        expected_value = 0.000365289198877
        self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
        
        '''
        Sharpe Ratio of Fund: 1.03455887842
        Sharpe Ratio of $SPX: 0.247809335326
        
        Cumulative Return of Fund: 0.05016
        Cumulative Return of $SPX: 0.0135380980508
        
        Standard Deviation of Fund: 0.00560508094997
        Standard Deviation of $SPX: 0.00840618502785
        
        Average Daily Return of Fund: 0.000365289198877
        Average Daily Return of $SPX: 0.000131224926273
        
        Final Portfolio Value: 1050160.0
        '''


    def test_orders_leverage_1(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage-1.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1050160.0, final_portfolio_value, 4, "Final portfolio value is {} incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(106, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))
        
        cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        
        expected_value = 1.19402406143
        self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
        
        expected_value = 0.05016
        self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
        
        expected_value = 0.00647534272091
        self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
        
        expected_value = 0.000487052265169
        self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
        
        '''
        Sharpe Ratio of Fund: 1.19402406143
        Sharpe Ratio of $SPX: 0.0814792462178
        
        Cumulative Return of Fund: 0.05016
        Cumulative Return of $SPX: 0.000968694624926
        
        Standard Deviation of Fund: 0.00647534272091
        Standard Deviation of $SPX: 0.00801527501158
        
        Average Daily Return of Fund: 0.000487052265169
        Average Daily Return of $SPX: 4.11400826828e-05
        
        Final Portfolio Value: 1050160.0
        '''
        
    def test_orders_leverage_2(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage-2.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        self.assertAlmostEqual(1074650.0, final_portfolio_value, 4, "Final portfolio value is {} incorrect".format(final_portfolio_value), delta=None)
        self.assertEqual(37, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect".format(final_portfolio_dataframe_length))
        
        cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        
        expected_value = 4.92529481246
        self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
        
        expected_value = 0.07465
        self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
        
        expected_value = 0.00651837064888
        self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
        
        expected_value = 0.00202241842159
        self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg dailt return {} is incorrect. Expected".format(avg_daily_ret[0], expected_value), delta=None)
        
        '''
        Sharpe Ratio of Fund: 4.92529481246
        Sharpe Ratio of $SPX: 2.65553881849
        
        Cumulative Return of Fund: 0.07465
        Cumulative Return of $SPX: 0.0482142153967
        
        Standard Deviation of Fund: 0.00651837064888
        Standard Deviation of $SPX: 0.00801128120646
        
        Average Daily Return of Fund: 0.00202241842159
        Average Daily Return of $SPX: 0.00134015293001
        
        Final Portfolio Value: 1074650.0
        '''
        
        
if __name__ == '__main__':
    unittest.main()

