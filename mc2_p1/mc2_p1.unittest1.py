import unittest
import datetime as dt
import marketsim
try:
    from analysis import get_portfolio_stats
except ImportError:
    pass


class Mc2P1Test(unittest.TestCase):
    def try_get_portfolio_stats(self, portvals):
        statsMethodExists = True
        
        # First try from previous assignment file
        try:
            cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = get_portfolio_stats(portvals)
        except AttributeError:
            statsMethodExists = False
        
        if statsMethodExists:
            return statsMethodExists, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio
        
        # Otherwise try this function
        try:
            cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = marketsim.assess_my_portfolio(portvals)
        except AttributeError:
            statsMethodExists = False
            
        if statsMethodExists:
            return statsMethodExists, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio
        
        return False, 0., 0., 0., 0.
    
    def test_orders_short(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-short.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals) 

        expected_value = 998035.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 11
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
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

        expected_value = 1133860.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 240
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
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

        expected_value = 1078752.6
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 232
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
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

        expected_value = 1050160.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 141
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
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


    def test_orders_01(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-01.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1115569.2
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 245
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 0.612340613407
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.1155692
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.0142680745065
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.00055037432146
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_02(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-02.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1095003.35
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 245
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 1.01613520942
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.09500335
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00610110545183
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.000365289198877
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_03(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-03.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 857616.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 240
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = -0.759896272199
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = -0.142384
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.0119352106704
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = -0.000571326189931
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_04(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-04.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 923545.4
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 233
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = -0.266030146916
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = -0.0764546
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.0143332213612
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = -0.000240200768212
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_05(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-05.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1415563.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 296
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 2.19591520826
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.415563
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00880023087527
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.00121733290744
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_06(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-06.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 894604.3
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 210
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = -1.23463930987
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = -0.1053957
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00657385746675
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = -0.000511281541086
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


    def test_orders_07(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-07.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1106563.3
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 237
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 2.10356512897
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.1065633
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00327897532471
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.0004345040621
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


    def test_orders08(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-08.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1074884.1
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 229
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 0.941858298061
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.0748841
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00560508094997
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.000365289198877
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


    def test_orders_09(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-09.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1067710.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 37
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 2.90848480553
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.06771
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.0102202265027
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.00187252252117
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)


    def test_orders_10(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-10.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1050160.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 141
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 1.03455887842
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.05016
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00560508094997
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.000365289198877
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
        



    def test_orders_11(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-11.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1078670.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 37
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 3.28377563093
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.07867
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.0104365693923
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.00215889226484
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


    def test_orders_12(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-12.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1050160.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 240
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 0.792286003513
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.05016
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00428731360634
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.00021397693658
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_leverage(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1087919.23
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 232
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 0.449503553356
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.08791923
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.0196343644101
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.0005559678854
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_leverage_1(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage-1.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1050160.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 106
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 1.19402406143
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.05016
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00647534272091
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.000487052265169
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


    def test_orders_leverage_2(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage-2.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1074650.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 37
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 4.92529481246
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.07465
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00651837064888
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.00202241842159
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


    def test_orders_leverage_3(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage-3.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 1050160.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 141
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = 1.03455887842
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = 0.05016
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00560508094997
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = 0.000365289198877
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            

    def test_orders_leverage_4(self):
        portvals = marketsim.compute_portvals(orders_file = "./orders/orders-leverage-4.csv", start_val=1000000)
        final_portfolio_value = portvals.ix[-1,:][0]
        final_portfolio_dataframe_length = len(portvals)

        expected_value = 998035.0
        self.assertAlmostEqual(expected_value, final_portfolio_value, 4, "Final portfolio value is {} incorrect. Expected {}".format(final_portfolio_value, expected_value), delta=None)
        
        expected_value = 11
        self.assertEqual(expected_value, final_portfolio_dataframe_length, "Final portfolio dataframe length {} is incorrect. Expected {}".format(final_portfolio_dataframe_length, expected_value))

        success, cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = self.try_get_portfolio_stats(portvals)
            
        if success:
            expected_value = -0.446948390642
            self.assertAlmostEqual(expected_value, sharpe_ratio[0], 4, "Sharpe ratio {} is incorrect. Expected {}".format(sharpe_ratio[0], expected_value), delta=None)
            
            expected_value = -0.001965
            self.assertAlmostEqual(expected_value, cum_ret[0], 4, "Cumulative return {} is incorrect. Expected {}".format(cum_ret[0], expected_value), delta=None)
            
            expected_value = 0.00634128215394
            self.assertAlmostEqual(expected_value, std_daily_ret[0], 4, "Standard deviation {} is incorrect. Expected {}".format(std_daily_ret[0], expected_value), delta=None)
            
            expected_value = -0.000178539446839
            self.assertAlmostEqual(expected_value, avg_daily_ret[0], 4, "Avg daily return {} is incorrect. Expected {}".format(avg_daily_ret[0], expected_value), delta=None)
            


if __name__ == '__main__':
    unittest.main()
