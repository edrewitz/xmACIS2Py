import matplotlib as mpl
import matplotlib.dates as md
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import metpy.calc as mpcalc
import numpy as np
import pandas as pd
import os
import xmacis2py.xmacis_data as xm
import warnings
warnings.filterwarnings('ignore')

from xmacis2py.file_funcs import update_csv_file_paths, update_image_file_paths
try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta

mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['xtick.labelsize'] = 7
mpl.rcParams['ytick.labelsize'] = 7
mpl.rcParams['font.size'] = 6

props = dict(boxstyle='round', facecolor='wheat', alpha=1)

try:
    utc = datetime.now(UTC)
except Exception as e:
    utc = datetime.utcnow()

def plot_temperature_summary(station, product_type, start_date=None, end_date=None):

    r'''
    This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 
    2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
       A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

    Optional Arguments:
    1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)
    2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

    '''

    try:
        today = datetime.now(UTC)
    except Exception as e:
        today = datetime.utcnow()


    if product_type == 'Past 7 Days' or product_type == 7:

        product_type = 'Past 7 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=9)
        d = 7
        decimate = 1

    elif product_type == 'Past 10 Days' or product_type == 10:

        product_type = 'Past 10 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=12) 
        d = 10
        decimate = 1

    elif product_type == 'Past 15 Days' or product_type == 15:

        product_type = 'Past 15 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=17)  
        d = 15
        decimate = 1

    elif product_type == 'Past 30 Days' or product_type == 30:

        product_type = 'Past 30 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=32)   
        d = 30
        decimate = 1

    elif product_type == 'Past 60 Days' or product_type == 60:

        product_type = 'Past 60 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=62)  
        d = 60
        decimate = 2

    elif product_type == 'Past 90 Days' or product_type == 90:

        product_type = 'Past 90 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=92) 
        d = 90
        decimate = 5

    else:
        start_date = start_date
        end_date = end_date
        t1 = datetime.strptime(start_date, '%Y-%m-%d')
        t2 = datetime.strptime(end_date, '%Y-%m-%d')
        d1 = t1.day
        d2 = t2.day
        d = abs(d2 - d1)

    csv_fname = f"{station}_{product_type}.csv"

    path, path_print = update_csv_file_paths(station, product_type)

    try:
        if os.path.exists(f"{path}/{csv_fname}"):
            os.remove(f"{path}/{csv_fname}")
        else:
            pass
    except Exception as e:
        pass    

    df, start_date, end_date, df_days = xm.xmacis_to_df(station, start_date, end_date, 'AVG')

    file = df.to_csv(csv_fname, index=False)
    os.replace(f"{csv_fname}", f"{path}/{csv_fname}")

    df = pd.read_csv(f"{path}/{csv_fname}")

    df['DATE'] = pd.to_datetime(df['DATE'])

    missing_days = df_days

    means = xm.get_means(df)
    maxima = xm.get_maxima(df)
    minima = xm.get_minima(df)
    hdd_sum, cdd_sum = xm.get_sum_hdd_cdd(df)

    fig = plt.figure(figsize=(14,15))
    fig.set_facecolor('aliceblue')
    gs = gridspec.GridSpec(10, 10)

    fig.suptitle(f"{station.upper()} Temperature Summary [{product_type.upper()}]", fontsize=18, fontweight='bold')

    ax1 = fig.add_subplot(gs[0:2, 0:10])
    ax1.set_title(f"Daily Maximum Temperature [°F]", fontweight='bold', y=0.05, alpha=1, loc='center', zorder=11)
    ax1.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax1.bar(df['DATE'], df['MAX'], color='red', zorder=1, alpha=0.3)
    ax1.text(0.35, 1.45, f"Valid: {start_date} to {end_date}", fontsize=12, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.425, 1.37, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.94, 0.85, f"MAX = {str(int(round(maxima[0], 0)))} [°F]\nMEAN = {str(int(round(means[0], 0)))} [°F]\nMIN = {str(int(round(minima[0], 0)))} [°F]", fontsize=5, fontweight='bold', transform=ax1.transAxes, bbox=props, zorder=10)
    ax1.text(0.0001, 1.02, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax1.transAxes, bbox=props)
    ax1.axhline(y=maxima[0], color='darkred', linestyle='--', zorder=3)
    ax1.axhline(y=means[0], color='dimgrey', linestyle='--', zorder=3)
    ax1.axhline(y=minima[0], color='darkblue', linestyle='--', zorder=3)

    ax2 = fig.add_subplot(gs[2:4, 0:10])
    ax2.set_title(f"Daily Minimum Temperature [°F]", fontweight='bold', y=0.05, alpha=1, loc='center', zorder=11)
    ax2.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax2.bar(df['DATE'], df['MIN'], color='blue', zorder=1, alpha=0.3)
    ax2.text(0.94, 0.85, f"MAX = {str(int(round(maxima[1], 0)))} [°F]\nMEAN = {str(int(round(means[1], 0)))} [°F]\nMIN = {str(int(round(minima[1], 0)))} [°F]", fontsize=5, fontweight='bold', transform=ax2.transAxes, bbox=props, zorder=10)
    ax2.axhline(y=maxima[1], color='darkred', linestyle='--', zorder=3)
    ax2.axhline(y=means[1], color='dimgrey', linestyle='--', zorder=3)
    ax2.axhline(y=minima[1], color='darkblue', linestyle='--', zorder=3)

    ax3 = fig.add_subplot(gs[4:6, 0:10])
    ax3.set_title(f"Daily Average Temperature [°F]", fontweight='bold', y=0.05, alpha=1, loc='center', zorder=11)
    ax3.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax3.bar(df['DATE'], df['AVG'], color='black', zorder=1, alpha=0.3)
    ax3.text(0.93, 0.85, f"MAX = {str(maxima[2])} [°F]\nMEAN = {str(means[2])} [°F]\nMIN = {str(minima[2])} [°F]", fontsize=5, fontweight='bold', transform=ax3.transAxes, bbox=props, zorder=10)
    ax3.axhline(y=maxima[2], color='darkred', linestyle='--', zorder=3)
    ax3.axhline(y=means[2], color='dimgrey', linestyle='--', zorder=3)
    ax3.axhline(y=minima[2], color='darkblue', linestyle='--', zorder=3)
    

    ax4 = fig.add_subplot(gs[6:8, 0:10])
    ax4.set_title(f"Daily Temperature Departure [°F]", fontweight='bold', y=0.05, alpha=1, loc='center', zorder=11)
    ax4.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax4.bar(df['DATE'], df['DEP'], color='black', zorder=1, alpha=0.3)
    ax4.text(0.94, 0.85, f"MAX = {str(maxima[3])} [°F]\nMEAN = {str(means[3])} [°F]\nMIN = {str(minima[3])} [°F]", fontsize=5, fontweight='bold', transform=ax4.transAxes, bbox=props, zorder=10)
    ax4.axhline(y=maxima[3], color='darkred', linestyle='--', zorder=3)
    ax4.axhline(y=means[3], color='dimgrey', linestyle='--', zorder=3)
    ax4.axhline(y=minima[3], color='darkblue', linestyle='--', zorder=3)
    ax4.axhline(y=0, color='black', linestyle='-', zorder=3)

    ax5 = fig.add_subplot(gs[8:10, 0:10])
    ax5.set_title(f"HDD [Red] & CDD [Blue]", fontweight='bold', y=0.05, alpha=1, loc='center', zorder=11)
    ax5.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    if hdd_sum > cdd_sum:
        ax5.bar(df['DATE'], df['HDD'], color='darkred', zorder=1, alpha=0.3)
        ax5.bar(df['DATE'], df['CDD'], color='darkblue', zorder=2, alpha=0.3)
    else:
        ax5.bar(df['DATE'], df['HDD'], color='darkred', zorder=2, alpha=0.3)
        ax5.bar(df['DATE'], df['CDD'], color='darkblue', zorder=1, alpha=0.3)        
    ax5.text(0.935, 0.9, f"Total HDD = {str(int(round(hdd_sum, 0)))}\nTotal CDD = {str(int(round(cdd_sum, 0)))}", fontsize=5, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    top_5, dates = xm.rank_top_5(df, 'MAX')
    ax5.text(0.0, -0.55, f"     TOP-5 MAX T\n#1: {str(int(round(top_5[0], 0)))} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    top_5, dates = xm.rank_top_5(df, 'MIN')
    ax5.text(0.15, -0.55, f"     TOP-5 MIN T\n#1: {str(int(round(top_5[0], 0)))} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    top_5, dates = xm.rank_top_5(df, 'AVG')
    ax5.text(0.3, -0.55, f"     TOP-5 AVG T\n#1: {str(top_5[0])} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(top_5[1])} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(top_5[2])} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(top_5[3])} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(top_5[4])} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    top_5, dates = xm.rank_top_5(df, 'DEP')
    ax5.text(0.0, -1.07, f"     TOP-5 T DEP\n#1: {str(top_5[0])} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(top_5[1])} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(top_5[2])} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(top_5[3])} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(top_5[4])} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    top_5, dates = xm.rank_top_5(df, 'HDD')
    ax5.text(0.2, -1.07, f"     TOP-5 HDD\n#1: {str(int(round(top_5[0], 0)))} - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))}- {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))} - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))} - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))} - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)


    top_5, dates = xm.rank_top_5(df, 'CDD')
    ax5.text(0.35, -1.07, f"     TOP-5 CDD\n#1: {str(int(round(top_5[0], 0)))} - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(top_5[1], 0)))} - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(top_5[2], 0)))} - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(top_5[3], 0)))} - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(top_5[4], 0)))} - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    bottom_5, dates = xm.rank_bottom_5(df, 'MAX')
    ax5.text(0.55, -0.55, f"     BOTTOM-5 MAX T\n#1: {str(int(round(bottom_5[0], 0)))} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    bottom_5, dates = xm.rank_bottom_5(df, 'MIN')
    ax5.text(0.7, -0.55, f"     BOTTOM-5 MIN T\n#1: {str(int(round(bottom_5[0], 0)))} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    bottom_5, dates = xm.rank_bottom_5(df, 'AVG')
    ax5.text(0.85, -0.55, f"     BOTTOM-5 AVG T\n#1: {str(bottom_5[0])} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(bottom_5[1])} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(bottom_5[2])} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(bottom_5[3])} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(bottom_5[4])} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    bottom_5, dates = xm.rank_bottom_5(df, 'DEP')
    ax5.text(0.55, -1.07, f"     BOTTOM-5 T DEP\n#1: {str(bottom_5[0])} [°F] - {dates[0].strftime(f'%b %d')}\n#2: {str(bottom_5[1])} [°F] - {dates[1].strftime(f'%b %d')}\n#3: {str(bottom_5[2])} [°F] - {dates[2].strftime(f'%b %d')}\n#4: {str(bottom_5[3])} [°F] - {dates[3].strftime(f'%b %d')}\n#5: {str(bottom_5[4])} [°F] - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    bottom_5, dates = xm.rank_bottom_5(df, 'HDD')
    ax5.text(0.72, -1.07, f"     BOTTOM-5 HDD\n#1: {str(int(round(bottom_5[0], 0)))} - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))} - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))} - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))} - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))} - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)


    bottom_5, dates = xm.rank_bottom_5(df, 'CDD')
    ax5.text(0.87, -1.07, f"     BOTTOM-5 CDD\n#1: {str(int(round(bottom_5[0], 0)))} - {dates[0].strftime(f'%b %d')}\n#2: {str(int(round(bottom_5[1], 0)))} - {dates[1].strftime(f'%b %d')}\n#3: {str(int(round(bottom_5[2], 0)))} - {dates[2].strftime(f'%b %d')}\n#4: {str(int(round(bottom_5[3], 0)))} - {dates[3].strftime(f'%b %d')}\n#5: {str(int(round(bottom_5[4], 0)))} - {dates[4].strftime(f'%b %d')}", fontsize=9, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)   
    
    img_path, img_path_print = update_image_file_paths(station, product_type, 'Temperature Summary')
    fname = f"{station.upper()}_{product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    print(f"Saved {fname} to {img_path_print}")

def plot_precipitation_summary(station, product_type, start_date=None, end_date=None):

    r'''
    This function plots a graphic showing the Precipitation Summary for a given station for a given time period. 

    Required Arguments:

    1) station (String) - The identifier of the ACIS2 station. 
    2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
       A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

    Optional Arguments:
    1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)
    2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

    '''

    try:
        today = datetime.now(UTC)
    except Exception as e:
        today = datetime.utcnow()


    if product_type == 'Past 7 Days' or product_type == 7:

        product_type = 'Past 7 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=9)
        d = 7
        decimate = 1

    elif product_type == 'Past 10 Days' or product_type == 10:

        product_type = 'Past 10 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=12) 
        d = 10
        decimate = 1

    elif product_type == 'Past 15 Days' or product_type == 15:

        product_type = 'Past 15 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=17)  
        d = 15
        decimate = 1

    elif product_type == 'Past 30 Days' or product_type == 30:

        product_type = 'Past 30 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=32)   
        d = 30
        decimate = 1

    elif product_type == 'Past 60 Days' or product_type == 60:

        product_type = 'Past 60 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=62)  
        d = 60
        decimate = 2

    elif product_type == 'Past 90 Days' or product_type == 90:

        product_type = 'Past 90 Days'
        end_date = today - timedelta(days=2)
        start_date = today - timedelta(days=92) 
        d = 90
        decimate = 5

    else:
        start_date = start_date
        end_date = end_date
        t1 = datetime.strptime(start_date, '%Y-%m-%d')
        t2 = datetime.strptime(end_date, '%Y-%m-%d')
        d1 = t1.day
        d2 = t2.day
        d = abs(d2 - d1)

    csv_fname = f"{station}_{product_type}.csv"

    path, path_print = update_csv_file_paths(station, product_type)

    try:
        if os.path.exists(f"{path}/{csv_fname}"):
            os.remove(f"{path}/{csv_fname}")
        else:
            pass
    except Exception as e:
        pass    

    df, start_date, end_date, df_days = xm.xmacis_to_df(station, start_date, end_date, 'PCP')

    file = df.to_csv(csv_fname, index=False)
    os.replace(f"{csv_fname}", f"{path}/{csv_fname}")

    df = pd.read_csv(f"{path}/{csv_fname}")
    df['DATE'] = pd.to_datetime(df['DATE'])

    missing_days = df_days

    means = xm.get_means(df)
    maxima = xm.get_maxima(df)
    minima = xm.get_minima(df)
    precip_sum = xm.get_precipitation_sum(df)

    top_5, dates = xm.rank_top_5(df, 'PCP')

    fig = plt.figure(figsize=(14,8))
    fig.set_facecolor('aliceblue')
    gs = gridspec.GridSpec(10, 10)

    fig.suptitle(f"{station.upper()} Precipitation Summary [{product_type.upper()}]", fontsize=18, fontweight='bold')

    ax1 = fig.add_subplot(1,1,1)
    ax1.xaxis.set_major_formatter(md.DateFormatter('%m/%d'))
    ax1.text(0.35, 1.065, f"Valid: {start_date} to {end_date}", fontsize=12, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.425, 1.04, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.01, -0.07, f"DAILY MAX = {str(maxima[6])} [IN] DAILY MEAN = {str(means[6])} [IN] TOTAL SUM = {precip_sum} [IN]", fontsize=7, fontweight='bold', transform=ax1.transAxes, bbox=props, zorder=1)
    ax1.text(0.44, -0.08, f"                                                                   TOP 5 WETTEST DAYS\n#1: {str(top_5[0])} [IN] - {dates[0].strftime(f'%b %d')} #2: {str(top_5[1])} [IN] - {dates[1].strftime(f'%b %d')} #3: {str(top_5[2])} [IN] - {dates[2].strftime(f'%b %d')} #4: {str(top_5[3])} [IN] - {dates[3].strftime(f'%b %d')} #5: {str(top_5[4])} [IN] - {dates[4].strftime(f'%b %d')}", fontsize=7, fontweight='bold', transform=ax1.transAxes, bbox=props, zorder=10)
    ax1.text(0.0001, 1.01, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax1.transAxes, bbox=props)
    ax1.axhline(y=maxima[6], color='darkgreen', linestyle='--', zorder=1, alpha=0.5)
    ax1.axhline(y=means[6], color='dimgrey', linestyle='--', zorder=1, alpha=0.5)

    plt.bar(df['DATE'], df['PCP'])
    bars = plt.bar(df['DATE'], df['PCP'], color='green')
    plt.bar_label(bars)

    img_path, img_path_print = update_image_file_paths(station, product_type, 'Precipitation Summary')
    fname = f"{station.upper()}_{product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    print(f"Saved {fname} to {img_path_print}")
