"""
This file simplifies the process for xmACIS2Py users to retrieve xmACIS2 data in the form of a Pandas.DataFrame

xmACIS2Py data_access is powered by the xmACIS2 client in the WxData Python Library

For more information on the xmACIS2 Client in the WxData Library, visit: https://pypi.org/project/wxdata/

(C) Eric J. Drewitz 2025-2026
"""

import warnings as _warnings
_warnings.filterwarnings('ignore')
import pandas as _pd
import os as _os
import requests as _requests
# Imports the WxData library
from wxdata import client as _client
from xmacis2py.utils.clean_data import clean_normal_departure_dataframe as _clean_data
from xmacis2py.data_access.exceptions import(
    climo_normals_year_error as _climo_normals_year_error, 
    return_call_counter as _return_call_counter
)
from datetime import(
    datetime as _datetime,
    timedelta as _timedelta
)

_now = _datetime.now()
_yesterday = _now - _timedelta(days=1)
_default_start = _now - _timedelta(days=30)

_year = _yesterday.year
_month = _yesterday.month
_day = _yesterday.day

if _month < 10:
    if _day >= 10:
        _yesterday = f"{_year}-0{_month}-{_day}"
    else:
        _yesterday = f"{_year}-0{_month}-0{_day}"   
else:
    if _day >= 10:
        _yesterday = f"{_year}-{_month}-{_day}"
    else:
        _yesterday = f"{_year}-{_month}-0{_day}" 


def get_single_station_acis_data(station,
            start_date=None,
            end_date=None,
            from_when=_yesterday,
            time_delta=30,
            proxies=None,
            clear_recycle_bin=False,
            to_csv=False,
            path='default',
            filename='default',
            notifications='on',
            return_pandas_df=True):
    
    """
    ***For Single-Station Queries***
    
    This function is a client that downloads user-specified xmACIS2 data and returns a Pandas.DataFrame
    The user can also save the data as a CSV file in a specified location
    This client supports VPN/PROXY connections. 
    
    Required Arguments:
    
    1) station (String) - The 4 letter station ID (i.e. KRAL for Riverside Municipal Airport in Riverside, CA)
    
    Optional Arguments:
    
    1) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    2) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    3) from_when (String or Datetime) - Default=Yesterday. Default value is yesterday's date. 
       Dates can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
       
    4) time_delta (Integer) - Default=30. If from_when is NOT None, time_delta represents how many days IN THE PAST 
       from the time 'from_when.' (e.g. From January 31st back 30 days)
       
    5) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                               'http':'http://your-proxy-address:port',
                               'https':'http://your-proxy-address:port'
                               }
                        
    6) clear_recycle_bin (Boolean) - (Default=False in WxData >= 1.2.5) (Default=True in WxData < 1.2.5). When set to True, 
        the contents in your recycle/trash bin will be deleted with each run of the program you are calling WxData. 
        This setting is to help preserve memory on the machine. 
        
    7) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.
    
    8) path (String) - Default='default'. If set to 'default' the path will be "XMACIS2 DATA/file". Only change if you want to create your 
       directory path.
       
    9) filename (String) - Default='default'. If set to 'default' the filename will be the station ID. Only change if you want a custom
       filename. 
       
    10) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified. 
        
    11) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 
        
    Returns
    -------
    
    A Pandas.DataFrame of the xmACIS2 climate data the user specifies if return_pandas_df = True.
    """
    
    if return_pandas_df == True:
    
        df = _client.get_xmacis_data(station,
                        start_date=start_date,
                        end_date=end_date,
                        from_when=from_when,
                        time_delta=time_delta,
                        proxies=proxies,
                        clear_recycle_bin=clear_recycle_bin,
                        to_csv=to_csv,
                        path=path,
                        filename=filename,
                        notifications=notifications,
                        return_pandas_df=return_pandas_df)
    
        return df
    
    else:
        _client.get_xmacis_data(station,
                        start_date=start_date,
                        end_date=end_date,
                        from_when=from_when,
                        time_delta=time_delta,
                        proxies=proxies,
                        clear_recycle_bin=clear_recycle_bin,
                        to_csv=to_csv,
                        path=path,
                        filename=filename,
                        notifications=notifications,
                        return_pandas_df=return_pandas_df)
        
        
