# Precipitation Summary

***def plot_precipitation_summary(station, 
                               product_type='Precipitation 30 Day Summary',
                               start_date=None,
                                end_date=None,
                                from_when=yesterday,
                                time_delta=30,
                                proxies=None,
                                clear_recycle_bin=True,
                                to_csv=False,
                                path='default',
                                filename='default',
                                notifications='on',
                               show_running_sum=False,
                               interpolation_limit=3,
                               x_axis_day_interval=5,
                               x_axis_date_format='%m/%d',
                               create_ranking_table=True,
                               bar_label_fontsize=6,
                               only_label_bars_greater_than_0=True,
                               hide_bar_labels=False):***

    This function plots a graphic showing the Precipitation Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Precipitation 30 Day Summary'. The type of product. 
    
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
                        
    7) clear_recycle_bin (Boolean) - Default=True. When set to True, the contents in your recycle/trash bin will be deleted with each run
        of the program you are calling WxData. This setting is to help preserve memory on the machine. 
        
    8) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.
    
    9) path (String) - Default='default'. If set to 'default' the path will be "XMACIS2 DATA/file". Only change if you want to create your 
       directory path.
       
    10) filename (String) - Default='default'. If set to 'default' the filename will be the station ID. Only change if you want a custom
       filename. 
       
    11) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified. 
    
    12) show_running_sum (Boolean) - Default=True. When set to False, running sum will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    15) x_axis_date_format (String) - Default='%m/%d'. The datetime format as a string. 
        For more information regarding datetime string formats: https://docs.python.org/3/library/datetime.html#:~:text=Notes-,%25a,-Weekday%20as%20locale%E2%80%99s
    
    16) create_ranking_table (Boolean) - Default=True. Creates a table for top 5 values in second image.
    
    17) bar_label_fontsize (Integer) - Default=6. The fontsize of the precipitation values on the top of each bar. 
    
    18) only_label_bars_greater_than_0 (Boolean) - Default=True. When set to True, only columns with non-zero values are labeled. 
    
    19) hide_bar_labels (Boolean) - Default=False. To hide the bar labels, set to True. This is useful for users who do not want to 
        display the precipitation amounts on top of each bar and only want the graph without the labels to reduce potential clutter.
    
    Returns
    -------
    
    A graphic showing a precipitation summary of xmACIS2 data saved to {path}.
