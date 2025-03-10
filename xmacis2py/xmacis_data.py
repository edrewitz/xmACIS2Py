import urllib
import requests
import json
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta


def xmacis_to_df(station, start_date, end_date, parameter):

    r'''
    This function gets the xmACIS2 data for a given station and given period

    Required Arguments: 

    1) station (String) - The identifier for the station in xmACIS2

    2) start_date (datetime array) - The start date of the period

    3) end_date (datetime array) - The end date of the period

    4) parameter (String) - The parameter the user wishes to query

    '''

    station = station.upper()
    start_date = start_date
    end_date = end_date    

    if type(start_date) != type('String'):
        syear = str(start_date.year)
        smonth = str(start_date.month)
        sday = str(start_date.day)
        start_date = f"{syear}-{smonth}-{sday}"
    else:
        pass
    if type(end_date) != type('String'):
        eyear = str(end_date.year)
        emonth = str(end_date.month)
        eday = str(end_date.day)
        end_date = f"{eyear}-{emonth}-{eday}"
    else:
        pass


    input_dict = {"elems":["maxt","mint","avgt",{"name":"avgt","normal":"departure"},"hdd","cdd","pcpn","snow","snwd"],"sid":station,"sdate":start_date,"edate":end_date}
    output_cols = ['DATE','MAX','MIN','AVG','DEP','HDD','CDD','PCP','SNW','DPT']

    try:
        params = urllib.parse.urlencode({'params':json.dumps(input_dict)}).encode("utf-8")
        req = urllib.request.Request('http://data.rcc-acis.org/StnData', params, {'Accept':'application/json'})
        response = urllib.request.urlopen(req)
        a = response.read()
        z= json.loads(a)
        b=z["data"]
    
        df = pd.DataFrame(b,columns=output_cols)

        try:
            df = df.replace({'M':np.NaN})
        except Exception as e:
            df = df.infer_objects(copy=False)
            df.replace('M', np.nan, inplace=True)

        if parameter != 'PCP':
            nan_counts = df['AVG'].isna().sum()
        else:
            nan_counts = df['PCP'].isna().sum()

        df = df.replace('T', 0.00)
    
        return df, start_date, end_date, nan_counts

    except Exception as e:
        print(f"{station} is not found in xmACIS2. Please try again with a different station.")

def get_means(df):

    r'''
    This function calculates the means in the dataframe

    Required Arguments:

    1) df (Pandas DataFrame) 

    Returns: The means of each parameter's dataframe

    '''

    means = []
    
    try:
        mean_max = df['MAX'].mean()
    except Exception as e:
        pass
    try:
        mean_min = df['MIN'].mean()
    except Exception as e:
        pass
    try:
        mean_avg = df['AVG'].mean()
    except Exception as e:
        pass
    try:
        mean_dep = df['DEP'].mean()
    except Exception as e:
        pass
    try:
        mean_hdd = df['HDD'].mean()
    except Exception as e:
        pass
    try:
        mean_cdd = df['CDD'].mean()
    except Exception as e:
        pass
    try:
        mean_pcp = df['PCP'].mean()
    except Exception as e:
        pass
    try:
        mean_snw = df['SNW'].mean()
    except Exception as e:
        pass
    try:
        mean_dpt = df['DPT'].mean()
    except Exception as e:
        pass

    try:
        mean_max = int(round(mean_max, 0))
    except Exception as e:
        pass
    try:
        mean_min = int(round(mean_min, 0))
    except Exception as e:
        pass
    try:
        mean_avg = float(round(mean_avg, 1))
    except Exception as e:
        pass
    try:
        mean_dep = float(round(mean_dep, 1))
    except Exception as e:
        pass
    try:
        mean_hdd = int(round(mean_hdd, 0))
    except Exception as e:
        pass
    try:
        mean_cdd = int(round(mean_cdd, 0))
    except Exception as e:
        pass
    try:
        mean_pcp = float(round(mean_pcp, 2))
    except Exception as e:
        pass
    try:
        mean_snw = float(round(mean_snw, 1))
    except Exception as e:
        pass
    try:
        mean_dpt = int(round(mean_dpt, 0))
    except Exception as e:
        pass

    try:
        means.append(mean_max)
    except Exception as e:
        pass
    try:
        means.append(mean_min)
    except Exception as e:
        pass
    try:
        means.append(mean_avg)
    except Exception as e:
        pass
    try:
        means.append(mean_dep)
    except Exception as e:
        pass
    try:
        means.append(mean_hdd)
    except Exception as e:
        pass
    try:
        means.append(mean_cdd)
    except Exception as e:
        pass
    try:
        means.append(mean_pcp)
    except Exception as e:
        pass
    try:
        means.append(mean_snw)
    except Exception as e:
        pass
    try:
        means.append(mean_dpt)
    except Exception as e:
        pass
    
    return means

