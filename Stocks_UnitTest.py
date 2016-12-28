import unittest
from stocks import stocks

class Stocks_UnitTest(unittest.TestCase):
    def test_download_data(self):
        symbols = ['MSFT','IBM','SPY','AAPL']
        self.assertIsNotNone(symbols)
        for sb in symbols:
            self.pullData(sb)

    def test_cache(self):
        """
        need implement a cache for visited stocks
        :return:
        """
        s = stocks()
        s.get_data("MSFT")
        self.assertTrue(s.is_cached("MSFT"))

    def test_data_to_csv(self):
        import os
        s = stocks()
        s.get_data_to_csv("MSFT")
        self.assertTrue(os.path.isfile(s.symbol_to_path("MSFT")))

    def test_get_cmcm(self):
        s = stocks()
        s.get_data('CMCM')
        self.assertTrue(s.is_cached('CMCM'))

    def pullData(self, stock):
        """
        use pandas datareader to read history stock data from yahoo
        :param stock: stock symbol
        :return: None
        """
        s = stocks()
        currstock = s.get_data(stock)
        print(len(currstock))