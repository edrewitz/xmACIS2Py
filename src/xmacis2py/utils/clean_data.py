"""
This file hosts the functions that clean up the xmACIS2 Pandas.DataFrame to make the data easier to work with. 

(C) Eric J. Drewitz 2025-2026
"""

import pandas as pd
import numpy as np

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
    
    df = df.replace('T', 0.001)
    
    return df

def missing_to_nan(df):
    
    """
    This function does replaces the missing value character 'M' with np.nan (NaN)
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The Pandas.DataFrame of xmACIS2 data.
    
    Optional Arguments: None
    
    Returns
    -------
    
    A Pandas.DataFrame where M is replaced with NaN.
    """
    
    try:
        df = df.replace({'M':np.NaN})
    except Exception as e:
        df = df.infer_objects(copy=False)
        df.replace('M', np.nan, inplace=True)

    return df

def clean_normal_departure_dataframe(df,
                                     departures=False):
    
    """
    This function cleans up the Pandas.DataFrame of the xmACIS2 Data.
    The ingested dataframe has each value as a string - the problem with this is we cannot perform math operations on strings.
    This function converts these strings to integers and floating points.
    
    Required Arguments:
    
    1) df (Pandas.DataFrame) - The dataframe of the xmACIS2 data.
    
    Optional Arguments: 
    
    1) departures (Boolean) - Default=False. Switch to True for departures. 
    
    Returns
    -------
    
    A Pandas.DataFrame with string values converted to integers and floating points.    
    """
    if departures == False:
        cols = ["Maximum Temperature", 
                "Minimum Temperature", 
                "Average Temperature", 
                "Heating Degree Days",
                "Cooling Degree Days",
                "Growing Degree Days",
                "Precipitation",
                "Snowfall"]
        
        
        df = replace_trace_with_zeros(df)
        
        for col in cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        
        df = missing_to_nan(df)
        
        new_df = pd.DataFrame()
        
        new_df['Date'] = df['Date']
        new_df['Maximum Temperature'] = pd.to_numeric(df['Maximum Temperature'])
        new_df['Minimum Temperature'] = pd.to_numeric(df['Minimum Temperature'])
        new_df['Average Temperature'] = pd.to_numeric(df['Average Temperature'])
        new_df['Heating Degree Days'] = pd.to_numeric(df['Heating Degree Days'])
        new_df['Cooling Degree Days'] = pd.to_numeric(df['Cooling Degree Days'])
        new_df['Growing Degree Days'] = pd.to_numeric(df['Growing Degree Days'])
        new_df['Precipitation'] = pd.to_numeric(df['Precipitation'])
        new_df['Snowfall'] = pd.to_numeric(df['Snowfall'])
        
    else:
        cols = ["Maximum Temperature Departure", 
                "Minimum Temperature Departure", 
                "Average Temperature Departure", 
                "Heating Degree Days Departure",
                "Cooling Degree Days Departure",
                "Growing Degree Days Departure",
                "Precipitation Departure",
                "Snowfall Departure"]
        
        
        df = replace_trace_with_zeros(df)
        
        for col in cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        
        df = missing_to_nan(df)
        
        new_df = pd.DataFrame()
        
        new_df['Date'] = df['Date']
        new_df['Maximum Temperature Departure'] = pd.to_numeric(df['Maximum Temperature Departure'])
        new_df['Minimum Temperature Departure'] = pd.to_numeric(df['Minimum Temperature Departure'])
        new_df['Average Temperature Departure'] = pd.to_numeric(df['Average Temperature Departure'])
        new_df['Heating Degree Days Departure'] = pd.to_numeric(df['Heating Degree Days Departure'])
        new_df['Cooling Degree Days Departure'] = pd.to_numeric(df['Cooling Degree Days Departure'])
        new_df['Growing Degree Days Departure'] = pd.to_numeric(df['Growing Degree Days Departure'])
        new_df['Precipitation Departure'] = pd.to_numeric(df['Precipitation Departure'])
        new_df['Snowfall Departure'] = pd.to_numeric(df['Snowfall Departure'])        
    
    return new_df