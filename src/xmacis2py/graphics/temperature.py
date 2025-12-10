"""
This file hosts the functions that plot temperature summaries that have multiple parameters in xmACIS2 Data

(C) Eric J. Drewitz 2025
"""



import matplotlib as mpl
import matplotlib.dates as md
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

from xmacis2py.utils.file_funcs import update_image_file_paths
from xmacis2py.data_access.get_data import get_data
from xmacis2py.analysis_tools import *

from matplotlib.ticker import MaxNLocator

try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta

mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['xtick.labelsize'] = 7
mpl.rcParams['ytick.labelsize'] = 7
mpl.rcParams['font.size'] = 6

props = dict(boxstyle='round', facecolor='wheat', alpha=1)
warm = dict(boxstyle='round', facecolor='darkred', alpha=1)
cool = dict(boxstyle='round', facecolor='darkblue', alpha=1)
green = dict(boxstyle='round', facecolor='darkgreen', alpha=1)
gray = dict(boxstyle='round', facecolor='gray', alpha=1)
purple = dict(boxstyle='round', facecolor='purple', alpha=1)
orange = dict(boxstyle='round', facecolor='darkorange', alpha=1)

try:
    utc = datetime.now(UTC)
except Exception as e:
    utc = datetime.utcnow()
    
today = datetime.now()
yesterday = today - timedelta(days=1)

year = yesterday.year
month = yesterday.month
day = yesterday.day

if day >= 10:
    yesterday = f"{year}-{month}-{day}"
else:
    yesterday = f"{year}-{month}-0{day}"
    
