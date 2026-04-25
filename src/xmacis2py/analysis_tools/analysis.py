"""
This file hosts functions that perform various statistical operations on the xmACIS2 Datasets

Analysis Tools:

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
- filter_analog_years
- analog_weighted_mean
- analog_weighted_percentile

(C) Eric J. Drewitz 2025-2026
"""

import warnings as _warnings
import numpy as _np
import os as _os
import pandas as _pd
import math as _math
from scipy import signal as _signal
_warnings.filterwarnings('ignore')

def _round_down(value, to_nearest):
    """
    This function rounds a number down to a specific number of decimal places.
    
    Required Arguments:
    
    1) value (Float) - The value to be rounded.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)  
    
    Returns
    -------
    
    The rounded value as specified.  
    """
    
    if to_nearest < 0:
        raise ValueError("Decimals must be a non-negative integer.")
    factor = 10**to_nearest
    return _math.floor(value * factor) / factor

def _round_up(value,
              to_nearest):
    
    """
    This function rounds up a value.
    
    Required Arguments:
    
    1) value (Float) - The value to be rounded.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)  
    
    Returns
    -------
    
    The rounded value as specified.    
    """
    
    new_value = round(value, to_nearest)
    
    return new_value

def number_of_days_at_value(df,
                            parameter,
                            value):

    """
    This function tallies the number of days in the period at a certain value.

    Required Arguments:

    1) df (Pandas.DataFrame) - The xmaCIS2 dataframe for the period of interest.

    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'

    3) value (String, Integer or Float) - The value the user wants to set as the threshold.

    For precipitation, if the user wants to have all days where at least a trace occurred, enter 'T'.

    Otherwise, this value must be an integer or a floating point type.

    Returns
    -------

    The number of days a value is at a certain value
    """
    try:
        value = value.upper()
    except Exception as e:
        pass

    if value == 'T':
        value = 0.001
    else:
        value = value

    count = 0
    for val in df[parameter]:
        if val == value:
            count = count + 1
        else:
            pass

    return count


def number_of_days_above_value(df,
                               parameter,
                               value):

    """
    This function tallies the number of days in the period above a certain value.

    Required Arguments:

    1) df (Pandas.DataFrame) - The xmaCIS2 dataframe for the period of interest.

    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'

    3) value (String, Integer or Float) - The value the user wants to set as the threshold.

    For precipitation, if the user wants to have all days where at least a trace occurred, enter 'T'.

    Otherwise, this value must be an integer or a floating point type.

    Returns
    -------

    The number of days a value is above a certain value
    """
    try:
        value = value.upper()
    except Exception as e:
        pass

    if value == 'T':
        value = 0.001
    else:
        value = value
        
    count = 0
    for val in df[parameter]:
        if val > value:
            count = count + 1
        else:
            pass

    return count


def number_of_days_below_value(df,
                               parameter,
                               value):

    """
    This function tallies the number of days in the period below a certain value.

    Required Arguments:

    1) df (Pandas.DataFrame) - The xmaCIS2 dataframe for the period of interest.

    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'

    3) value (String, Integer or Float) - The value the user wants to set as the threshold.

    For precipitation, if the user wants to have all days where at least a trace occurred, enter 'T'.

    Otherwise, this value must be an integer or a floating point type.

    Returns
    -------

    The number of days a value is below a certain value
    """
    try:
        value = value.upper()
    except Exception as e:
        pass

    if value == 'T':
        value = 0.001
    else:
        value = value

    count = 0
    for val in df[parameter]:
        if val < value:
            count = count + 1
        else:
            pass

    return count

def number_of_days_at_or_below_value(df,
                               parameter,
                               value):

    """
    This function tallies the number of days in the period at or below a certain value.

    Required Arguments:

    1) df (Pandas.DataFrame) - The xmaCIS2 dataframe for the period of interest.

    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'

    3) value (String, Integer or Float) - The value the user wants to set as the threshold.

    For precipitation, if the user wants to have all days where at least a trace occurred, enter 'T'.

    Otherwise, this value must be an integer or a floating point type.

    Returns
    -------

    The number of days a value is at or below a certain value
    """
    try:
        value = value.upper()
    except Exception as e:
        pass

    if value == 'T':
        value = 0.001
    else:
        value = value

    count = 0
    for val in df[parameter]:
        if val <= value:
            count = count + 1
        else:
            pass

    return count

