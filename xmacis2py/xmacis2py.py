import matplotlib as mpl
import matplotlib.dates as md
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import metpy.calc as mpcalc
import numpy as np
import pandas as pd
import os
import xmacis2py.xmacis_data as xm

from xmacis2py.file_funcs import update_csv_file_paths, update_image_file_paths
try:
    from datetime import datetime, timedelta, UTC
except Exception as e:
    from datetime import datetime, timedelta

mpl.rcParams['font.weight'] = 'bold'
mpl.rcParams['xtick.labelsize'] = 5
mpl.rcParams['ytick.labelsize'] = 5
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

    if product_type == 'Custom' or product_type == 'custom':

        if end_date.year == today.year and end_date.month == today.month and end_date.day == today.day:
            end_date = end_date - timedelta(days=2)
    
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

    elif product_type == 'Past 7 Days' or product_type == 7:

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

    csv_fname = f"{station}_{product_type}.csv"

    path, path_print = update_csv_file_paths(station, product_type)

    try:
        if os.path.exists(f"{path}/{csv_fname}"):
            os.remove(f"{path}/{csv_fname}")
            print(f"Removed {csv_fname} from {path_print}.")
        else:
            pass
    except Exception as e:
        pass    

    df, start_date, end_date = xm.xmacis_to_csv(station, start_date, end_date)

    file = df.to_csv(csv_fname, index=False)
    os.replace(f"{csv_fname}", f"{path}/{csv_fname}")
    print(f"Saved {csv_fname} to {path_print}.")

    df = pd.read_csv(f"{path}/{csv_fname}")

    missing_days = d - (len(df) - 1)

    print(f"There are {missing_days} missing days of data.")

    means = xm.get_means(df)
    maxima = xm.get_maxima(df)
    minima = xm.get_minima(df)
    hdd_sum, cdd_sum = xm.get_sum_hdd_cdd(df)

    fig = plt.figure(figsize=(14,14))
    fig.set_facecolor('aliceblue')
    gs = gridspec.GridSpec(10, 10)

    fig.suptitle(f"{station.upper()} Temperature Summary [{product_type.upper()}]", fontsize=18, fontweight='bold')

    ax1 = fig.add_subplot(gs[0:2, 0:10])
    ax1.set_title(f"Daily Maximum Temperature [°F]", fontweight='bold', y=0.88, alpha=0.7, loc='left', zorder=11)
    ax1.xaxis.set_major_formatter(md.DateFormatter('%d'))
    ax1.plot(df['DATE'], df['MAX'], color='red', zorder=5)
    ax1.text(0.35, 1.45, f"Valid: {start_date} to {end_date}", fontsize=12, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.425, 1.37, f"Missing Days = {str(missing_days)}", fontsize=9, fontweight='bold', transform=ax1.transAxes)
    ax1.text(0.94, 0.85, f"MAX = {str(maxima[0])} [°F]\nMEAN = {str(means[0])} [°F]\nMIN = {str(minima[0])} [°F]", fontsize=5, fontweight='bold', transform=ax1.transAxes, bbox=props, zorder=10)
    ax1.text(0.01, 1.02, f"Plot Created with xmACIS2Py (C) Eric J. Drewitz {utc.strftime('%Y')} | Data Source: xmACIS2 | Image Creation Time: {utc.strftime('%Y-%m-%d %H:%MZ')}", fontsize=6, fontweight='bold', transform=ax1.transAxes, bbox=props)
    ax1.axhline(y=maxima[0], color='darkred', linestyle='--', zorder=1, alpha=0.5)
    ax1.axhline(y=means[0], color='dimgrey', linestyle='--', zorder=1, alpha=0.5)
    ax1.axhline(y=minima[0], color='darkblue', linestyle='--', zorder=1, alpha=0.5)

    ax2 = fig.add_subplot(gs[2:4, 0:10])
    ax2.set_title(f"Daily Minimum Temperature [°F]", fontweight='bold', y=0.88, alpha=0.7, loc='left', zorder=11)
    ax2.xaxis.set_major_formatter(md.DateFormatter('%d'))
    ax2.plot(df['DATE'], df['MIN'], color='blue', zorder=5)
    ax2.text(0.94, 0.85, f"MAX = {str(maxima[1])} [°F]\nMEAN = {str(means[1])} [°F]\nMIN = {str(minima[1])} [°F]", fontsize=5, fontweight='bold', transform=ax2.transAxes, bbox=props, zorder=10)
    ax2.axhline(y=maxima[1], color='darkred', linestyle='--', zorder=1, alpha=0.5)
    ax2.axhline(y=means[1], color='dimgrey', linestyle='--', zorder=1, alpha=0.5)
    ax2.axhline(y=minima[1], color='darkblue', linestyle='--', zorder=1, alpha=0.5)

    ax3 = fig.add_subplot(gs[4:6, 0:10])
    ax3.set_title(f"Daily Average Temperature [°F]", fontweight='bold', y=0.88, alpha=0.7, loc='left', zorder=11)
    ax3.xaxis.set_major_formatter(md.DateFormatter('%d'))
    ax3.plot(df['DATE'], df['AVG'], color='grey', zorder=5)
    ax3.text(0.93, 0.85, f"MAX = {str(maxima[2])} [°F]\nMEAN = {str(means[2])} [°F]\nMIN = {str(minima[2])} [°F]", fontsize=5, fontweight='bold', transform=ax3.transAxes, bbox=props, zorder=10)
    ax3.axhline(y=maxima[2], color='darkred', linestyle='--', zorder=1, alpha=0.5)
    ax3.axhline(y=means[2], color='dimgrey', linestyle='--', zorder=1, alpha=0.5)
    ax3.axhline(y=minima[2], color='darkblue', linestyle='--', zorder=1, alpha=0.5)

    ax4 = fig.add_subplot(gs[6:8, 0:10])
    ax4.set_title(f"Daily Temperature Departure [°F]", fontweight='bold', y=0.88, alpha=0.7, loc='left', zorder=11)
    ax4.xaxis.set_major_formatter(md.DateFormatter('%d'))
    ax4.plot(df['DATE'], df['DEP'], color='black', zorder=5)
    ax4.text(0.94, 0.85, f"MAX = {str(maxima[3])} [°F]\nMEAN = {str(means[3])} [°F]\nMIN = {str(minima[3])} [°F]", fontsize=5, fontweight='bold', transform=ax4.transAxes, bbox=props, zorder=10)
    ax4.axhline(y=maxima[2], color='darkred', linestyle='--', zorder=1, alpha=0.5)
    ax4.axhline(y=means[2], color='dimgrey', linestyle='--', zorder=1, alpha=0.5)
    ax4.axhline(y=minima[2], color='darkblue', linestyle='--', zorder=1, alpha=0.5)

    ax5 = fig.add_subplot(gs[8:10, 0:10])
    ax5.set_title(f"HDD [Red] & CDD [Blue]", fontweight='bold', y=0.88, alpha=0.7, loc='left', zorder=11)
    ax5.xaxis.set_major_formatter(md.DateFormatter('%d'))
    ax5.plot(df['DATE'], df['HDD'], color='darkred', zorder=5)
    ax5.plot(df['DATE'], df['CDD'], color='darkblue', zorder=5)
    ax5.text(0.935, 0.9, f"Total HDD = {str(hdd_sum)}\nTotal CDD = {str(cdd_sum)}", fontsize=5, fontweight='bold', transform=ax5.transAxes, bbox=props, zorder=10)

    img_path, img_path_print = update_image_file_paths(station, product_type)
    fname = f"{station.upper()}_{product_type}.png"
    fig.savefig(f"{img_path}/{fname}", bbox_inches='tight')
    print(f"Saved {fname} to {img_path_print}")