def get_maxima(df):

    r'''
    This function finds the maxima in the dataframe

    Required Arguments:

    1) df (Pandas DataFrame) 

    Returns: The maxima of each parameter's dataframe

    '''

    maxima = []
    
    try:
        max_max = df['MAX'].max()
    except Exception as e:
        pass
    try:
        max_min = df['MIN'].max()
    except Exception as e:
        pass
    try:
        max_avg = df['AVG'].max()
    except Exception as e:
        pass
    try:
        max_dep = df['DEP'].max()
    except Exception as e:
        pass
    try:
        max_hdd = df['HDD'].max()
    except Exception as e:
        pass
    try:
        max_cdd = df['CDD'].max()
    except Exception as e:
        pass
    try:
        max_pcp = df['PCP'].max()
    except Exception as e:
        pass
    try:
        max_snw = df['SNW'].max()
    except Exception as e:
        pass
    try:
        max_dpt = df['DPT'].max()
    except Exception as e:
        pass

    try:
        max_max = int(round(max_max, 0))
    except Exception as e:
        pass
    try:
        max_min = int(round(max_min, 0))
    except Exception as e:
        pass
    try:
        max_avg = float(round(max_avg, 1))
    except Exception as e:
        pass
    try:
        max_dep = float(round(max_dep, 1))
    except Exception as e:
        pass
    try:
        max_hdd = int(round(max_hdd, 0))
    except Exception as e:
        pass
    try:
        max_cdd = int(round(max_cdd, 0))
    except Exception as e:
        pass
    try:
        max_pcp = float(round(max_pcp, 2))
    except Exception as e:
        pass
    try:
        max_snw = float(round(max_snw, 1))
    except Exception as e:
        pass
    try:
        max_dpt = int(round(max_dpt, 0))
    except Exception as e:
        pass

    try:
        maxima.append(max_max)
    except Exception as e:
        pass
    try:
        maxima.append(max_min)
    except Exception as e:
        pass
    try:
        maxima.append(max_avg)
    except Exception as e:
        pass
    try:
        maxima.append(max_dep)
    except Exception as e:
        pass
    try:
        maxima.append(max_hdd)
    except Exception as e:
        pass
    try:
        maxima.append(max_cdd)
    except Exception as e:
        pass
    try:
        maxima.append(max_pcp)
    except Exception as e:
        pass
    try:
        maxima.append(max_snw)
    except Exception as e:
        pass
    try:
        maxima.append(max_dpt)
    except Exception as e:
        pass
    
    return maxima

def get_minima(df):

    r'''
    This function finds the minima in the dataframe

    Required Arguments:

    1) df (Pandas DataFrame) 

    Returns: The minima of each parameter's dataframe

    '''

    minima = []

    try:
        min_max = df['MAX'].min()
    except Exception as e:
        pass
    try:
        min_min = df['MIN'].min()
    except Exception as e:
        pass
    try:
        min_avg = df['AVG'].min()
    except Exception as e:
        pass
    try:
        min_dep = df['DEP'].min()
    except Exception as e:
        pass
    try:
        min_hdd = df['HDD'].min()
    except Exception as e:
        pass
    try:
        min_cdd = df['CDD'].min()
    except Exception as e:
        pass
    try:
        min_pcp = df['PCP'].min()
    except Exception as e:
        pass
    try:
        min_snw = df['SNW'].min()
    except Exception as e:
        pass
    try:
        min_dpt = df['DPT'].min()
    except Exception as e:
        pass

    try:
        min_max = int(round(min_max, 0))
    except Exception as e:
        pass
    try:
        min_min = int(round(min_min, 0))
    except Exception as e:
        pass
    try:
        min_avg = float(round(min_avg, 1))
    except Exception as e:
        pass
    try:
        min_dep = float(round(min_dep, 1))
    except Exception as e:
        pass
    try:
        min_hdd = int(round(min_hdd, 0))
    except Exception as e:
        pass
    try:
        min_cdd = int(round(min_cdd, 0))
    except Exception as e:
        pass
    try:
        min_pcp = float(round(min_pcp, 2))
    except Exception as e:
        pass
    try:
        min_snw = float(round(min_snw, 1))
    except Exception as e:
        pass
    try:
        min_dpt = int(round(min_dpt, 0))
    except Exception as e:
        pass

    try:
        minima.append(min_max)
    except Exception as e:
        pass
    try:
        minima.append(min_min)
    except Exception as e:
        pass
    try:
        minima.append(min_avg)
    except Exception as e:
        pass
    try:
        minima.append(min_dep)
    except Exception as e:
        pass
    try:
        minima.append(min_hdd)
    except Exception as e:
        pass
    try:
        minima.append(min_cdd)
    except Exception as e:
        pass
    try:
        minima.append(min_pcp)
    except Exception as e:
        pass
    try:
        minima.append(min_snw)
    except Exception as e:
        pass
    try:
        minima.append(min_dpt)
    except Exception as e:
        pass
    
    return minima

