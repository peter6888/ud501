import unittest
import matplotlib
matplotlib.use('Agg')
import optimization as opt


class TestMCP2(unittest.TestCase):
    pass


tests = {
    'Example1': {
        'args': {
            'start_date': '2010-01-01',
            'end_date': '2010-12-31',
            'symbols': ['GOOG', 'AAPL', 'GLD', 'XOM'],
        },
        'results': {
            'allocs': [0.0, 0.39661695, .603338305, 0.0],
            'sharpe': 2.00401501102,
            'volatility': 0.0101163831312,
            'adr': 0.00127710312803,
            'cumulative_return': 0.360090826885,
        }},
    'Example2': {
        'args': {
            'start_date': '2004-01-01',
            'end_date': '2006-01-01',
            'symbols': ['AXP', 'HPQ', 'IBM', 'HNZ'],
        },
        'results': {
            'allocs': [0.775113042, 0.224886958, 0.0, 0.0],
            'sharpe': 0.842697383626,
            'volatility': 0.0093236393828,
            'adr': 0.000494944887734,
            'cumulative_return': 0.255021425162,
        }},
    'Example3': {
        'args': {
            'start_date': '2004-12-01',
            'end_date': '2006-05-31',
            'symbols': ['YHOO', 'XOM', 'GLD', 'HNZ'],
        },
        'results': {
            'allocs': [ -3.84053467e-17, 7.52817663e-02, 5.85249656e-01, 3.39468578e-01],
            'sharpe': 1.5178365773,
            'volatility': 0.00797126844855,
            'adr': 0.000762170576913,
            'cumulative_return': 0.315973959221,
        }},
    'Example4': {
        'args': {
            'start_date': '2005-12-01',
            'end_date': '2006-05-31',
            'symbols': ['YHOO', 'HPQ', 'GLD', 'HNZ'],
        },
        'results': {
            'allocs': [-1.67414005e-15, 1.01227499e-01, 2.46926722e-01, 6.51845779e-01],
            'sharpe': 3.2334265871,
            'volatility': 0.00842416845541,
            'adr': 0.00171589132005,
            'cumulative_return': 0.229471589743,
        },
    },
    'UserExample1': {
        'args': {
            'start_date': '2004-01-01',
            'end_date': '2006-01-01',
            'symbols': ['AXP', 'HPQ', 'IBM', 'HNZ', 'YHOO'],
        },
        'results': {
            'allocs':[5.96720975e-01,
                      1.03885481e-01,
                      0.00000000e+00,
                      1.37232890e-16,
                      2.99393544e-01],
            'sharpe': 1.0569849024,
            'volatility': 0.0108163816073,
            'adr': 0.000720195684412,
            'cumulative_return': 0.394860863607,
        },
    },
    'UserExample2': {
        'args': {
            'start_date': '2004-01-01',
            'end_date': '2006-01-01',
            'symbols': ['HPQ', 'HNZ', 'YHOO'],
        },
        'results': {
            'allocs': [5.71453264e-02, 1.78676518e-16, 9.42854674e-01],
            'sharpe': 0.970122332123,
            'volatility': 0.0207701736385,
            'adr': 0.00126930607603,
            'cumulative_return': 0.700039633035,
        },
    },

}

def t_generator(*args, **kwargs):
    def t(self):
        self.assertAlmostEqual(*args, **kwargs)
    return t

def range_generator(value):
    def t(self):
        self.assertGreaterEqual(value, -0.02)
        self.assertLessEqual(value, 1.02)
    return t

for name, test in tests.iteritems():
    allocations, cr, adr, sddr, sr = opt.optimize_portfolio(
        sd = test['args']['start_date'],
        ed = test['args']['end_date'],
        syms = test['args']['symbols'],
        gen_plot = False,
    )

    t = t_generator(cr, test['results']['cumulative_return'], places=4)
    setattr(TestMCP2, "test_{0}_cumulative_return".format(name), t)

    t = t_generator(adr, test['results']['adr'], places=4)
    setattr(TestMCP2, "test_{0}_adr".format(name), t)

    t = t_generator(sddr, test['results']['volatility'], places=4)
    setattr(TestMCP2, "test_{0}_volatility".format(name), t)

    t = t_generator(sr, test['results']['sharpe'], places=4)
    setattr(TestMCP2, "test_{0}_sharpe_ratio".format(name), t)

    t = t_generator(1.0, sum(allocations), delta=0.02)
    setattr(TestMCP2, "test_{0}_allocation_sum".format(name), t)

    allocs = test['results']['allocs']
    for idx, stock in enumerate(test['args']['symbols']):
        t = t_generator(allocations[idx], allocs[idx], delta=.1)
        setattr(TestMCP2, "test_{0}_allocation_{1}".format(name, stock), t)

        t = range_generator(allocations[idx])
        setattr(TestMCP2, "test_{0}_allocation_in_range".format(name), t)


if __name__ == '__main__':
    unittest.main()        