def number_of_days_at_or_above_value(df,
                                    parameter,
                                    value):

    """
    This function tallies the number of days in the period at or above a certain value.

    Required Arguments:

    1) df (Pandas.DataFrame) - The xmaCIS2 dataframe for the period of interest.

    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'

    3) value (String, Integer or Float) - The value the user wants to set as the threshold.

    For precipitation, if the user wants to have all days where at least a trace occurred, enter 'T'.

    Otherwise, this value must be an integer or a floating point type.

    Returns
    -------

    The number of days a value is at or above a certain value
    """
    try:
        value = value.upper()
    except Exception as e:
        pass

    if value == 'T':
        value = 0.001
    else:
        value = value

    count = 0
    for val in df[parameter]:
        if val >= value:
            count = count + 1
        else:
            pass

    return count

def number_of_missing_days(df,
                           parameter):
    
    """
    This function does the following actions on missing data:
    
    1) Replaces M with NaN.
    
    2) Tallies the amount of missing days in an analysis period.
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'
    
    Optional Arguments: None
    
    Returns
    -------
    
    1) The tally of missing days in an analysis period for a specific parameter.     
    """

    nan_counts = df[parameter].isna().sum()

    nan_counts = int(nan_counts)

    return nan_counts


def period_mean(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period mean for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period mean for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].mean()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
        
        
def period_median(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period median for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period median for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].median()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var

def period_percentile(df,
                    parameter,
                    round_value=False,
                    round_up=True,
                    to_nearest=0,
                    data_type='float',
                    percentile=0.25):
    
    """
    This function finds the period median for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.

    5) percentile (Float) - Default=0.25 (25th Percentile). A value between 0 and 1 that represents the percentile.
        (i.e. 0.25 = 25th percentile, 0.75 = 75th percentile). 
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period user-specified percentile for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].quantile(percentile)
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var

        
def period_standard_deviation(df,
                                parameter,
                                round_value=False,
                                round_up=True,
                                to_nearest=0,
                                data_type='float'):
    
    """
    This function finds the period standard deviation for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period standard deviation for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].std()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
        
        
def period_mode(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period mode for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period mode for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].mode()
    
    modes = len(var)
    
    if modes == 0:
        print("There are zero modes in this dataset")
    elif modes == 1:
        print("There is 1 mode in this dataset")
    else:
        print(f"There are {modes} modes in this dataset")
    
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                try:
                    var = int(var)
                except Exception as e:
                    var = var
            else:
                try:
                    var = float(var)
                except Exception as e:
                    var = var
    return var
        
        
def period_variance(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period variance for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period variance for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].var()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
        
def period_skewness(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period skewness for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period skewness for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].skew()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
        
        
def period_kurtosis(df,
                    parameter,
                    round_value=False,
                    round_up=True,
                    to_nearest=0,
                    data_type='float'):
    
    """
    This function finds the period kurtosis for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period kurtosis for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].kurt()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
        

def period_maximum(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period maximum for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period maximum for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].max()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
        
def period_minimum(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period maximum for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period minimum for the variable of interest.    
    """
    data_type = data_type.lower()
    
    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
    
    var = df[parameter].min()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var


