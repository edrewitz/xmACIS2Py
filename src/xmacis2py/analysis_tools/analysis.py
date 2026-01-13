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

(C) Eric J. Drewitz 2025
"""

import warnings
import numpy as np
import pandas as pd
import math
from scipy import signal
warnings.filterwarnings('ignore')

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
    return math.floor(value * factor) / factor

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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
    
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
        df = df.replace({0.001:np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace(0.001, np.nan, inplace=True)
        
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
            
        ranked_df = pd.DataFrame(ranked)
        dates_df = pd.DataFrame(dates)
        
        df = pd.DataFrame()
        df[date_name] = dates_df
        df[parameter] = ranked_df
                   
    else:
        
        rank_subset = rank_subset.lower()
        if rank_subset == 'first':
            ranked = []
            dates = []
            for i in range(0, first, 1):
                ranked.append(df[parameter].iloc[i])
                dates.append(pd.to_datetime(df[date_name].iloc[i]))
                
            ranked_df = pd.DataFrame(ranked)
            dates_df = pd.DataFrame(dates)
            
            df = pd.DataFrame()
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
                
            ranked_df = pd.DataFrame(ranked)
            dates_df = pd.DataFrame(dates)
            
            df = pd.DataFrame()
            df[date_name] = dates_df
            df[parameter] = ranked_df
            
        else:
            ranked = []
            dates = []
            for i in range(between[0], between[1], 1):
                ranked.append(df[parameter].iloc[i])
                dates.append(df[date_name].iloc[i])
                
            ranked_df = pd.DataFrame(ranked)
            dates_df = pd.DataFrame(dates)
            
            df = pd.DataFrame()
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
            
        df[var_name] = signal.detrend(df[parameter], type=detrend_type)
    else:
        df[var_name] = signal.detrend(df[parameter], type=detrend_type)
    
    return df
