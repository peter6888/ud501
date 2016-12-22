"""
stocks.py - cached stock prices
"""
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

    def is_cached(self, symbol):
        return symbol in self.cached_symbols