def get_multi_station_acis_data(stations,
                            start_date=None,
                            end_date=None,
                            from_when=_yesterday,
                            time_delta=30,
                            proxies=None,
                            clear_recycle_bin=False,
                            to_csv=False,
                            path='default',
                            filename='default',
                            notifications='on',
                            return_pandas_df=True):
    
    
    """
    ***For Multi-Station Queries***
    
    This function is a client that downloads user-specified xmACIS2 data and returns a Pandas.DataFrame
    The user can also save the data as a CSV file in a specified location
    This client supports VPN/PROXY connections. 
    
    Required Arguments:
    
    1) stations (String) - A list of 4 letter station IDs (i.e. KRAL for Riverside Municipal Airport in Riverside, CA)
    
    Optional Arguments:
    
    1) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    2) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    3) from_when (String or Datetime) - Default=Yesterday. Default value is yesterday's date. 
       Dates can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
       
    4) time_delta (Integer) - Default=30. If from_when is NOT None, time_delta represents how many days IN THE PAST 
       from the time 'from_when.' (e.g. From January 31st back 30 days)
       
    5) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                               'http':'http://your-proxy-address:port',
                               'https':'http://your-proxy-address:port'
                               }
                        
    6) clear_recycle_bin (Boolean) - (Default=False in WxData >= 1.2.5) (Default=True in WxData < 1.2.5). When set to True, 
        the contents in your recycle/trash bin will be deleted with each run of the program you are calling WxData. 
        This setting is to help preserve memory on the machine. 
        
    7) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.
    
    8) path (String) - Default='default'. If set to 'default' the path will be "XMACIS2 DATA/file". Only change if you want to create your 
       directory path.
       
    9) filename (String) - Default='default'. If set to 'default' the filename will be the station ID. Only change if you want a custom
       filename. 
       
    10) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified. 
        
    11) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 
        
    Returns
    -------
    
    A List of Pandas.DataFrames for each station of the xmACIS2 climate data the user specifies if return_pandas_df = True.
    """
    
    df_list = []
    if return_pandas_df == True:
        for station in stations:
            station = station.upper()
        
            df = _client.get_xmacis_data(station,
                            start_date=start_date,
                            end_date=end_date,
                            from_when=from_when,
                            time_delta=time_delta,
                            proxies=proxies,
                            clear_recycle_bin=clear_recycle_bin,
                            to_csv=to_csv,
                            path=path,
                            filename=filename,
                            notifications=notifications,
                            return_pandas_df=return_pandas_df)
            
            df_list.append(df)
                        
        return df_list
        
    else:
        _client.get_xmacis_data(station,
                        start_date=start_date,
                        end_date=end_date,
                        from_when=from_when,
                        time_delta=time_delta,
                        proxies=proxies,
                        clear_recycle_bin=clear_recycle_bin,
                        to_csv=to_csv,
                        path=path,
                        filename=filename,
                        notifications=notifications,
                        return_pandas_df=return_pandas_df)
            
            
