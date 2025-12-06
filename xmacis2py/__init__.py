"""
xmACIS2Py is a Python package that performs various statistical operations on ACIS2 Climate Data.

xmACIS2Py also is a graphics library of various different xmACIS2 stat graphics.

xmACIS2Py is powered by the xmACIS2 client in the WxData Python Library

For more information on the xmACIS2 Client in the WxData Library, visit: https://pypi.org/project/wxdata/

(C) Eric J. Drewitz 2025
"""






# This is our data access (powered by WxData)
from xmacis2py.data_access.get_data import get_data

"""
Module
-------

xmacis2py.analysis_tools.analysis

Analysis Tools:
- replace_trace_with_zeros
- number_of_missing_days
- period_mean
- period_median
- period_standard_deviation
- period_mode
- period_variance
- period_skewness
- period_kurtosis
- period_maximum
- period_minimum
- period_sum
- period_rankings
- running_sum
- running_mean
"""
from xmacis2py.analysis_tools.analysis import *