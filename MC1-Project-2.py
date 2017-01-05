
import unittest
import datetime as dt
import pandas as pd
from stocks import stocks
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spo
from scipy.optimize import minimize

class SharperOptiminze(unittest.TestCase):
    def test_minimize(self):
        from scipy.optimize import minimize, rosen, rosen_der
        x0 = [1.3, 0.7, 0.8, 1.9, 1.2]
        res = minimize(rosen, x0, method='Nelder-Mead', tol=1e-6)
        print(res.x)

    def test_run(self):
        # define original line
        l_orig = np.float32([4,2])
        x_orig = np.linspace(0, 10, 21)
        print(x_orig)
        y_orig = l_orig[0] * x_orig + l_orig[1]
        plt.plot(x_orig, y_orig, 'b--', linewidth=2.0, label="Original line")

        # Generate noisy data points
        noise_sigma = 3.0
        noise = np.random.normal(0, noise_sigma, y_orig.shape)
        data = np.asarray([x_orig, y_orig + noise]).T
        plt.plot(data[:,0], data[:,1], 'go', label='Data points')

        l_fit = self.fit_line(data, self.error)
        print(l_fit)
        plt.plot(data[:,0], l_fit[0] * data[:,0] + l_fit[1], 'r--', linewidth=2.0, label='Matched line')
        plt.show()

    def error(self, line, data):
        err = np.sum((data[:,1] - (line[0] * data[:, 0]) + line[1]) ** 2)
        return err

    def fit_line(self, data, error_func):
        l = np.float32([0, np.mean(data[:,1])]) # slope = 0, intercept = mean(y values)
        x_ends = np.float32([-5,5])
        plt.plot(x_ends, l[0] * x_ends + l[1], 'm--', linewidth=2.0, label='Initial guess')

        result = spo.minimize(error_func, l, args=(data,), method='SLSQP', options={'disp':True})

        return result.x

