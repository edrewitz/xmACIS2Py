# Multi Station Meta-Data

***def multi_station_meta(station_ids,
                        proxies=None,
                        to_csv=False,
                        path=f"XMACIS META",
                        return_pandas_df=True):***

    ***For Multi Station Meta-Data Query***
    
    Required Argument:
    
    station_ids (String List) - A list of the 4-Letter ICAO Station IDs.
    
    Optional Arguments: 
    
    1) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                               'http':'http://your-proxy-address:port',
                               'https':'http://your-proxy-address:port'
                               }
    2) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.
    
    3) path (String) - Default="XMACIS META". If set to 'default' the path will be "XMACIS2 DATA/file". Only change if you want to create your 
       directory path.
       
    4) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 

    5) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified.
    
    Returns
    -------
    
    The meta-data for the specified ACIS2 stations in the form of a Pandas.DataFrame    