def get_single_station_climate_normals(station,
                        interval='daily',
                        start_date=_default_start,
                        end_date=_yesterday,
                        to_csv=False,
                        proxies=None,
                        path=f"XMACIS2 NORMALS",
                        notifications='on',
                        return_pandas_df=True):
    
    """
    ***For Single-Station Queries***
    
    This function is a client that downloads 30-year climate normals for a user-specified ACIS2 station and returns a Pandas.DataFrame
    The user can also save the data as a CSV file in a specified location
    This client supports VPN/PROXY connections. 
    
    Required Arguments:
    
    1) station (String) - The 4 letter station ID (i.e. KRAL for Riverside Municipal Airport in Riverside, CA)
    
    Optional Arguments:
    
    1) interval (String) - Default='daily'. The interval of the climate normals. (daily, monthly, yearly)
    
    2) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    3) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    4) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.

       
    5) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                               'http':'http://your-proxy-address:port',
                               'https':'http://your-proxy-address:port'
                               }
                    
    6) path (String) - Default='default'. If set to 'default' the path will be "XMACIS2 NORMALS/file". Only change if you want to create your 
       directory path.
       
    7) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified. 
        
    8) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 
        
    Returns
    -------
    
    A Pandas.DataFrame of the 30-year climate normals for a user-specified ACIS2 station. 
    """
    url = f"https://data.rcc-acis.org/StnData"
    
    station = station.upper()
    
    interval = interval.lower()
    if interval == 'daily':
        interval = 'dly'
        path_interval = 'DAILY'
    elif interval == 'monthly':
        interval = 'mly'
        path_interval = 'MONTHLY'
    else:
        interval = 'yly'
        path_interval = 'YEARLY'
        
    if type(start_date) != type('a'):
        start_date = f"{start_date.strftime('%Y-%m-%d')}"
    else:
        start_date = start_date
        
    if type(end_date) != type('a'):
        end_date = f"{end_date.strftime('%Y-%m-%d')}"
    else:
        end_date = end_date
        
    syear = int(f"{start_date[0:4]}")
    eyear = int(f"{end_date[0:4]}")
    

    if syear != eyear:
        call = _return_call_counter()
        _climo_normals_year_error(start_date,
                                end_date,
                                path_interval,
                                call)
        syear = eyear
        start_date = f"{syear}-{start_date[6:7]}-{start_date[9:10]}"
    
    payload = {
        "sid": station,
        "sdate": start_date,
        "edate": end_date,
        "elems": [
            {"name": "maxt", "interval": interval, "normal": 1},
            {"name": "mint", "interval": interval, "normal": 1},
            {"name": "avgt", "interval": interval, "normal": 1},
            {"name": "hdd", "interval": interval, "normal": 1},
            {"name": "cdd", "interval": interval, "normal": 1},
            {"name": "gdd", "interval": interval, "normal": 1},
            {"name": "pcpn", "interval": interval, "normal": 1},
            {"name": "snow", "interval": interval, "normal": 1},
        ]
    }
    
    if proxies == None:
        response = _requests.post(url, json=payload)
    else:
        response = _requests.post(url, json=payload, proxies=proxies)
        
    response.raise_for_status()
    data = response.json()
    response.close()
    
    df = _pd.json_normalize(data,
                            record_path=['data'])
    
    col_names = ["Date",
                 "Maximum Temperature", 
                 "Minimum Temperature", 
                 "Average Temperature", 
                 "Heating Degree Days",
                 "Cooling Degree Days",
                 "Growing Degree Days",
                 "Precipitation",
                 "Snowfall"]
    
    df.columns = col_names
    
    df = _clean_data(df)
    
    df['Date'] = _pd.to_datetime(df['Date'])
    
    if to_csv == True:
        path = f"{path}/{path_interval}"
        try:
            _os.makedirs(path)
        except Exception as e:
            pass
        full_path = f"{path}/{station}.csv"
        df.to_csv(f"{full_path}", index=False)
        if notifications == 'on':
            print(f"{station} Data Saved: {full_path}")
    else:
        pass
    
    if return_pandas_df == True:
        return df
    else:
        pass
    

def get_multi_station_climate_normals(stations,
                        interval='daily',
                        start_date=_default_start,
                        end_date=_yesterday,
                        to_csv=False,
                        proxies=None,
                        path=f"XMACIS2 NORMALS",
                        notifications='on',
                        return_pandas_df=True):
    
    """
    ***For Multi-Station Queries***
    
    This function is a client that downloads 30-year climate normals for a user-specified list of ACIS2 station and returns a Pandas.DataFrame
    for each user-specified station.
    The user can also save the data as a CSV file in a specified location
    This client supports VPN/PROXY connections. 
    
    Required Arguments:
    
    1) stations (String List) - A list of 4 letter station IDs (i.e. KRAL for Riverside Municipal Airport in Riverside, CA)
    
    Optional Arguments:
    
    1) interval (String) - Default='daily'. The interval of the climate normals. (daily, monthly, yearly)
    
    2) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    3) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    4) to_csv (Boolean) - Default=False. When set to True, a CSV file of the data will be created and saved to the user specified or default path.

       
    5) proxies (dict or None) - Default=None. If the user is using proxy server(s), the user must change the following:

       proxies=None ---> proxies={
                               'http':'http://your-proxy-address:port',
                               'https':'http://your-proxy-address:port'
                               }
                    
    6) path (String) - Default='default'. If set to 'default' the path will be "XMACIS2 NORMALS/file". Only change if you want to create your 
       directory path.
       
    7) notifications (String) - Default='on'. When set to 'on' a print statement to the user will tell the user their file saved to the path
        they specified. 
        
    8) return_pandas_df (Boolean) - Default=True. When set to True, a pandas.DataFrame is returned.
        To only download CSV files and not return a pandas.DataFrame for each file set to False. 
        
    Returns
    -------
    
    A list of Pandas.DataFrames of 30-year climate normals for each station in the user-specified list of stations. 
    """ 
    
    dfs = []
    if return_pandas_df == True:
        for station in stations:
            df = get_single_station_climate_normals(station,
                        interval=interval,
                        start_date=start_date,
                        end_date=end_date,
                        to_csv=to_csv,
                        proxies=proxies,
                        path=path,
                        notifications=notifications,
                        return_pandas_df=return_pandas_df)
            
            dfs.append(df)
            
        return dfs
    
    else:
        for station in stations:
            get_single_station_climate_normals(station,
                        interval=interval,
                        start_date=start_date,
                        end_date=end_date,
                        to_csv=to_csv,
                        proxies=proxies,
                        path=path,
                        notifications=notifications,
                        return_pandas_df=return_pandas_df)
        

