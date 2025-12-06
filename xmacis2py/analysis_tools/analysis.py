"""
This file hosts functions that perform various statistical operations on the xmACIS2 Datasets

(C) Eric J. Drewitz 2025
"""

import warnings
import numpy as np
import pandas as pd
warnings.filterwarnings('ignore')


def replace_trace_with_zeros(df):
    
    """
    This function replaces trace amounts of precipitation with zeros.
    A trace of precipitation gets counted as zero in climatology. 
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    Optional Arguments: None
    
    Returns
    -------
    
    A Pandas.DataFrame with T replaced by zeros.   
    """
    
    df = df.replace('T', 0.00)
    
    return df

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
    
    1) A Pandas.DataFrame where M is replaced with NaN.
    
    2) The tally of missing days in an analysis period.     
    """
    
    try:
        df = df.replace({'M':np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace('M', np.nan, inplace=True)

    nan_counts = df[parameter].isna().sum()

    return df, nan_counts


def period_mean(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period mean for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].mean()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
        
def period_median(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period median for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].median()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
def period_standard_deviation(df,
                                parameter,
                                round=False,
                                to_nearest=0,
                                data_type='float'):
    
    """
    This function finds the period standard deviation for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].std()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
        
def period_mode(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period mode for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].mode()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
        
def period_variance(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period variance for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].var()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
def period_skewness(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period skewness for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].skew()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
        
def period_kurtosis(df,
                    parameter,
                    round=False,
                    to_nearest=0,
                    data_type='float'):
    
    """
    This function finds the period kurtosis for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].kurt()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        

def period_maximum(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period maximum for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
    
    try:
        var = df[parameter].max()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")
        
def period_minimum(df,
                parameter,
                round=False,
                to_nearest=0,
                data_type='float'):
    
    """
    This function finds the period maximum for the specified parameter
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    2) parameter (String) - The parameter of interest. 
    
    Optional Arguments:
    
    1) round (Boolean) - Default=False. If the user would like to round set round=True.
    
    2) to_nearest (Integer) - Default=0. When to_nearest=0, the returned data is rounded to the nearest whole number.
    
    3) data_type (String) - Default='float'. The data type of the returned data.
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
        var = df[parameter].min()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")


def period_sum(df,
               parameter='Precipitation',
               round=False,
               to_nearest=0,
               data_type='float'):

    """
    This function finds the period sum for the specified parameter.

    Required Arguments:

    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    Optional Arguments:
    
    1) Parameter (String) - Default='Precipitation' Since total precipitation is the most likely
        use for period_sum(), 'Precipitation' is the default value. 
        
    2) round (Boolean) - Default=False. If the user would like to round set round=True.
    
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
        var = df[parameter].sum()
        if round == True:
            if data_type == 'integer':
                var = int(round(var, 0))
            else:
                var = float(round(var, to_nearest))
        else:
            if data_type == 'integer' and type(var) != type(0):
                var = int(round(var, 0))
            else:
                if data_type == 'integer':
                    var = int(var)
                else:
                    var = float(var)
        return var
    except Exception as e:
        print(f"An Error Occurred: {e}")

    
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
                dates.append(df[date_name].iloc[i])
                
            ranked_df = pd.DataFrame(ranked)
            dates_df = pd.DataFrame(dates)
            
            df = pd.DataFrame()
            df[date_name] = dates_df
            df[parameter] = ranked_df
                
        elif rank_subset == 'last':
            ranked = []
            dates = []
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
