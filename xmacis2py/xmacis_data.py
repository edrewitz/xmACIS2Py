import urllib
import requests
import json
import pandas as pd
import numpy as np

try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta


def xmacis_to_csv(station, start_date, end_date):

    r'''
    This function gets the xmACIS2 data for a given station and given period

    Required Arguments: 

    1) station (String) - The identifier for the station in xmACIS2

    2) start_date (datetime array) - The start date of the period

    3) end_date (datetime array) - The end date of the period

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

    params = urllib.parse.urlencode({'params':json.dumps(input_dict)}).encode("utf-8")
    req = urllib.request.Request('http://data.rcc-acis.org/StnData', params, {'Accept':'application/json'})
    response = urllib.request.urlopen(req)
    a = response.read()
    z= json.loads(a)
    b=z["data"]

    df = pd.DataFrame(b,columns=output_cols)

    df = df.replace({'M':np.NaN})

    df = df.dropna()

    df = df.replace('T', 0.00)

    return df, start_date, end_date

def get_means(df):

    means = []
    
    mean_max = df['MAX'].mean()
    mean_min = df['MIN'].mean()
    mean_avg = df['AVG'].mean()
    mean_dep = df['DEP'].mean()
    mean_hdd = df['HDD'].mean()
    mean_cdd = df['CDD'].mean()
    mean_pcp = df['PCP'].mean()
    mean_snw = df['SNW'].mean()
    mean_dpt = df['DPT'].mean()

    mean_max = int(round(mean_max, 0))
    mean_min = int(round(mean_min, 0))
    mean_avg = float(round(mean_avg, 1))
    mean_dep = float(round(mean_dep, 1))
    mean_hdd = int(round(mean_hdd, 0))
    mean_cdd = int(round(mean_cdd, 0))
    mean_pcp = float(round(mean_pcp, 2))
    mean_snw = float(round(mean_snw, 1))
    mean_dpt = int(round(mean_dpt, 0))
    
    means.append(mean_max)
    means.append(mean_min)
    means.append(mean_avg)
    means.append(mean_dep)
    means.append(mean_hdd)
    means.append(mean_cdd)
    means.append(mean_pcp)
    means.append(mean_snw)
    means.append(mean_dpt)
    
    return means

def get_maxima(df):

    maxima = []
    
    max_max = df['MAX'].max()
    max_min = df['MIN'].max()
    max_avg = df['AVG'].max()
    max_dep = df['DEP'].max()
    max_hdd = df['HDD'].max()
    max_cdd = df['CDD'].max()
    max_pcp = df['PCP'].max()
    max_snw = df['SNW'].max()
    max_dpt = df['DPT'].max()

    max_max = int(round(max_max, 0))
    max_min = int(round(max_min, 0))
    max_avg = float(round(max_avg, 1))
    max_dep = float(round(max_dep, 1))
    max_hdd = int(round(max_hdd, 0))
    max_cdd = int(round(max_cdd, 0))
    max_pcp = float(round(max_pcp, 2))
    max_snw = float(round(max_snw, 1))
    max_dpt = int(round(max_dpt, 0))

    maxima.append(max_max)
    maxima.append(max_min)
    maxima.append(max_avg)
    maxima.append(max_dep)
    maxima.append(max_hdd)
    maxima.append(max_cdd)
    maxima.append(max_pcp)
    maxima.append(max_snw)
    maxima.append(max_dpt)
    
    return maxima

def get_minima(df):

    minima = []

    min_max = df['MAX'].min()
    min_min = df['MIN'].min()
    min_avg = df['AVG'].min()
    min_dep = df['DEP'].min()
    min_hdd = df['HDD'].min()
    min_cdd = df['CDD'].min()
    min_pcp = df['PCP'].min()
    min_snw = df['SNW'].min()
    min_dpt = df['DPT'].min()

    min_max = int(round(min_max, 0))
    min_min = int(round(min_min, 0))
    min_avg = float(round(min_avg, 1))
    min_dep = float(round(min_dep, 1))
    min_hdd = int(round(min_hdd, 0))
    min_cdd = int(round(min_cdd, 0))
    min_pcp = float(round(min_pcp, 2))
    min_snw = float(round(min_snw, 1))
    min_dpt = int(round(min_dpt, 0))

    minima.append(min_max)
    minima.append(min_min)
    minima.append(min_avg)
    minima.append(min_dep)
    minima.append(min_hdd)
    minima.append(min_cdd)
    minima.append(min_pcp)
    minima.append(min_snw)
    minima.append(min_dpt)
    
    return minima

def get_sum_hdd_cdd(df):

    hdd = df['HDD'].sum()
    cdd = df['CDD'].sum()

    return hdd, cdd
  