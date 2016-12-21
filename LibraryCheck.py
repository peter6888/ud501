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