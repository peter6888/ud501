#!/usr/bin/env python
import numpy as np
import analysis
import datetime


def rfr_conv(rfr, sf):
    return (1.0+rfr)**(1.0/sf)-1.0


if __name__ == "__main__":

    start_time = datetime.datetime.now()

    for description, \
        start_date, end_date,\
        symbols, \
        allocations, \
        rfr, sf, should_fail, gen_plot, \
        v_cr, v_adr, v_sddr, v_sr, v_ev in [

            ("Example #1 from the course wiki",
             '2010-01-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1],
             0, 252, False, False,
             0.255646784534, 0.000957366234238, 0.0100104028, 1.51819243641, 1255646.78453),

            ("Example #2 from the course wiki",
             '2010-01-01', '2010-12-31',
             ['AXP', 'HPQ', 'IBM', 'HNZ'],
             [0.0, 0.0, 0.0, 1.0],
             0, 252, False, False,
             0.198105963655, 0.000763106152672, 0.00926153128768, 1.30798398744, 1198105.96365),

            ("Example #3 from the course wiki",
             '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1],
             0, 252, False, False,
             0.205113938792, 0.00129586924366, 0.00929734619707, 2.21259766672, 1205113.93879),

            # These are the values from the wiki for the plot.png to be turned in
            ("Test Case #4 (with plot)",
             '2010-01-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.2, 0.4, 0.2],
             0, 252, False, True,
             0.213526797808, 0.000814502803749, 0.00930020797913, 1.39027333521, 1213526.79781),

            ("Test Case #5",
             '2009-01-01', '2011-12-31',
             ['CBS', 'DIS', 'VIAB'],
             [0.33, 0.34, 0.33],
             0, 252, False, False,
             1.39455419951, 0.00143518275443, 0.0236414905805, 0.963679504361, 2394554.19951),

            ("Test Case #6",
             '2009-01-01', '2011-12-31',
             ['WFC', 'IBM', 'KO', 'WMT'],
             [0.4, 0.3, 0.2, 0.1],
             0, 252, False, False,
             0.499431577786, 0.00068515522105, 0.0172994353627, 0.628720054628, 1499431.57779),

            # Copied from Laura Hamilton - but passing rfr as a daily rate
            ("Risk free rate test",
             '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1],
             rfr_conv(0.015, 252), 252, False, False,
             0.205113938792, 0.00129586924366, 0.00929734619707, 2.11171703734, 1205113.93879),

            # Note - for weekly data (sf=52), I use: dates = pd.date_range(sd, ed, freq="W-FRI")
            ("Weekly values test",
             '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1],
             0, 52, False, False,
             0.206281186797, 0.00677856155691, 0.0245647783748, 1.98987761212, 1206281.1868),

            # Note - for monthly data (sf=12), I use: dates = pd.date_range(sd, ed, freq="BM")
            ("Monthly values test",
             '2010-06-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1],
             0, 12, False, False,
             0.237584996044, 0.0370190732108, 0.0463683816307, 2.76563094917, 1237584.99604),

            # Pathological cases

            ("One symbol portfolio",
             '2011-01-01', '2011-12-31',
             ['GOOG'],
             [1.0],
             0, 252, False, False,
             0.0687515512534, 0.000435296317827, 0.0185833707187, 0.371843995698, 1068751.55125),

            ("Zero symbol portfolio",
             '2011-01-01', '2011-12-31',
             [],
             [],
             0, 252, True, False,
             0, 0, 0, 0, 0),

            ("Backwards dates",
             '2010-12-31', '2010-01-01',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.1],
             0, 252, True, False,
             0, 0, 0, 0, 0),

            ("Allocs don't sum to 1.0",
             '2010-01-01', '2010-12-31',
             ['GOOG', 'AAPL', 'GLD', 'XOM'],
             [0.2, 0.3, 0.4, 0.5],
             0, 252, True, False,
             0, 0, 0, 0, 0),

            ]:

        print description + ":",
        exec_failed = False
        exception_type = ""
        exception_message = ""

        try:
            c_cr, c_adr, c_sddr, c_sr, c_ev = \
                analysis.assess_portfolio(sd=start_date, ed=end_date,
                                          syms=symbols, allocs=allocations,
                                          sv=1000000, rfr=rfr, sf=sf,
                                          gen_plot=gen_plot)
        except Exception as e:
            exec_failed = True
            exception_type = type(e).__name__
            exception_message = e.message

        if exec_failed:
            if should_fail:
                result_msg = "Ok!"
            else:
                result_msg = "***** Bad! ******"
            print "Threw exception " + exception_type + ": " + exception_message + "   " + result_msg
        else:
            if should_fail:
                print "Test was supposed to fail but didn't.  ***** Bad! ******"
            else:
                if np.allclose([c_cr, c_adr, c_sddr, c_sr, c_ev], [v_cr, v_adr, v_sddr, v_sr, v_ev]):
                    print "Correct values returned: Ok!"
                else:
                    print "Incorrect values returned:", \
                        ", ".join([str(x) for x in [c_cr, c_adr, c_sddr, c_sr, c_ev]]), "***** Bad! ******"

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    print "Duration:", duration,
    if duration < datetime.timedelta(seconds=5):
        print "Ok!"
    else:
        print "***** Bad! ******"
