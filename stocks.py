"""
stocks.py - cached stock prices
"""
import os
from pandas_datareader import data
from datetime import datetime

class stocks(object):
    def __init__(self):
        #self.cache_size = 5 # cache size
        self.cached_symbols = set()
        self.cache = {}

    def get_data(self, symbol, start=datetime(2000,1,1), end=datetime(2016,1,1)):
        if symbol in self.cached_symbols:
            return self.cache[symbol]
        self.cache[symbol] = data.get_data_yahoo(symbols=symbol, start=start, end=end)
        self.cached_symbols.add(symbol)
        return self.cache[symbol]

    def get_data_to_csv(self, symbol, start=datetime(2000,1,1), end=datetime(2016,1,1)):
        """
        get data and store to csv
        :param symbol:
        :param start:
        :param end:
        :return:
        """
        data = self.get_data(symbol, start, end)
        data.to_csv(self.symbol_to_path(symbol))
        return data

    def is_cached(self, symbol):
        return symbol in self.cached_symbols

    def symbol_to_path(self, symbol, base_dir="data"):
        """Return CSV file path given ticker symbol."""
        return os.path.join(base_dir, "{}.csv".format(str(symbol)))
