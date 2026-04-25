# xmACIS2Py Analysis Tools

### period_mean()

***def period_mean(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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

### period_median()

***def period_median(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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


### period_mode()

***def period_mode(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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


### period_percentile()

***def period_percentile(df,
                    parameter,
                    round_value=False,
                    round_up=True,
                    to_nearest=0,
                    data_type='float',
                    percentile=0.25):***

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

### period_standard_deviation()

***def period_standard_deviation(df,
                                parameter,
                                round_value=False,
                                round_up=True,
                                to_nearest=0,
                                data_type='float'):***

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


### period_variance()

***def period_variance(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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


### period_skewness()

***period_skewness(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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

### period_kurtosis()

***def period_kurtosis(df,
                    parameter,
                    round_value=False,
                    round_up=True,
                    to_nearest=0,
                    data_type='float'):***

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

### period_maximum()

***def period_maximum(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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


### period_minimum()

***def period_minimum(df,
                parameter,
                round_value=False,
                round_up=True,
                to_nearest=0,
                data_type='float'):***

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


### period_sum()

***def period_sum(df,
               parameter,
               round_value=False,
               round_up=True,
               to_nearest=0,
               data_type='float'):***

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


### period_rankings()

***def period_rankings(df,
                    parameter,
                    ascending=False,
                    rank_subset=None,
                    first=5,
                    last=5,
                    between=[],
                    date_name='Date'):***

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


### running_sum()

***def running_sum(df, 
                parameter,
                interpolation_limit=3):***

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

### running_mean()

***def running_mean(df, 
                 parameter,
                 interpolation_limit=3):***

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


### detrend_data()

***def detrend_data(df,
                 parameter,
                 detrend_type='linear'):***


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

### number_of_missing_days()

***def number_of_missing_days(df,
                           parameter):***

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


### number_of_days_at_or_below_value()

***def number_of_days_at_or_below_value(df,
                               parameter,
                               value):***

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


### number_of_days_at_or_above_value()

***def number_of_days_at_or_above_value(df,
                                    parameter,
                                    value):***

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


### number_of_days_below_value()

***def number_of_days_below_value(df,
                               parameter,
                               value):***

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

### number_of_days_above_value()

***def number_of_days_above_value(df,
                               parameter,
                               value):***

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
    
### number_of_days_at_value()

***def number_of_days_at_value(df,
                            parameter,
                            value):***

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


### calculate_daily_normals()

***def calculate_daily_normals(station,
                            df=None,
                            input_path=None,
                            start_date=None,
                            end_date=None,
                            to_csv=False,
                            output_path=f"XMACIS2 DAILY NORMALS",
                            return_pandas_df=True):***

    This function calculates daily climatological normals for a user-specified period.
    
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


### filter_analog_years()

***def filter_analog_years(station,
                        analogs,
                        df=None,
                        input_path=None,
                        to_csv=False,
                        output_path=f"XMACIS2 ANALOGS",
                        return_pandas_df=True):***


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


### analog_weighted_mean()

***def analog_weighted_mean(df,
                  parameter,
                  weights):***

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


### analog_weighted_percentile()

***def analog_weighted_percentile(df,
                  parameter,
                  weights,
                  percentile):***

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
