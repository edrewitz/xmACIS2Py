"""
This file hosts the function that download and returns a station's meta-data for an ACIS2 station.

(C) Eric J. Drewitz 2025-2026
"""

import requests as _requests
import pandas as _pd
import os as _os

def single_station_meta(station_id,
                        proxies=None,
                        to_csv=False,
                        path=f"XMACIS META",
                        return_pandas_df=True,
                        notifications='on'):
    
    """
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
    """
    
    url = "https://data.rcc-acis.org/StnMeta"

    payload = {
        "sids": station_id.upper(),                
        "meta": ["name", "state", "sids", "ll", "elev"]
    }

    if proxies == None:
        response = _requests.post(url, json=payload)
    else:
        response = _requests.post(url, json=payload, proxies=proxies)
    response.raise_for_status()
    data = response.json()
    response.close()
    
    df = _pd.json_normalize(data,
                      record_path=['meta'])
    
    sid = df['sids'].iloc[0][2]
    sid = f"{sid[0:4]}"
    lat = df['ll'].iloc[0][1]
    lon = df['ll'].iloc[0][0]
    state = df['state'].iloc[0]
    name = df['name'].iloc[0]
    elev = df['elev'].iloc[0]
    df['Station ID'] = sid
    df['Station Name'] = name
    df['Station Elevation (ft)'] = elev
    df['State'] = state
    df['Latitude'] = lat
    df['Longitude'] = lon
    
    df = df.drop(columns=["state", "sids", "ll", "elev", "name"])
    
    if to_csv == False:
        pass
    else:
        try:
            _os.makedirs(f"{path}")
        except Exception as e:
            pass
        filename = f"{station_id.upper()}.csv"
        df.to_csv(f"{path}/{filename}", index=False)
        if notifications.lower() == 'on':
            print(f"{filename} saved to {path}")
        
    if return_pandas_df == True:
        return df
    else:
        pass
    
    
def multi_station_meta(station_ids,
                        proxies=None,
                        to_csv=False,
                        path=f"XMACIS META",
                        return_pandas_df=True,
                        notifications='on'):
    
    """
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
    """

    if return_pandas_df == True:
        df_list = []
        for station in station_ids:
            station = station.upper()
            try:
                df = single_station_meta(station,
                            proxies=proxies,
                            to_csv=to_csv,
                            path=path,
                            return_pandas_df=return_pandas_df,
                            notifications=notifications)
                
                df_list.append(df)
            except Exception as e:
              pass
            
        df = _pd.concat(df_list, ignore_index=True)
        
        return df
        
    else:
        for station in station_ids:
            station = station.upper()
            single_station_meta(station,
                        proxies=proxies,
                        to_csv=to_csv,
                        path=path,
                        return_pandas_df=return_pandas_df,
                        notifications=notifications)
