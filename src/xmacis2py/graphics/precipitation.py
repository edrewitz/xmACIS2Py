"""
This file hosts the functions that plot precipitation summaries that have multiple parameters in xmACIS2 Data

(C) Eric J. Drewitz 2025
"""


import xmacis2py.analysis_tools.analysis as analysis
import matplotlib as mpl
import matplotlib.dates as md
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from xmacis2py.utils.file_funcs import update_image_file_paths
from xmacis2py.data_access.get_data import get_data
from matplotlib.ticker import MaxNLocator

try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta

mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['xtick.labelsize'] = 7
mpl.rcParams['ytick.labelsize'] = 7

props = dict(boxstyle='round', facecolor='wheat', alpha=1)
warm = dict(boxstyle='round', facecolor='darkred', alpha=1)
green = dict(boxstyle='round', facecolor='darkgreen', alpha=1)
gray = dict(boxstyle='round', facecolor='gray', alpha=1)
purple = dict(boxstyle='round', facecolor='purple', alpha=1)


try:
    utc = datetime.now(UTC)
except Exception as e:
    utc = datetime.utcnow()
    
today = datetime.now()
yesterday = today - timedelta(days=1)

year = yesterday.year
month = yesterday.month
day = yesterday.day

if month < 10:
    if day >= 10:
        yesterday = f"{year}-0{month}-{day}"
    else:
        yesterday = f"{year}-0{month}-0{day}"   
else:
    if day >= 10:
        yesterday = f"{year}-{month}-{day}"
    else:
        yesterday = f"{year}-{month}-0{day}"   
    
def plot_precipitation_summary(station, 
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
                               only_label_bars_greater_than_0=True):
    
    """
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
    
    Returns
    -------
    
    A graphic showing a precipitation summary of xmACIS2 data.
    """

    mpl.rcParams['font.size'] = bar_label_fontsize

    df = get_data(station,
            start_date=start_date,
            end_date=end_date,
            from_when=from_when,
            time_delta=time_delta,
            proxies=proxies,
            clear_recycle_bin=clear_recycle_bin,
            to_csv=to_csv,
            path=path,
            filename=filename,
            notifications=notifications)

    missing = analysis.number_of_missing_days(df,
                           'Precipitation')
    
    standard_deviation = analysis.period_standard_deviation(df,
                                                    'Precipitation',
                                                    round_value=True,
                                                    to_nearest=2,
                                                    data_type='float')
    
    variance = analysis.period_variance(df,
                                'Precipitation',
                                round_value=True,
                                to_nearest=2,
                                data_type='float')
    
    skewness = analysis.period_skewness(df,
                                'Precipitation',
                                round_value=True,
                                to_nearest=2,
                                data_type='float')
    
    kurtosis = analysis.period_kurtosis(df,
                                'Precipitation',
                                round_value=True,
                                to_nearest=2,
                                data_type='float')
    
    total_precip = analysis.period_sum(df,
                                'Precipitation',
                                round_value=False,
                                to_nearest=2,
                                data_type='float')
    
    top5 = analysis.period_rankings(df,
                            'Precipitation',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = analysis.period_rankings(df,
                            'Precipitation',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Precipitation Summary [IN]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=14, y=0.98, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=False))
    ax.xaxis.set_major_formatter(md.DateFormatter(x_axis_date_format))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    bars = plt.bar(df['Date'], df['Precipitation'], color='green', alpha=0.3)
    if only_label_bars_greater_than_0 == True:
        ax.bar_label(bars, fmt=lambda x: f'{x}' if x > 0 else '', label_type='edge')
    else:
        plt.bar_label(bars)
    if missing == 0:
        ax.text(0.87, 1.01, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.87, 1.01, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.87, 1.01, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    
    if show_running_sum == True:
        run_sum = analysis.running_sum(df, 
                                    'Precipitation',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_sum, 
                            columns=['MEAN'])
        
        ax.set_ylim(0, total_precip + 0.05)
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING SUM')   
    else:
        ax.set_ylim(0, (np.nanmax(df['Precipitation']) + 0.05))
        
    img_path = update_image_file_paths(station, 
                                       product_type, 
                                       'Precipitation Summary', 
                                       show_running_sum,
                                       False,
                                       'No Detrending', 
                                       running_type='Sum')
        
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
        
    if create_ranking_table == True:
        
        plt.axis('off')
        fig = plt.figure(figsize=(12,8))
        fig.set_facecolor('aliceblue')
        
        fig.text(0, 1, f"""Top 5 Days: #1 {top5['Precipitation'].iloc[0]} [IN] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}   #2 {top5['Precipitation'].iloc[1]} [IN] - {top5['Date'].iloc[1].strftime('%m/%d/%Y')}   #3 {top5['Precipitation'].iloc[2]} [IN] - {top5['Date'].iloc[2].strftime('%m/%d/%Y')}   #4 {top5['Precipitation'].iloc[3]} [IN] - {top5['Date'].iloc[3].strftime('%m/%d/%Y')}   #5 {top5['Precipitation'].iloc[4]} [IN] - {top5['Date'].iloc[4].strftime('%m/%d/%Y')}
                                
Standard Deviation: {standard_deviation}   Variance: {variance}   Skewness: {skewness}   Kurtosis: {kurtosis}
                                    
                """, fontsize=14, fontweight='bold', color='white', bbox=green)
        
        fig.text(0, 0.997, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', bbox=props)

    
    fname = f"{station.upper()} Stats Table.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")