def plot_comprehensive_summary(station, 
                               product_type='Comprehensive 30 Day Summary',
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
                               show_running_means=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):

    """
    This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

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
                        
    7) clear_recycle_bin (Boolean) - Default=True. When set to True, the contents in your recycle/trash bin will be deleted with each run
        of the program you are calling WxData. This setting is to help preserve memory on the machine. 
        
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
    
    Returns
    -------
    
    A graphic showing a comprehensive temperature summary of xmACIS2 data.
    """

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

    maxt_missing = number_of_missing_days(df,
                           'Maximum Temperature')
    mint_missing = number_of_missing_days(df,
                           'Minimum Temperature')
    avgt_missing = number_of_missing_days(df,
                           'Average Temperature')
    avgtdep_missing = number_of_missing_days(df,
                           'Average Temperature Departure')
    hdd_missing = number_of_missing_days(df,
                           'Heating Degree Days')
    cdd_missing = number_of_missing_days(df,
                           'Cooling Degree Days')
    gdd_missing = number_of_missing_days(df,
                           'Growing Degree Days')
    
    days_missing = [maxt_missing,
                    mint_missing,
                    avgt_missing,
                    avgtdep_missing,
                    hdd_missing,
                    cdd_missing,
                    gdd_missing]
    
    missing_days = max(days_missing)
    
    
    max_max_t = period_maximum(df,
                'Maximum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean_max_t = period_mean(df,
                'Maximum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    min_max_t = period_minimum(df,
                'Maximum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    max_min_t = period_maximum(df,
                'Minimum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean_min_t = period_mean(df,
                'Minimum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    min_min_t = period_minimum(df,
                'Minimum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    max_avg_t = period_maximum(df,
                'Average Temperature',
                round_value=True,
                to_nearest=1,
                data_type='float')
    
    mean_avg_t = period_mean(df,
                'Average Temperature',
                round_value=True,
                to_nearest=1,
                data_type='float')
    
    min_avg_t = period_minimum(df,
                'Average Temperature',
                round_value=True,
                to_nearest=1,
                data_type='float')
    
    max_dep_t = period_maximum(df,
                'Average Temperature Departure',
                round_value=True,
                to_nearest=1,
                data_type='float')
    
    min_dep_t = period_minimum(df,
                'Average Temperature Departure',
                round_value=True,
                to_nearest=1,
                data_type='float')
    
    
    mean_gdd = period_mean(df,
                'Growing Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    hdd_sum = period_sum(df,
                        'Heating Degree Days',
                        data_type='integer')
    
    cdd_sum = period_sum(df,
                        'Cooling Degree Days',
                        data_type='integer')
    
    
    fig = plt.figure(figsize=(14,12))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Temperature Summary\nPeriod Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, y=1.0, fontweight='bold', bbox=props)
    ax1 = fig.add_subplot(6, 1, 1)
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.set_ylim((np.nanmin(df['Maximum Temperature']) - 5), (np.nanmax(df['Maximum Temperature']) + 5))
    ax1.set_title(f"Maximum Temperature [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.915, fontsize=5, bbox=warm)
    ax1.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax1.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax1.bar(df['Date'], df['Maximum Temperature'], color='red', zorder=1, alpha=0.3)
    if missing_days == 0:
        ax1.text(0.37, 1.27, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', color='white', transform=ax1.transAxes, bbox=green)
    elif missing_days > 0 and missing_days < 5:
        ax1.text(0.37, 1.27, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', color='white', transform=ax1.transAxes, bbox=warm)
    else:
        ax1.text(0.37, 1.27, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', color='white', transform=ax1.transAxes, bbox=purple)
    ax1.text(0.0008, 1.05, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax1.transAxes, bbox=props)
    ax1.axhline(y=max_max_t, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax1.axhline(y=mean_max_t, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax1.axhline(y=min_max_t, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax1.legend(loc=(0.5, 1.17))
    
    ax2 = fig.add_subplot(6, 1, 2)
    ax2.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.set_ylim((np.nanmin(df['Minimum Temperature']) - 5), (np.nanmax(df['Minimum Temperature']) + 5))
    ax2.set_title(f"Minimum Temperature [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.915, fontsize=5, bbox=cool)
    ax2.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax2.bar(df['Date'], df['Minimum Temperature'], color='blue', zorder=1, alpha=0.3)
    ax2.axhline(y=max_min_t, color='darkred', linestyle='--', zorder=3)
    ax2.axhline(y=mean_min_t, color='dimgrey', linestyle='--', zorder=3)
    ax2.axhline(y=min_min_t, color='darkblue', linestyle='--', zorder=3)
    
    ax3 = fig.add_subplot(6, 1, 3)
    ax3.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax3.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax3.set_ylim((np.nanmin(df['Average Temperature']) - 5), (np.nanmax(df['Average Temperature']) + 5))
    ax3.set_title(f"Average Temperature [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.915, fontsize=5, bbox=gray)
    ax3.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax3.bar(df['Date'], df['Average Temperature'], color='black', zorder=1, alpha=0.3)
    ax3.axhline(y=max_avg_t, color='darkred', linestyle='--', zorder=3)
    ax3.axhline(y=mean_avg_t, color='dimgrey', linestyle='--', zorder=3)
    ax3.axhline(y=min_avg_t, color='darkblue', linestyle='--', zorder=3)
    
    ax4 = fig.add_subplot(6, 1, 4)
    ax4.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax4.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax4.set_ylim((np.nanmin(df['Average Temperature Departure']) - 5), (np.nanmax(df['Average Temperature Departure']) + 5))
    ax4.set_title(f"Average Temperature Departure [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.915, fontsize=5, bbox=gray)
    ax4.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax4.bar(df['Date'], df['Average Temperature Departure'], color='black', zorder=1, alpha=0.3)
    ax4.axhline(y=max_dep_t, color='darkred', linestyle='--', zorder=3)
    ax4.axhline(y=min_dep_t, color='darkblue', linestyle='--', zorder=3)
    ax4.axhline(y=0, color='black', linestyle='-', zorder=3)
    
    ax5 = fig.add_subplot(6, 1, 5)
    ax5.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax5.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax5.set_title(f"Heating Degree Days & Cooling Degree Days", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.915, fontsize=5, bbox=purple)
    ax5.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    if hdd_sum > cdd_sum:
        ax5.bar(df['Date'], df['Heating Degree Days'], color='darkred', zorder=1, alpha=0.3)
        ax5.bar(df['Date'], (df['Cooling Degree Days'] * -1), color='darkblue', zorder=2, alpha=0.3)
    else:
        ax5.bar(df['Date'], df['Heating Degree Days'], color='darkred', zorder=2, alpha=0.3)
        ax5.bar(df['Date'], (df['Cooling Degree Days'] * -1), color='darkblue', zorder=1, alpha=0.3)
        
    ax6 = fig.add_subplot(6, 1, 6)
    ax6.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax6.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax6.set_ylim(np.nanmin(df['Growing Degree Days']), (np.nanmax(df['Growing Degree Days']) + 5))
    ax6.set_title(f"Growing Degree Days", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.915, fontsize=5, bbox=green)
    ax6.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax6.bar(df['Date'], df['Growing Degree Days'], color='green', zorder=1, alpha=0.3)
    ax6.axhline(y=mean_gdd, color='dimgrey', linestyle='--', zorder=3)   
    
    if show_running_means == True:
        run_mean_max = running_mean(df, 
                                    'Maximum Temperature',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean_max, 
                            columns=['MEAN'])
        
        run_mean_min = running_mean(df, 
                                    'Minimum Temperature',
                                    interpolation_limit=interpolation_limit)
        df_min = pd.DataFrame(run_mean_min, 
                            columns=['MEAN'])
        
        run_mean_avg = running_mean(df, 
                                    'Average Temperature',
                                    interpolation_limit=interpolation_limit)
        df_avg = pd.DataFrame(run_mean_avg, 
                            columns=['MEAN'])
        
        run_mean_dep = running_mean(df, 
                                    'Average Temperature Departure',
                                    interpolation_limit=interpolation_limit)
        df_dep = pd.DataFrame(run_mean_dep, 
                            columns=['MEAN'])

        run_mean_gdd = running_mean(df, 
                                    'Growing Degree Days',
                                    interpolation_limit=interpolation_limit)
        df_gdd = pd.DataFrame(run_mean_gdd, 
                            columns=['MEAN'])        

        ax1.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax1.fill_between(df['Date'], mean_max_t, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean_max_t))
        ax1.fill_between(df['Date'], mean_max_t, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean_max_t))
        
        ax2.plot(df['Date'], df_min['MEAN'], color='black', alpha=0.5, zorder=3)
        ax2.fill_between(df['Date'], mean_min_t, df_min['MEAN'], color='red', alpha=0.3, where=(df_min['MEAN'] > mean_min_t))
        ax2.fill_between(df['Date'], mean_min_t, df_min['MEAN'], color='blue', alpha=0.3, where=(df_min['MEAN'] < mean_min_t))
        
        ax3.plot(df['Date'], df_avg['MEAN'], color='black', alpha=0.5, zorder=3)
        ax3.fill_between(df['Date'], mean_avg_t, df_avg['MEAN'], color='red', alpha=0.3, where=(df_avg['MEAN'] > mean_avg_t))
        ax3.fill_between(df['Date'], mean_avg_t, df_avg['MEAN'], color='blue', alpha=0.3, where=(df_avg['MEAN'] < mean_avg_t))
        
        ax4.plot(df['Date'], df_dep['MEAN'], color='black', alpha=0.5, zorder=3)
        ax4.fill_between(df['Date'], 0, df_dep['MEAN'], color='red', alpha=0.3, where=(df_dep['MEAN'] > 0))
        ax4.fill_between(df['Date'], 0, df_dep['MEAN'], color='blue', alpha=0.3, where=(df_dep['MEAN'] < 0))
        
        ax6.plot(df['Date'], df_gdd['MEAN'], color='black', alpha=0.5, zorder=3)
        ax6.fill_between(df['Date'], mean_gdd, df_gdd['MEAN'], color='lime', alpha=0.3, where=(df_gdd['MEAN'] > mean_gdd))
        ax6.fill_between(df['Date'], mean_gdd, df_gdd['MEAN'], color='orange', alpha=0.3, where=(df_gdd['MEAN'] < mean_gdd))

    img_path = update_image_file_paths(station, product_type, 'Temperature Summary', show_running_means, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
    
def plot_maximum_temperature_summary(station, 
                               product_type='Maximum Temperature 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Maximum Temperature Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Maximum Temperature 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a maximum temperature summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Maximum Temperature')
    
    maxima = period_maximum(df,
                'Maximum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Maximum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Maximum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Maximum Temperature',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Maximum Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Maximum Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Maximum Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Maximum Temperature',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Maximum Temperature',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Maximum Temperature Summary [°F]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Maximum Temperature']) - 5), (np.nanmax(df['Maximum Temperature']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax.bar(df['Date'], df['Maximum Temperature'], color='red', zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Maximum Temperature',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Maximum Temperature'].iloc[0]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Maximum Temperature'].iloc[1]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Maximum Temperature'].iloc[2]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Maximum Temperature'].iloc[3]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Maximum Temperature'].iloc[4]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Maximum Temperature'].iloc[0]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Maximum Temperature'].iloc[1]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Maximum Temperature'].iloc[2]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Maximum Temperature'].iloc[3]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Maximum Temperature'].iloc[4]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.42, f"""         Statistics\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Maximum Temperature Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
    
def plot_minimum_temperature_summary(station, 
                               product_type='Minimum Temperature 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Minimum Temperature Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Minimum Temperature 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a minimum temperature summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Minimum Temperature')
    
    maxima = period_maximum(df,
                'Minimum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Minimum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Minimum Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Minimum Temperature',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Minimum Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Minimum Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Minimum Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Minimum Temperature',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Minimum Temperature',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Minimum Temperature Summary [°F]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Minimum Temperature']) - 5), (np.nanmax(df['Minimum Temperature']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax.bar(df['Date'], df['Minimum Temperature'], color='blue', zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Minimum Temperature',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Minimum Temperature'].iloc[0]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Minimum Temperature'].iloc[1]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Minimum Temperature'].iloc[2]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Minimum Temperature'].iloc[3]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Minimum Temperature'].iloc[4]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Minimum Temperature'].iloc[0]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Minimum Temperature'].iloc[1]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Minimum Temperature'].iloc[2]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Minimum Temperature'].iloc[3]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Minimum Temperature'].iloc[4]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.42, f"""         Statistics\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Minimum Temperature Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
    
def plot_average_temperature_summary(station, 
                               product_type='Average Temperature 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Average Temperature Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Average Temperature 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a average temperature summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Average Temperature')
    
    maxima = period_maximum(df,
                'Average Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Average Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Average Temperature',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Average Temperature',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Average Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Average Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Average Temperature',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Average Temperature',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Average Temperature',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Average Temperature Summary [°F]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Average Temperature']) - 5), (np.nanmax(df['Average Temperature']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax.bar(df['Date'], df['Average Temperature'], color='gray', zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Average Temperature',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Average Temperature'].iloc[0]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Average Temperature'].iloc[1]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Average Temperature'].iloc[2]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Average Temperature'].iloc[3]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Average Temperature'].iloc[4]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Average Temperature'].iloc[0]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Average Temperature'].iloc[1]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Average Temperature'].iloc[2]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Average Temperature'].iloc[3]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Average Temperature'].iloc[4]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.42, f"""         Statistics\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Average Temperature Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
    
def plot_average_temperature_departure_summary(station, 
                               product_type='Average Temperature Departure 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Average Temperature Departure Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Average Temperature Departure 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a average temperature departure summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Average Temperature Departure')
    
    maxima = period_maximum(df,
                'Average Temperature Departure',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Average Temperature Departure',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Average Temperature Departure',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Average Temperature Departure',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Average Temperature Departure',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Average Temperature Departure',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Average Temperature Departure',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Average Temperature Departure',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Average Temperature Departure',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Average Temperature Departure Summary [°F]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Average Temperature Departure']) - 5), (np.nanmax(df['Average Temperature Departure']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    bar_colors = ['red' if t >= 0 else 'blue' for t in df['Average Temperature Departure']]
    ax.bar(df['Date'], df['Average Temperature Departure'], color=bar_colors, zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Average Temperature Departure',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Average Temperature Departure'].iloc[0]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Average Temperature Departure'].iloc[1]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Average Temperature Departure'].iloc[2]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Average Temperature Departure'].iloc[3]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Average Temperature Departure'].iloc[4]} [°F] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Average Temperature Departure'].iloc[0]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Average Temperature Departure'].iloc[1]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Average Temperature Departure'].iloc[2]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Average Temperature Departure'].iloc[3]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Average Temperature Departure'].iloc[4]} [°F] - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.42, f"""         Statistics\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Average Temperature Departure Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
def plot_heating_degree_day_summary(station, 
                               product_type='Heating Degree Days 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Heating Degree Day Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Heating Degree Days 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a heating degree day summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Heating Degree Days')
    
    maxima = period_maximum(df,
                'Heating Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Heating Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Heating Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    numsum = period_sum(df,
                        'Heating Degree Days',
                        round_value=False,
                        to_nearest=0,
                        data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Heating Degree Days',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Heating Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Heating Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Heating Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Heating Degree Days',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Heating Degree Days',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Heating Degree Day Summary   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Heating Degree Days']) - 5), (np.nanmax(df['Heating Degree Days']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax.bar(df['Date'], df['Heating Degree Days'], color='red', zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Heating Degree Days',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Heating Degree Days'].iloc[0]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Heating Degree Days'].iloc[1]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Heating Degree Days'].iloc[2]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Heating Degree Days'].iloc[3]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Heating Degree Days'].iloc[4]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}        """, transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Heating Degree Days'].iloc[0]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Heating Degree Days'].iloc[1]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Heating Degree Days'].iloc[2]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Heating Degree Days'].iloc[3]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Heating Degree Days'].iloc[4]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}        """, transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.405, f"""         Statistics\nSum: {numsum}\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Heating Degree Day Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
def plot_cooling_degree_day_summary(station, 
                               product_type='Cooling Degree Days 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Cooling Degree Day Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Cooling Degree Days 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a cooling degree day summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Cooling Degree Days')
    
    maxima = period_maximum(df,
                'Cooling Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Cooling Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Cooling Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    numsum = period_sum(df,
                        'Cooling Degree Days',
                        round_value=False,
                        to_nearest=0,
                        data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Cooling Degree Days',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Cooling Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Cooling Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Cooling Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Cooling Degree Days',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Cooling Degree Days',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Cooling Degree Day Summary   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Cooling Degree Days']) - 5), (np.nanmax(df['Cooling Degree Days']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax.bar(df['Date'], df['Cooling Degree Days'], color='blue', zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Cooling Degree Days',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Cooling Degree Days'].iloc[0]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Cooling Degree Days'].iloc[1]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Cooling Degree Days'].iloc[2]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Cooling Degree Days'].iloc[3]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Cooling Degree Days'].iloc[4]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}           """, transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Cooling Degree Days'].iloc[0]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Cooling Degree Days'].iloc[1]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Cooling Degree Days'].iloc[2]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Cooling Degree Days'].iloc[3]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Cooling Degree Days'].iloc[4]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}           """, transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.405, f"""         Statistics\nSum: {numsum}\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Cooling Degree Day Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")
    