def period_sum(df,
               parameter,
               round_value=False,
               round_up=True,
               to_nearest=0,
               data_type='float'):

    """
    This function finds the period sum for the specified parameter.

    Required Arguments:

    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.

    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
        
    1) round_value (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) round_up (Boolean) - Default=True. When set to True, the value is rounded up. Set round_up=False to round down.
    
    3) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    4) data_type (String) - Default='float'. The data type of the returned data.
        Set data_type='integer' if the user prefers to return an integer type rather than a float type.
    
    Types of Rounding
    -----------------
    
    to_nearest=0 ---> Whole Number
    to_nearest=1 ---> Nearest Tenth (0.1)
    to_nearest=2 ---> Nearest Hundredth (0.01)    

    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'    
    
    Returns
    -------
    
    The period sum for the variable of interest.   
    """
    data_type = data_type.lower()

    try:
        df = df.replace({0.001:_np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, _np.nan, inplace=True)
        
    var = df[parameter].sum()
    if round_value == True:
        if data_type == 'integer':
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if round_up == True:
                var = _round_up(var, to_nearest)
            else:
                var = _round_down(var, to_nearest)
                
            var = float(var)
    else:
        if data_type == 'integer' and type(var) != type(0):
            if round_up == True:
                var = _round_up(var, 0)
            else:
                var = _round_down(var, 0)
            var = int(var)
        else:
            if data_type == 'integer':
                var = int(var)
            else:
                var = float(var)
    return var
   
def period_rankings(df,
                    parameter,
                    ascending=False,
                    rank_subset=None,
                    first=5,
                    last=5,
                    between=[],
                    date_name='Date'):
    
    """
    This function ranks the data for the period. 
    This is useful when asked a question like "What were the top 5 hottest days in the period?"
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) ascending (Boolean) Default=False. The default setting sorts from high to low values.
        To sort from low to high values, set ascending=True.
        
    2) rank_subset (Integer or None) - Default=None. When set to None, there is no subset of the ranked data.
        An example of a rank subset is top 5 hottest days. 
        
        Valid Ranked Subset Entries
        ---------------------------
        
        1) ranked_subset=None
        2) ranked_subset='first'
        3) ranked_subset='last'
        4) ranked_subset='between'
        
        
        Types of ranked subsets:
        
        1) first (Integer) - Default=5. Top x (x=5 in this example) values for the parameter in the period.
        
        2) last (Integer) - Default=5. Bottom x (x=5 in this example) values for the parameter in the period.
        
        3) between (Integer List) - Default=Blank List. If you want to do a custom ranking, you pass the start and end indices in here.
        
            i.e. Let's say I want to rank between 5th and 10th place, I would set between=[5,10].
            
    3) date_name (String) - Default='Date'. The variable name for Date.
            
    Returns
    -------    
    
    A Pandas.DataFrame organized by user specified ranking system.
    """
    
    df = df.sort_values([parameter], ascending=ascending)
    
    if rank_subset == None:
        
        ranked = []
        dates = []
        for i in range(0, len(df[date_name]), 1):
            ranked.append(df[parameter].iloc[i])
            dates.append(df[date_name].iloc[i])
            
        ranked_df = _pd.DataFrame(ranked)
        dates_df = _pd.DataFrame(dates)
        
        df = _pd.DataFrame()
        df[date_name] = dates_df
        df[parameter] = ranked_df
                   
    else:
        
        rank_subset = rank_subset.lower()
        if rank_subset == 'first':
            ranked = []
            dates = []
            for i in range(0, first, 1):
                ranked.append(df[parameter].iloc[i])
                dates.append(_pd.to_datetime(df[date_name].iloc[i]))
                
            ranked_df = _pd.DataFrame(ranked)
            dates_df = _pd.DataFrame(dates)
            
            df = _pd.DataFrame()
            df[date_name] = dates_df
            df[parameter] = ranked_df
                
        elif rank_subset == 'last':
            ranked = []
            dates = []
            nan_count = number_of_missing_days(df,
                                   parameter)

            last = last + nan_count + 1
            last = last * -1
            
            for i in range(-1, last, -1):
                ranked.append(df[parameter].iloc[i])
                dates.append(df[date_name].iloc[i])
                
            ranked_df = _pd.DataFrame(ranked)
            dates_df = _pd.DataFrame(dates)
            
            df = _pd.DataFrame()
            df[date_name] = dates_df
            df[parameter] = ranked_df
            
        else:
            ranked = []
            dates = []
            for i in range(between[0], between[1], 1):
                ranked.append(df[parameter].iloc[i])
                dates.append(df[date_name].iloc[i])
                
            ranked_df = _pd.DataFrame(ranked)
            dates_df = _pd.DataFrame(dates)
            
            df = _pd.DataFrame()
            df[date_name] = dates_df
            df[parameter] = ranked_df  

    df = df.dropna()
            
    return df              
        

def running_sum(df, 
                parameter,
                interpolation_limit=3):

    """
    This function returns a list of the running sum of the data. 

    Required Arguments:

    1) df (Pandas DataFrame)

    2) parameter (String) - The parameter abbreviation. 
    
    Optional Arguments:
    
    1) interpolation_limit (Integer) - Default=3. The maximum amount of consecutive
        missing days of data the user wants to interpolate between.

    Returns
    -------
    
    A list of the running sums
    """

    sums = []
    current_sum = 0
    df = df.interpolate(limit=interpolation_limit)

    for i in range(0, len(df[parameter]), 1):
        current_sum += df[parameter].iloc[i]
        sums.append(current_sum)

    return sums


def running_mean(df, 
                 parameter,
                 interpolation_limit=3):
    
    """
    Calculates the running mean of a dataframe.

    Required Arguments:

    1) df (Pandas DataFrame)

    2) parameter (String) - The parameter abbreviation. 
    
    Optional Arguments:
    
    1) interpolation_limit (Integer) - Default=3. The maximum amount of consecutive
        missing days of data the user wants to interpolate between.    

    Returns
    -------
    
    A list of the running means of the dataframe
    """
    running_sum = 0
    running_means = []
    df = df.interpolate(limit=interpolation_limit)
    
    for i, value in enumerate(df[parameter]):
        running_sum += value
        running_means.append(running_sum / (i + 1))
        
    return running_means

def detrend_data(df,
                 parameter,
                 detrend_type='linear'):
    
    """
    This function detrends the xmACIS2 data for a user specified parameter. 
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of the xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Parameter List
    --------------
    
    'Maximum Temperature'
    'Minimum Temperature'
    'Average Temperature', 
    'Average Temperature Departure'
    'Heating Degree Days'
    'Cooling Degree Days'
    'Precipitation'
    'Snowfall'
    'Snow Depth'
    'Growing Degree Days'
    
    Optional Arguments:
    
    1) detrend_type (String) - Default='linear'. The type of detrending. 
    If type == 'linear' (default), the result of a linear least-squares fit to data is subtracted from data. 
    If type == 'constant', only the mean of data is subtracted.
    
    Returns
    -------
    
    A Pandas.DataFrame of the detrended data for the specific variable.    
    """
    var_name = f"{parameter} Detrended"
    
    count = number_of_missing_days(df,
                           parameter)
    
    if count > 0:
        df = df.interpolate(limit=count)

        df = df.fillna(method='ffill').fillna(method='bfill')
            
        df[var_name] = _signal.detrend(df[parameter], type=detrend_type)
    else:
        df[var_name] = _signal.detrend(df[parameter], type=detrend_type)
    
    return df

def calculate_daily_normals(station,
                            df=None,
                            input_path=None,
                            start_date=None,
                            end_date=None,
                            to_csv=False,
                            output_path=f"XMACIS2 DAILY NORMALS",
                            return_pandas_df=True):
    
    """
    This function calculates daily climatological means for a user-specified period.
    
    This function is useful for those who do not want the day to day fluctuations smoothed out
    as xmACIS2 smooths out the normals (the ones downloaded from the server via get_single_station_climate_normals()).
    
    This is also useful for creating daily climatology normals for a custom period. (i.e. a 50-year climatology)
    
    Required Arguments: 
    
    1) station (String) - The 4-letter ID of the ACIS2 station.
    
    Optional Arguments
    
    1) df (Pandas.DataFrame) - Default=None. If the user is passing in a dataframe (df) without reading in the data from a CSV
        file, set df=df.
        
    2) input_path (String) - Default=None. If the user is reading in data from a CSV file, enter the full path to the
        CSV file.
        
    3) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    4) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    5) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified path.
    
    6) output_path (String) - Default="XMACIS2 DAILY NORMALS". The output directory hosting the CSV file (only needed if to_csv=True).
    
    7) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 
        
    Returns
    -------
    
    A Pandas.DataFrame of daily climatological normals for a custom period.     
    """
    
    if df is not None:
        df = df
    else:
        df = _pd.read_csv(f"{input_path}")
        
    if start_date is not None and end_date is not None:
        df = df.loc[start_date:end_date]
    else:
        pass
    
    df['date'] = _pd.to_datetime(df['Date'])
    
    df = df.groupby(df['date'].dt.dayofyear).agg({
        "Maximum Temperature": "mean",
        "Minimum Temperature": "mean",
        "Average Temperature": "mean",
        "Heating Degree Days": "mean",
        "Cooling Degree Days": "mean",
        "Growing Degree Days": "mean",
        "Precipitation": "mean",
        "Snowfall": "mean",
        "Snow Depth": "mean"
    })
    
    df = df.reset_index().rename(columns={"date": "Day Of Year"})
    
    df['Date'] = _pd.to_datetime(
        df["Day Of Year"] - 1,
        unit="D",
        origin="2000-01-01"
    )
    
    df['Date'] = df['Date'].dt.strftime("%m-%d")
    
    if to_csv == True:
        try:
            _os.makedirs(f"{output_path}")
        except Exception as e:
            pass
        
        df.to_csv(f"{output_path}/{station.upper()}.csv")
        
    else:
        pass
    
    if return_pandas_df == True:
        return df
    else:
        pass
        
        
def filter_analog_years(station,
                        analogs,
                        df=None,
                        input_path=None,
                        to_csv=False,
                        output_path=f"XMACIS2 ANALOGS",
                        return_pandas_df=True):
    
    """
    This function filters for analog periods in the form of month and year. 
    
    This can be useful when wanting to perform an analysis of analog years for seasonal forecasting applications.
    
    Required Arguments: 
    
    1) station (String) - The 4-letter ID of the ACIS2 station.
    
    2) analogs (Tuple List) - A list of tuples that represent the analog periods in the query. 
        Format: [(YYYY 1, mm 1), (YYYY 2, mm2),...., (YYYY n, mm n)]
        Example: Let's query winters 2006, 2016 and 2026
        
        [(2005, 12), (2006, 1), (2006, 2),
        (2015, 12), (2016, 1), (2016, 2),
        (2025, 12), (2026, 1), (2026, 2)]
    
    Optional Arguments
    
    1) df (Pandas.DataFrame) - Default=None. If the user is passing in a dataframe (df) without reading in the data from a CSV
        file, set df=df.
        
    2) input_path (String) - Default=None. If the user is reading in data from a CSV file, enter the full path to the
        CSV file.
    
    3) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified path.
    
    4) output_path (String) - Default="XMACIS2 ANALOGS". The output directory hosting the CSV file (only needed if to_csv=True).
    
    5) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 
        
    Returns
    -------
    
    A Pandas.DataFrame of analog years for years 1-n for a period for months 1-n.     
    """
    
    if df is not None:
        df = df
    else:
        df = _pd.read_csv(f"{input_path}")
        
    df['date'] = _pd.to_datetime(df['Date'])
    df = df.set_index('date')
    pairs = list(zip(df.index.year, df.index.month))

    df = df[[pair in analogs for pair in pairs]].copy()
    
    if to_csv == True:
        try:
            _os.makedirs(f"{output_path}")
        except Exception as e:
            pass
        
        df.to_csv(f"{output_path}/{station.upper()}.csv")
        
    else:
        pass
    
    if return_pandas_df == True:
        return df
    else:
        pass
    

def analog_weighted_mean(df,
                  parameter,
                  weights):
    
    """
    This function calculates the weighted mean for a given variable.
    
    This is useful when wanting to create weighted means of analogs when
    comparing analog years for seasonal forecasting applications.
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The dataframe of ACIS2 data.
    
    2) parameter (String) - The parameter of interest.
    
    3) weights (Float/Integer Array) - An array of numbers (can be both float and int) of the weights applied.
    
    Returns
    -------
    
    The weighted mean of the variable in a Pandas.DataFrame.    
    """
    
    df["Year"] = df.index.to_series().apply(
    lambda d: d.year + 1 if d.month == 12 else d.year
    )
    
    df = df.drop(columns=["Date"])
    means = df.groupby("Year").mean()

    
    weighted_mean = _np.average(
    means[parameter].values,
    axis=0,
    weights=weights
    )
    
    return weighted_mean


def analog_weighted_percentile(df,
                  parameter,
                  weights,
                  percentile):
    
    """
    This function calculates the weighted mean for values of a given percentile.
    
    This is useful when wanting to create weighted means applied to percentile values of analogs when
    comparing analog years for seasonal forecasting applications.
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The dataframe of ACIS2 data.
    
    2) parameter (String) - The parameter of interest.
    
    3) weights (Float/Integer Array) - An array of numbers (can be both float and int) of the weights applied.
    
    4) percentile (Float or Int) - A value between 0 and 1. (0.5 = 50th percentile)
    
    Returns
    -------
    
    The weighted mean of a given percentile of the variable in a Pandas.DataFrame.    
    """
    
    df["Year"] = df.index.to_series().apply(
    lambda d: d.year + 1 if d.month == 12 else d.year
    )
    
    df = df.drop(columns=["Date"])
    percentiles = df.groupby("Year").quantile(percentile)

    
    weighted_percentile = _np.average(
    percentiles[parameter].values,
    axis=0,
    weights=weights
    )
    
    return weighted_percentile
    
    
