import unittest

class LibraryCheck(unittest.TestCase):
    def test_numpy(self):
        import numpy as np
        l = [5,6,7]
        nparray = np.array(l)
        self.assertIsNotNone(nparray)
        self.assertTrue(len(nparray) == 3)

    def test_pandas(self):
        import pandas as pd
        s = pd.Series([1,3,5,6,9])
        self.assertTrue(len(s)==5)

    def test_matplotlib(self):
        import matplotlib.pyplot as plt
        import numpy as np
        t = np.arange(0.0, 2.0, 0.01)
        s = np.sin(2 * np.pi * t)
        plt.plot(t, s)
        plt.show()

    def test_pandas_datareader(self):
        """
        http://stackoverflow.com/questions/12433076/download-history-stock-prices-automatically-from-yahoo-finance-in-python/12510334#12510334
        :return:
        """
        from pandas_datareader import data
        from datetime import datetime
        ibm = data.get_data_yahoo(symbols='ibm', start=datetime(2000,1,1), end=datetime(2012,1,1))
        self.assertTrue(len(ibm) > 2)

    def test_scipy(self):
        """
        Under Ubuntu need to run this first
        sudo apt-get install libatlas-base-dev gfortran
        :return:
        """
        from scipy.optimize import minimize, rosen, rosen_der
        x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
        res = minimize(rosen, x0, method='Nelder-Mead', tol=1e-6)
        print(res.x)