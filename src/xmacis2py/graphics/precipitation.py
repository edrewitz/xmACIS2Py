"""
This file hosts the functions that plot precipitation summaries that have multiple parameters in xmACIS2 Data

(C) Eric J. Drewitz 2025-2026
"""


import xmacis2py.analysis_tools.analysis as _analysis
import matplotlib as _mpl
import matplotlib.dates as _md
import matplotlib.pyplot as _plt
import numpy as _np
import pandas as _pd
import warnings as _warnings
_warnings.filterwarnings('ignore')

from xmacis2py.utils.file_funcs import update_image_file_paths as _update_image_file_paths
from xmacis2py.data_access.get_data import get_data as _get_data
from matplotlib.ticker import MaxNLocator as _MaxNLocator

try:
    from datetime import(
        datetime as _datetime, 
        timedelta as _timedelta, 
        UTC as _UTC
    )
except Exception as e:
    from datetime import(
        datetime as _datetime, 
        timedelta as _timedelta
    )

_mpl.rcParams['font.weight'] = 'bold'
_mpl.rcParams['xtick.labelsize'] = 7
_mpl.rcParams['ytick.labelsize'] = 7

_props = dict(boxstyle='round', facecolor='wheat', alpha=1)
_warm = dict(boxstyle='round', facecolor='darkred', alpha=1)
_green = dict(boxstyle='round', facecolor='darkgreen', alpha=1)
_gray = dict(boxstyle='round', facecolor='gray', alpha=1)
_purple = dict(boxstyle='round', facecolor='purple', alpha=1)


try:
    _utc = _datetime.now(_UTC)
except Exception as e:
    _utc = _datetime.utcnow()
    
_today = _datetime.now()
_yesterday = _today - _timedelta(days=1)

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
    