def plot_growing_degree_day_summary(station, 
                               product_type='Growing Degree Days 30 Day Summary',
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
                               show_running_mean=True,
                               interpolation_limit=3,
                               x_axis_day_interval=5):
    
    """
    This function plots a graphic showing the Growing Degree Day Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 

    Optional Arguments:
    
    1) product_type (String) - Default='Growing Degree Days 30 Day Summary'. The type of product. 
    
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
    
    12) show_running_mean (Boolean) - Default=True. When set to False, running mean will be hidden.
    
    13) interpolation_limit (Integer) - Default=3. If there are missing days in the dataset, this value represents the amount of consecutive missing days to interpolate between.
    
    14) x_axis_day_interval (Integer) - Default=5. The amount of days the x-axis tick marks are spaced apart. 
    
    Returns
    -------
    
    A graphic showing a growing degree day summary of xmACIS2 data.
    """


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

    missing = number_of_missing_days(df,
                           'Growing Degree Days')
    
    maxima = period_maximum(df,
                'Growing Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    mean = period_mean(df,
                'Growing Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    minima = period_minimum(df,
                'Growing Degree Days',
                round_value=True,
                to_nearest=0,
                data_type='integer')
    
    numsum = period_sum(df,
                        'Growing Degree Days',
                        round_value=False,
                        to_nearest=0,
                        data_type='integer')
    
    standard_deviation = period_standard_deviation(df,
                                                    'Growing Degree Days',
                                                    round_value=True,
                                                    to_nearest=1,
                                                    data_type='float')
    
    variance = period_variance(df,
                                'Growing Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    skewness = period_skewness(df,
                                'Growing Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    kurtosis = period_kurtosis(df,
                                'Growing Degree Days',
                                round_value=True,
                                to_nearest=1,
                                data_type='float')
    
    top5 = period_rankings(df,
                            'Growing Degree Days',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
    
    bot5 = period_rankings(df,
                            'Growing Degree Days',
                            ascending=False,
                            rank_subset='last',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Growing Degree Day Summary   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", fontsize=18, x=0.6, y=1.06, fontweight='bold', bbox=props)
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_ylim((np.nanmin(df['Growing Degree Days']) - 5), (np.nanmax(df['Growing Degree Days']) + 5))
    ax.xaxis.set_major_locator(md.DayLocator(interval=x_axis_day_interval))
    ax.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax.bar(df['Date'], df['Growing Degree Days'], color='green', zorder=1, alpha=0.3)
    if missing == 0:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=green)
    elif missing > 0 and missing < 5:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=warm)
    else:
        ax.text(0.35, 1.07, f"Missing Days = {str(missing)}", fontsize=9, fontweight='bold', color='white', transform=ax.transAxes, bbox=purple)
    ax.text(0.0008, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax.transAxes, bbox=props)
    ax.axhline(y=maxima, color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax.axhline(y=mean, color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax.axhline(y=minima, color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax.legend(loc=(0.5, 1.05))
    
    if show_running_mean == True:
        run_mean = running_mean(df, 
                                    'Growing Degree Days',
                                    interpolation_limit=interpolation_limit)
        df_max = pd.DataFrame(run_mean, 
                            columns=['MEAN'])
        
        
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='darkgreen', alpha=0.3, where=(df_max['MEAN'] > mean))
        ax.fill_between(df['Date'], mean, df_max['MEAN'], color='darkorange', alpha=0.3, where=(df_max['MEAN'] < mean))
        
        
    ax.text(1.01, 0.63, f"""         Top 5 Days\n\n#1 {top5['Growing Degree Days'].iloc[0]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {top5['Growing Degree Days'].iloc[1]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {top5['Growing Degree Days'].iloc[2]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {top5['Growing Degree Days'].iloc[3]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {top5['Growing Degree Days'].iloc[4]} - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}         """, transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=warm)
    ax.text(1.01, 0.01, f"""         Bottom 5 Days\n\n#1 {bot5['Growing Degree Days'].iloc[0]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#2 {bot5['Growing Degree Days'].iloc[1]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#3 {bot5['Growing Degree Days'].iloc[2]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#4 {bot5['Growing Degree Days'].iloc[3]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}\n\n#5 {bot5['Growing Degree Days'].iloc[4]} - {bot5['Date'].iloc[0].strftime('%m/%d/%Y')}           """, transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=cool)
    ax.text(1.01, 0.405, f"""         Statistics\nSum: {numsum}\nStandard Deviation: {standard_deviation}\nVariance: {variance}\nSkewness: {skewness}\nKurtosis: {kurtosis}""", transform=ax.transAxes, fontsize=12, fontweight='bold', color='white', bbox=gray)

    
    img_path = update_image_file_paths(station, product_type, 'Growing Degree Day Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {fname} to {img_path}")