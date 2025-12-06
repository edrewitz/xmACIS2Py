"""
xmACIS2Py is a Python package that performs various statistical operations on ACIS2 Climate Data.

xmACIS2Py also is a graphics library of various different xmACIS2 stat graphics.

xmACIS2Py is powered by the xmACIS2 client in the WxData Python Library

For more information on the xmACIS2 Client in the WxData Library, visit: https://pypi.org/project/wxdata/

(C) Eric J. Drewitz 2025
"""






# This is our data access (powered by WxData)
from xmacis2py.data_access.get_data import get_data

# This consists of all the analysis tools in xmACIS2Py
from xmacis2py.analysis_tools.analysis import *