def plot_precipitation_summary(station, 
                               product_type='Precipitation 30 Day Summary',
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
                               show_running_sum=False,
                               interpolation_limit=3,
                               x_axis_day_interval=5,
                               x_axis_date_format='%m/%d',
                               create_ranking_table=True,
                               bar_label_fontsize=6,
                               only_label_bars_greater_than_0=True,
                               hide_bar_labels=False):
    
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
                        
    7) clear_recycle_bin (Boolean) - (Default=False in xmACIS2Py >= 2.2.1) (Default=True in xmACIS2Py < 2.2.1). When set to True, 
        the contents in your recycle/trash bin will be deleted with each run of the program you are calling WxData. 
        This setting is to help preserve memory on the machine. 
        
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
    """

    _mpl.rcParams['font.size'] = bar_label_fontsize

    df = _get_data(station,
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

    missing = _analysis.number_of_missing_days(df,
                           'Precipitation')
    
    standard_deviation = _analysis.period_standard_deviation(df,
                                                    'Precipitation',
                                                    round_value=True,
                                                    to_nearest=2,
                                                    data_type='float')
    
    variance = _analysis.period_variance(df,
                                'Precipitation',
                                round_value=True,
                                to_nearest=2,
                                data_type='float')
    
    skewness = _analysis.period_skewness(df,
                                'Precipitation',
                                round_value=True,
                                to_nearest=2,
                                data_type='float')
    
    kurtosis = _analysis.period_kurtosis(df,
                                'Precipitation',
                                round_value=True,
                                to_nearest=2,
                                data_type='float')
    
    total_precip = _analysis.period_sum(df,
                                'Precipitation',
                                round_value=False,
                                to_nearest=2,
                                data_type='float')
    
    top5 = _analysis.period_rankings(df,
                            'Precipitation',
                            ascending=False,
                            rank_subset='first',
                            first=5,
                            last=5,
                            between=[],
                            date_name='Date')
        
        
    fig = _plt.figure(figsize=(12,8))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Precipitation Summary [IN]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}", 
                 fontsize=14, y=0.98, 
                 fontweight='bold', 
                 bbox=_props)
    
    ax = fig.add_subplot(1, 1, 1)
    ax.yaxis.set_major_locator(_MaxNLocator(integer=False))
    ax.xaxis.set_major_formatter(_md.DateFormatter(x_axis_date_format))
    ax.xaxis.set_major_locator(_md.DayLocator(interval=x_axis_day_interval))
    bars = _plt.bar(df['Date'], df['Precipitation'], color='green', alpha=0.3)
    if hide_bar_labels == False:
        if only_label_bars_greater_than_0 == True:
            ax.bar_label(bars, fmt=lambda x: f'{x}' if x > 0 else '', label_type='edge')
        else:
            _plt.bar_label(bars)
    else:
        pass
    if missing == 0:
        ax.text(0.87, 1.01, f"Missing Days = {str(missing)}", 
                fontsize=9, 
                fontweight='bold', 
                color='white', 
                transform=ax.transAxes, 
                bbox=_green)
        
    elif missing > 0 and missing < 5:
        ax.text(0.87, 1.01, f"Missing Days = {str(missing)}", 
                fontsize=9, 
                fontweight='bold', 
                color='white', 
                transform=ax.transAxes, 
                bbox=_warm)
    else:
        ax.text(0.87, 1.01, f"Missing Days = {str(missing)}", 
                fontsize=9, 
                fontweight='bold',
                color='white', 
                transform=ax.transAxes, 
                bbox=_purple)
        
    ax.text(0.0008, 
            1.01, 
            f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {_utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {_utc.strftime('%Y-%m-%d %H:%MZ')}", 
            fontsize=6, 
            fontweight='bold', 
            transform=ax.transAxes, 
            bbox=_props)
    
    if show_running_sum == True:
        run_sum = _analysis.running_sum(df, 
                                    'Precipitation',
                                    interpolation_limit=interpolation_limit)
        df_max = _pd.DataFrame(run_sum, 
                            columns=['MEAN'])
        
        ax.set_ylim(0, total_precip + 0.05)
        ax.plot(df['Date'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING SUM')   
    else:
        ax.set_ylim(0, (_np.nanmax(df['Precipitation']) + 0.05))
        
    img_path = _update_image_file_paths(station, 
                                       product_type, 
                                       'Precipitation Summary', 
                                       show_running_sum,
                                       False,
                                       'No Detrending', 
                                       running_type='Sum')
        
    fname = f"{station.upper()} {product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    _plt.close(fig)
    print(f"Saved {fname} to {img_path}")
        
    if create_ranking_table == True:
        
        _plt.axis('off')
        fig = _plt.figure(figsize=(12,8))
        fig.set_facecolor('aliceblue')
        
        fig.text(0, 1, 
                 f"""{station.upper()} Precipitation Summary [IN]   Period Of Record: {df['Date'].iloc[0].strftime('%m/%d/%Y')} - {df['Date'].iloc[-1].strftime('%m/%d/%Y')}\n\nTop 5 Days: #1 {top5['Precipitation'].iloc[0]} [IN] - {top5['Date'].iloc[0].strftime('%m/%d/%Y')}   #2 {top5['Precipitation'].iloc[1]} [IN] - {top5['Date'].iloc[1].strftime('%m/%d/%Y')}   #3 {top5['Precipitation'].iloc[2]} [IN] - {top5['Date'].iloc[2].strftime('%m/%d/%Y')}   #4 {top5['Precipitation'].iloc[3]} [IN] - {top5['Date'].iloc[3].strftime('%m/%d/%Y')}   #5 {top5['Precipitation'].iloc[4]} [IN] - {top5['Date'].iloc[4].strftime('%m/%d/%Y')}
                                
Standard Deviation: {standard_deviation}   Variance: {variance}   Skewness: {skewness}   Kurtosis: {kurtosis}
                                    
                """, fontsize=14, fontweight='bold', color='white', bbox=_green)
        
        fig.text(0, 0.997, 
                 f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {_utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {_utc.strftime('%Y-%m-%d %H:%MZ')}", 
                 fontsize=6, 
                 fontweight='bold', 
                 bbox=_props)

    
    fname = f"{station.upper()} Stats Table.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    _plt.close(fig)
    print(f"Saved {fname} to {img_path}")