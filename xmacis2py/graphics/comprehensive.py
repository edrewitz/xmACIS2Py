"""
This file hosts the functions that plot comprehensive summaries that have multiple parameters in xmACIS2 Data

(C) Eric J. Drewitz 2025
"""



import matplotlib as mpl
import matplotlib.dates as md
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

from xmacis2py.utils.file_funcs import(
    update_csv_file_paths, 
    update_image_file_paths
)
from xmacis2py.data_access.get_data import get_data
from xmacis2py.analysis_tools import *

from matplotlib.ticker import MaxNLocator
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
orange = dict(boxstyle='round', facecolor='orange', alpha=1)

    
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
                               product_type='PAST 30 DAYS', 
                               start_date=None,
                                end_date=None,
                                from_when=yesterday,
                                time_delta=30,
                                proxies=None,
                                clear_recycle_bin=True,
                                to_csv=False,
                                path='default',
                                filename='default',
                                notifications='on'
                               show_running_mean=True):

    """
    This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 
    
    2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
       A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

    Optional Arguments:
    
    1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)
    
    2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)
    
    3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

    """

    df = get_data()

    file = df.to_csv(csv_fname, index=False)
    os.replace(f"{csv_fname}", f"{path}/{csv_fname}")

    df = pd.read_csv(f"{path}/{csv_fname}")

    df['DATE'] = pd.to_datetime(df['DATE'])

    missing_days = df_days

    means = get_means(df)
    maxima = get_maxima(df)
    minima = get_minima(df)
    hdd_sum, cdd_sum, gdd_sum = get_sum_hdd_cdd(df)

    run_mean_max = running_mean(df, 'MAX')
    df_max = pd.DataFrame(run_mean_max, columns=['MEAN'])
    
    run_mean_min = running_mean(df, 'MIN')
    df_min = pd.DataFrame(run_mean_min, columns=['MEAN'])
    
    run_mean_avg = running_mean(df, 'AVG')
    df_avg = pd.DataFrame(run_mean_avg, columns=['MEAN'])
    
    run_mean_dep = running_mean(df, 'DEP')
    df_dep = pd.DataFrame(run_mean_dep, columns=['MEAN'])

    run_mean_gdd = running_mean(df, 'GDD')
    df_gdd = pd.DataFrame(run_mean_gdd, columns=['MEAN'])

    fig = plt.figure(figsize=(12,10))
    fig.set_facecolor('aliceblue')

    fig.suptitle(f"{station.upper()} Temperature Summary [{product_type.upper()}]", fontsize=18, y=0.98, fontweight='bold')

    ax1 = fig.add_subplot(6, 1, 1)
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax1.set_ylim((np.nanmin(df['MAX']) - 5), (np.nanmax(df['MAX']) + 5))
    ax1.set_title(f"MAX T [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.825, bbox=warm)
    ax1.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax1.bar(df['DATE'], df['MAX'], color='red', zorder=1, alpha=0.3)
    if show_running_mean == True:
        ax1.plot(df['DATE'], df_max['MEAN'], color='black', alpha=0.5, zorder=3, label='RUNNING MEAN')
        ax1.fill_between(df['DATE'], means[0], df_max['MEAN'], color='red', alpha=0.3, where=(df_max['MEAN'] > means[0]))
        ax1.fill_between(df['DATE'], means[0], df_max['MEAN'], color='blue', alpha=0.3, where=(df_max['MEAN'] < means[0]))
        show_running_data = True
    else:
        show_running_data = False
    ax1.text(0.35, 1.45, f"Valid: {start_date} to {end_date}", fontsize=12, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.425, 1.27, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.0008, 1.05, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax1.transAxes, bbox=props)
    ax1.axhline(y=maxima[0], color='darkred', linestyle='--', zorder=3, label='PERIOD MAX')
    ax1.axhline(y=means[0], color='dimgrey', linestyle='--', zorder=3, label='PERIOD MEAN')
    ax1.axhline(y=minima[0], color='darkblue', linestyle='--', zorder=3, label='PERIOD MIN')
    ax1.legend(loc=(0.7, 1.01))

    ax2 = fig.add_subplot(6, 1, 2)
    ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax2.set_ylim((np.nanmin(df['MIN']) - 5), (np.nanmax(df['MIN']) + 5))
    ax2.set_title(f"MIN T [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.825, bbox=cool)
    ax2.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax2.bar(df['DATE'], df['MIN'], color='blue', zorder=1, alpha=0.3)
    if show_running_mean == True:
        ax2.plot(df['DATE'], df_min['MEAN'], color='black', alpha=0.5, zorder=3)
        ax2.fill_between(df['DATE'], means[1], df_min['MEAN'], color='red', alpha=0.3, where=(df_min['MEAN'] > means[1]))
        ax2.fill_between(df['DATE'], means[1], df_min['MEAN'], color='blue', alpha=0.3, where=(df_min['MEAN'] < means[1]))
        show_running_data = True
    else:
        show_running_data = False
    ax2.axhline(y=maxima[1], color='darkred', linestyle='--', zorder=3)
    ax2.axhline(y=means[1], color='dimgrey', linestyle='--', zorder=3)
    ax2.axhline(y=minima[1], color='darkblue', linestyle='--', zorder=3)

    ax3 = fig.add_subplot(6, 1, 3)
    ax3.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax3.set_ylim((np.nanmin(df['AVG']) - 5), (np.nanmax(df['AVG']) + 5))
    ax3.set_title(f"AVG T [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.825, bbox=gray)
    ax3.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax3.bar(df['DATE'], df['AVG'], color='black', zorder=1, alpha=0.3)
    if show_running_mean == True:
        ax3.plot(df['DATE'], df_avg['MEAN'], color='black', alpha=0.5, zorder=3)
        ax3.fill_between(df['DATE'], means[2], df_avg['MEAN'], color='red', alpha=0.3, where=(df_avg['MEAN'] > means[2]))
        ax3.fill_between(df['DATE'], means[2], df_avg['MEAN'], color='blue', alpha=0.3, where=(df_avg['MEAN'] < means[2]))
        show_running_data = True
    else:
        show_running_data = False
    ax3.axhline(y=maxima[2], color='darkred', linestyle='--', zorder=3)
    ax3.axhline(y=means[2], color='dimgrey', linestyle='--', zorder=3)
    ax3.axhline(y=minima[2], color='darkblue', linestyle='--', zorder=3)
    

    ax4 = fig.add_subplot(6, 1, 4)
    ax4.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax4.set_ylim((np.nanmin(df['DEP']) - 5), (np.nanmax(df['DEP']) + 5))
    ax4.set_title(f"T DEP [°F]", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.825, bbox=gray)
    ax4.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax4.bar(df['DATE'], df['DEP'], color='black', zorder=1, alpha=0.3)
    if show_running_mean == True:
        ax4.plot(df['DATE'], df_dep['MEAN'], color='black', alpha=0.5, zorder=3)
        ax4.fill_between(df['DATE'], 0, df_dep['MEAN'], color='red', alpha=0.3, where=(df_dep['MEAN'] > 0))
        ax4.fill_between(df['DATE'], 0, df_dep['MEAN'], color='blue', alpha=0.3, where=(df_dep['MEAN'] < 0))
        show_running_data = True
    else:
        show_running_data = False
    ax4.axhline(y=maxima[3], color='darkred', linestyle='--', zorder=3)
    ax4.axhline(y=minima[3], color='darkblue', linestyle='--', zorder=3)
    ax4.axhline(y=0, color='black', linestyle='-', zorder=3)

    ax5 = fig.add_subplot(6, 1, 5)
    ax5.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax5.set_title(f"HDD & CDD", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.825, bbox=purple)
    ax5.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    if hdd_sum > cdd_sum:
        ax5.bar(df['DATE'], df['HDD'], color='darkred', zorder=1, alpha=0.3)
        ax5.bar(df['DATE'], (df['CDD'] * -1), color='darkblue', zorder=2, alpha=0.3)
    else:
        ax5.bar(df['DATE'], df['HDD'], color='darkred', zorder=2, alpha=0.3)
        ax5.bar(df['DATE'], (df['CDD'] * -1), color='darkblue', zorder=1, alpha=0.3)        

    ax6 = fig.add_subplot(6, 1, 6)
    ax6.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax6.set_ylim(np.nanmin(df['GDD']), (np.nanmax(df['GDD']) + 5))
    ax6.set_title(f"GDD", fontweight='bold', alpha=1, loc='right', color='white', zorder=15, y=0.825, bbox=green)
    ax6.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax6.bar(df['DATE'], df['GDD'], color='green', zorder=1, alpha=0.3)
    ax6.axhline(y=means[9], color='dimgrey', linestyle='--', zorder=3)
    if show_running_mean == True:
        ax6.plot(df['DATE'], df_gdd['MEAN'], color='black', alpha=0.5, zorder=3)
        ax6.fill_between(df['DATE'], means[9], df_gdd['MEAN'], color='lime', alpha=0.3, where=(df_gdd['MEAN'] > means[9]))
        ax6.fill_between(df['DATE'], means[9], df_gdd['MEAN'], color='orange', alpha=0.3, where=(df_gdd['MEAN'] < means[9]))
        show_running_data = True
    else:
        show_running_data = False

    top_5, top_dates = xm.rank_top_5(df, 'MAX')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'MAX')

    ax6.text(0.0, -2, f"    MAX T STATS\n\nMAX: {str(int(round(maxima[0], 0)))} [°F]\nMEAN: {str(int(round(means[0], 0)))} [°F]\nMIN: {str(int(round(minima[0], 0)))} [°F]\n\nTOP-5\n#1: {str(int(round(top_5[0], 0)))} [°F] - {top_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))} [°F] - {top_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))} [°F] - {top_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))} [°F] - {top_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))} [°F] - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(int(round(bottom_5[0], 0)))} [°F] - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))} [°F] - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))} [°F] - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))} [°F] - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))} [°F] - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=warm)

    top_5, top_dates = xm.rank_top_5(df, 'MIN')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'MIN')

    ax6.text(0.12, -2, f"    MIN T STATS\n\nMAX: {str(int(round(maxima[1], 0)))} [°F]\nMEAN: {str(int(round(means[1], 0)))} [°F]\nMIN: {str(int(round(minima[1], 0)))} [°F]\n\nTOP-5\n#1: {str(int(round(top_5[0], 0)))} [°F] - {top_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))} [°F] - {top_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))} [°F] - {top_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))} [°F] - {top_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))} [°F] - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(int(round(bottom_5[0], 0)))} [°F] - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))} [°F] - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))} [°F] - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))} [°F] - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))} [°F] - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=cool)

    top_5, top_dates = xm.rank_top_5(df, 'AVG')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'AVG')
    
    ax6.text(0.24, -2, f"    AVG T STATS\n\nMAX: {str(round(maxima[2], 1))} [°F]\nMEAN: {str(round(means[2], 1))} [°F]\nMIN: {str(round(minima[2], 1))} [°F]\n\nTOP-5\n#1: {str(round(top_5[0], 1))} [°F] - {top_dates[0].strftime(f'%b %d')}\n#2: {str(round(top_5[1], 1))} [°F] - {top_dates[1].strftime(f'%b %d')}\n#3: {str(round(top_5[2], 1))} [°F] - {top_dates[2].strftime(f'%b %d')}\n#4: {str(round(top_5[3], 1))} [°F] - {top_dates[3].strftime(f'%b %d')}\n#5: {str(round(top_5[4], 1))} [°F] - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(round(bottom_5[0], 1))} [°F] - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(round(bottom_5[1], 1))} [°F] - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(round(bottom_5[2], 1))} [°F] - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(round(bottom_5[3], 1))} [°F] - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(round(bottom_5[4], 1))} [°F] - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=gray)

    top_5, top_dates = xm.rank_top_5(df, 'DEP')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'DEP')

    ax6.text(0.37, -2, f"    T DEP STATS\n\nMAX: {str(round(maxima[3], 1))} [°F]\nMEAN: {str(round(means[3], 1))} [°F]\nMIN: {str(round(minima[3], 1))} [°F]\n\nTOP-5\n#1: {str(round(top_5[0], 1))} [°F] - {top_dates[0].strftime(f'%b %d')}\n#2: {str(round(top_5[1], 1))} [°F] - {top_dates[1].strftime(f'%b %d')}\n#3: {str(round(top_5[2], 1))} [°F] - {top_dates[2].strftime(f'%b %d')}\n#4: {str(round(top_5[3], 1))} [°F] - {top_dates[3].strftime(f'%b %d')}\n#5: {str(round(top_5[4], 1))} [°F] - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(round(bottom_5[0], 1))} [°F] - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(round(bottom_5[1], 1))} [°F] - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(round(bottom_5[2], 1))} [°F] - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(round(bottom_5[3], 1))} [°F] - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(round(bottom_5[4], 1))} [°F] - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=gray)

    top_5, top_dates = xm.rank_top_5(df, 'HDD')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'HDD')

    ax6.text(0.72, -2, f"    HDD STATS\n\nMAX: {str(int(round(maxima[4], 0)))}\nMEAN: {str(int(round(means[4], 0)))}\nSUM: {str(hdd_sum)} \n\nTOP-5\n#1: {str(int(round(top_5[0], 0)))}  - {top_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))}  - {top_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))}  - {top_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))}  - {top_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))}  - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(int(round(bottom_5[0], 0)))}  - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))}  - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))}  - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))}  - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))}  - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=warm)

    top_5, top_dates = xm.rank_top_5(df, 'CDD')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'CDD')

    ax6.text(0.82, -2, f"    CDD STATS\n\nMAX: {str(int(round(maxima[5], 0)))}\nMEAN: {str(int(round(means[5], 0)))}\nSUM: {str(cdd_sum)} \n\nTOP-5\n#1: {str(int(round(top_5[0], 0)))}  - {top_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))}  - {top_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))}  - {top_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))}  - {top_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))}  - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(int(round(bottom_5[0], 0)))}  - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))}  - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))}  - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))}  - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))}  - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=cool)

    top_5, top_dates = xm.rank_top_5(df, 'GDD')
    bottom_5, bottom_dates = xm.rank_bottom_5(df, 'GDD')

    ax6.text(0.92, -2, f"    GDD STATS\n\nMAX: {str(int(round(maxima[9], 0)))}\nMEAN: {str(int(round(means[9], 0)))}\nSUM: {str(gdd_sum)} \n\nTOP-5\n#1: {str(int(round(top_5[0], 0)))}  - {top_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))}  - {top_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))}  - {top_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))}  - {top_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))}  - {top_dates[4].strftime(f'%b %d')}\n\nBOT-5\n#1: {str(int(round(bottom_5[0], 0)))}  - {bottom_dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))}  - {bottom_dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))}  - {bottom_dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))}  - {bottom_dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))}  - {bottom_dates[4].strftime(f'%b %d')}", fontsize=6, fontweight='bold', transform=ax6.transAxes, color='white', bbox=green)
    
    
    img_path, img_path_print = update_image_file_paths(station, product_type, 'Temperature Summary', show_running_mean, running_type='Mean')
    fname = f"{station.upper()}_{product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    print(f"Saved {fname} to {img_path_print}")