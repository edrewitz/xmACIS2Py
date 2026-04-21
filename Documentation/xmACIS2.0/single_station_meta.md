# Single Station Meta-Data

***def single_station_meta(station_id,
                        proxies=None,
                        to_csv=False,
                        path=f"XMACIS META",
                        return_pandas_df=True):***

    ***For Single Station Meta-Data Query***
    
    Required Argument:
    
    station_id (String) - The 4-Letter ICAO Station ID.
    
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
    
    The meta-data for an ACIS2 station in the form of a Pandas.DataFrame 