def get_sum_hdd_cdd(df):

    r'''
    This function finds the sums of the heating and cooling degree days dataframes. 

    Required Arguments:

    1) df (Pandas DataFrame) 

    Returns: The sum of each parameter's dataframe

    '''

    try:
        hdd = df['HDD'].sum()
    except Exception as e:
        pass
    try:
        cdd = df['CDD'].sum()
    except Exception as e:
        pass

    return hdd, cdd

def get_precipitation_sum(df):

    r'''
    This function finds the sums of precipitation in the dataframe 

    Required Arguments:

    1) df (Pandas DataFrame) 

    Returns: The precipitation sum

    '''

    try:
        precip_sum = df['PCP'].sum()
    except Exception as e:
        pass

    return precip_sum


def rank_top_5(df, parameter):

    r'''
    This function will rank the top 5 days and totals for a given parameter in the analysis period.

    Required Arguments:

    1) df (Pandas DataFrame)

    2) parameter (String) - The parameter the user wishes to query. 

    Returns: Top 5 days and totals for a given parameter
    '''

    top_5 = []
    dates = []
    
    df = df.sort_values([parameter], ascending=False)
    rank_1 = df[parameter].iloc[0]
    rank_2 = df[parameter].iloc[1]
    rank_3 = df[parameter].iloc[2]
    rank_4 = df[parameter].iloc[3]
    rank_5 = df[parameter].iloc[4]

    date_1 = df['DATE'].iloc[0]
    date_2 = df['DATE'].iloc[1]
    date_3 = df['DATE'].iloc[2]
    date_4 = df['DATE'].iloc[3]
    date_5 = df['DATE'].iloc[4]

    top_5.append(rank_1)
    top_5.append(rank_2)
    top_5.append(rank_3)
    top_5.append(rank_4)
    top_5.append(rank_5)

    dates.append(date_1)
    dates.append(date_2)
    dates.append(date_3)
    dates.append(date_4)
    dates.append(date_5)
        

    return top_5, dates
    

def rank_bottom_5(df, parameter):

    r'''
    This function will rank the bottom 5 days and totals for a given parameter in the analysis period.

    Required Arguments:

    1) df (Pandas DataFrame)

    2) parameter (String) - The parameter the user wishes to query. 

    Returns: Bottom 5 days and totals for a given parameter
    '''

    bottom_5 = []
    dates = []
    
    df = df.sort_values([parameter], ascending=True)
    rank_1 = df[parameter].iloc[0]
    rank_2 = df[parameter].iloc[1]
    rank_3 = df[parameter].iloc[2]
    rank_4 = df[parameter].iloc[3]
    rank_5 = df[parameter].iloc[4]

    date_1 = df['DATE'].iloc[0]
    date_2 = df['DATE'].iloc[1]
    date_3 = df['DATE'].iloc[2]
    date_4 = df['DATE'].iloc[3]
    date_5 = df['DATE'].iloc[4]

    bottom_5.append(rank_1)
    bottom_5.append(rank_2)
    bottom_5.append(rank_3)
    bottom_5.append(rank_4)
    bottom_5.append(rank_5)

    dates.append(date_1)
    dates.append(date_2)
    dates.append(date_3)
    dates.append(date_4)
    dates.append(date_5)

    return bottom_5, dates











    
  
