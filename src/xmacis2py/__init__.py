"""
xmACIS2Py is a Python package that performs various statistical operations on ACIS2 Climate Data.

xmACIS2Py also is a graphics library of various different xmACIS2 stat graphics.

xmACIS2Py is powered by the xmACIS2 client in the WxData Python Library

For more information on the xmACIS2 Client in the WxData Library, visit: https://pypi.org/project/wxdata/

(C) Eric J. Drewitz 2025-2026
"""


# This is the module to create xmACIS2 temperature graphics
import xmacis2py.graphics.temperature as temperature

# This is the module to create xmACIS2 precipitation graphics
import xmacis2py.graphics.precipitation as precipitation

# ACIS2 Data Access
# - Single ACIS Station
# - Multi ACIS Station
from xmacis2py.data_access.station_data import(
    get_single_station_acis_data,
    get_multi_station_acis_data,
    get_single_station_climate_normals,
    get_multi_station_climate_normals,
    get_single_station_departures,
    get_multi_station_departures
)

# ACIS2 Station Meta-Data
# - Single Station
# - Multi Station
from xmacis2py.data_access.station_meta import (
    single_station_meta,
    multi_station_meta
)


"""
Module
-------

xmacis2py.analysis_tools.analysis

Functions:
- number_of_days_at_value
- number_of_days_above_value
- number_of_days_below_value
- number_of_days_at_or_below_value
- number_of_days_at_or_above_value
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
- calculate_daily_normals
"""
import xmacis2py.analysis_tools.analysis as analysis