def get_single_station_departures(station,
                        interval='daily',
                        start_date=_default_start,
                        end_date=_yesterday,
                        to_csv=False,
                        proxies=None,
                        path=f"XMACIS2 DEPARTURES",
                        notifications='on',
                        return_pandas_df=True):
    
    """
    This function downloads and returns the 30-year climate normals for a user-specified station at a user-specified interval 
    (i.e. daily, monthly, yearly).
    
    
    
    
    """
    url = f"https://data.rcc-acis.org/StnData"
    
    station = station.upper()
    
    interval = interval.lower()
    if interval == 'daily':
        interval = 'dly'
        path_interval = 'DAILY'
    elif interval == 'monthly':
        interval = 'mly'
        path_interval = 'MONTHLY'
    else:
        interval = 'yly'
        path_interval = 'YEARLY'
        
    if type(start_date) != type('a'):
        start_date = f"{start_date.strftime('%Y-%m-%d')}"
    else:
        start_date = start_date
        
    if type(end_date) != type('a'):
        end_date = f"{end_date.strftime('%Y-%m-%d')}"
    else:
        end_date = end_date
    
    payload = {
        "sid": station,
        "sdate": start_date,
        "edate": end_date,
        "elems": [
            {"name": "maxt", "interval": interval, "normal": "departure"},
            {"name": "mint", "interval": interval, "normal": "departure"},
            {"name": "avgt", "interval": interval, "normal": "departure"},
            {"name": "hdd", "interval": interval, "normal": "departure"},
            {"name": "cdd", "interval": interval, "normal": "departure"},
            {"name": "gdd", "interval": interval, "normal": "departure"},
            {"name": "pcpn", "interval": interval, "normal": "departure"},
            {"name": "snow", "interval": interval, "normal": "departure"},
        ]
    }
    
    if proxies == None:
        response = _requests.post(url, json=payload)
    else:
        response = _requests.post(url, json=payload, proxies=proxies)
        
    response.raise_for_status()
    data = response.json()
    response.close()
    
    df = _pd.json_normalize(data,
                            record_path=['data'])
    
    col_names = ["Date",
                 "Maximum Temperature Departure", 
                 "Minimum Temperature Departure", 
                 "Average Temperature Departure", 
                 "Heating Degree Days Departure",
                 "Cooling Degree Days Departure",
                 "Growing Degree Days Departure",
                 "Precipitation Departure",
                 "Snowfall Departure"]
    
    df.columns = col_names
    
    df = _clean_data(df,
                     departures=True)
    
    df['Date'] = _pd.to_datetime(df['Date'])
    
    if to_csv == True:
        path = f"{path}/{path_interval}"
        try:
            _os.makedirs(path)
        except Exception as e:
            pass
        full_path = f"{path}/{station}.csv"
        df.to_csv(f"{full_path}", index=False)
        if notifications == 'on':
            print(f"{station} Data Saved: {full_path}")
    else:
        pass
    
    if return_pandas_df == True:
        return df
    else:
        pass
    
    
def get_multi_station_departures(stations,
                        interval='daily',
                        start_date=_default_start,
                        end_date=_yesterday,
                        to_csv=False,
                        proxies=None,
                        path=f"XMACIS2 DEPARTURES",
                        notifications='on',
                        return_pandas_df=True):
    
    
    
    df_list = []
    if return_pandas_df == True:
        for station in stations:
            df = get_single_station_departures(station,
                        interval=interval,
                        start_date=start_date,
                        end_date=end_date,
                        to_csv=to_csv,
                        proxies=proxies,
                        path=path,
                        notifications=notifications,
                        return_pandas_df=return_pandas_df)
            
            df_list.append(df)
            
        return df_list
    else:
        for station in stations:
            get_single_station_departures(station,
                            interval=interval,
                            start_date=start_date,
                            end_date=end_date,
                            to_csv=to_csv,
                            proxies=proxies,
                            path=path,
                            notifications=notifications,
                            return_pandas_df=return_pandas_df)