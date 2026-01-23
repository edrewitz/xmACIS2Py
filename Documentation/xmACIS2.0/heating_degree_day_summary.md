# Heating Degree Day Summary

***def plot_heating_degree_day_summary(station, 
                               product_type='Heating Degree Days 30 Day Summary',
                               start_date=None,
                                end_date=None,
                                from_when=yesterday,
                                time_delta=30,
                                proxies=None,
                                clear_recycle_bin=False,
                                to_csv=False,
                                path='default',
                                filename='default',
                                notifications='on',
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5,
                               x_axis_date_format='%m/%d',
                               detrend_series=False,
                               detrend_type='linear',
                               create_ranking_table=True,
                               plot_type='bar',
                               shade_anomaly=True):***

    This function plots a graphic showing the Heating Degree Day Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Comprehensive 30 Day Summary'. The type of product. 
    
    2) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    3) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    4) from_when (String or Datetime) - Default=Yesterday. Default value is yesterday's date. 
       Dates can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
       
    5) time_delta (Integer) - Default=30. If from_when is NOT None, time_delta represents how many days IN THE PAST 
       from the time 'from_when.' (e.g. From January 31st back 30 days)
       
    6) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                           'http':'http://url',
                           'https':'https://url'
                        } 
                        
    7) clear_recycle_bin (Boolean) - (Default=False in xmACIS2Py >= 2.2.1) (Default=True in xmACIS2Py < 2.2.1). When set to True, 
        the contents in your recycle/trash bin will be deleted with each run of the program you are calling WxData. 
        This setting is to help preserve memory on the machine. 
        
    8) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.
    
    9) path (String) - Default='default'. If set to 'default' the path will be "XMACIS2 DATA/file". Only change if you want to create your 
       directory path.
       
    10) filename (String) - Default='default'. If set to 'default' the filename will be the station ID. Only change if you want a custom
       filename. 
       
    11) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified. 
    
    12) show_running_means (Boolean) - Default=True. When set to False, running means will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    15) x_axis_date_format (String) - Default='%m/%d'. The datetime format as a string. 
        For more information regarding datetime string formats: https://docs.python.org/3/library/datetime.html#:~:text=Notes-,%25a,-Weekday%20as%20locale%E2%80%99s

    16) detrend_series (Boolean) - Default=False. When set to True, either 'linear' or 'constant' detrending is applied to the dataset.
        Detrending the data removes the seasonality for a variable and is recommended if the user wants to analyze anomalies.
        
    17) detrend_type (String) - Default='linear'. This uses scipy.signal.detrend() to detrend the data and thus remove the signal of seasonality. 
        If type == 'linear' (default), the result of a linear least-squares fit to data is subtracted from data. 
        If type == 'constant', only the mean of data is subtracted.
        
    18) create_ranking_table (Boolean) - Default=True. Creates a table for top 5 and bottom 5 in a second image.
    
    19) plot_type (String) - Default='bar'. Options are 'bar' and 'line'. For long periods (years), a line graph looks better, though for shorter periods (month), 
        a bar graph looks more aesthetic. 
        
    20) shade_anomaly (Boolean) - Default=True. For line plots, users can shade the area under the curve. Set to False to not shade under the curve. 
    
    Returns
    -------
    
    A graphic showing a heating degree day summary of xmACIS2 data saved to {path}.
