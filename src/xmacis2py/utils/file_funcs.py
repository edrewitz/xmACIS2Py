"""
This file hosts the file management for the graphics.  

(C) Eric J. Drewitz 2025

"""
import os
import warnings
warnings.filterwarnings('ignore')

folder = os.getcwd()
folder_modified = folder.replace("\\", "/")

def update_csv_file_paths(station, 
                          product_type):

    """
    This function creates the file path for the data files.

    Required Arguments:

    1) station (String) - The Station ID

    2) product_type (String) - The type of summary (30 Day, 90 Day etc.)

    Returns
    -------
    
    A file path for the graphic to save: f:ACIS Data/{station}/{product_type}
    """

    try:
        os.makedirs(f"{folder_modified}/ACIS Data/{station}/{product_type}")
    except Exception as e:
        pass

    path = f"{folder_modified}/ACIS Data/{station}/{product_type}"

    return path

def update_image_file_paths(station, 
                            product_type, 
                            plot_type, 
                            show_running_data,
                            detrend_series, 
                            detrend_type,
                            running_type=None):

    """
    This function creates the file path for the graphics files.

    Required Arguments:

    1) station (String) - The Station ID

    2) product_type (String) - The type of summary (30 Day, 90 Day etc.)

    3) plot_type (String) - The type of summary (i.e. temperature or precipitation)

    4) show_running_data (Boolean) - Makes the file path take into account if users are choosing to show running means and/or sums
    
    5) detrend_series (Boolean) - When set to True the data is detrended. 
    
    6) detrend_type (String) - The type of detrending. 
        If type == 'linear' (default), the result of a linear least-squares fit to data is subtracted from data. 
        If type == 'constant', only the mean of data is subtracted.
    
    Optional Arguments:

    1) running_type (String) - Default = None. If the user is showing running data, they must specify either Mean or Sum.
       If set to None, the path will say running data rather than running mean or running sum. 
       

    Returns 
    -------
    
    A file path for the graphic to save: f:ACIS Graphics/{station}/{product_type}/{plot_type}
    """

    if show_running_data == True:
        if running_type == 'Mean':
            text = f"With Running Mean"
        if running_type == 'Sum':
            text = f"With Running Sum"
        if running_type == None:
            text = f"With Running Data"        
    else:
        if running_type == 'Mean':
            text = f"Without Running Mean"
        if running_type == 'Sum':
            text = f"Without Running Sum"
        if running_type == None:
            text = f"Without Running Data" 
            
    if detrend_series == False:
        trend = f"No Detrending"
    else:
        trend = f"{detrend_type.upper()} Detrending"
        
    try:
        os.makedirs(f"{folder_modified}/ACIS Graphics/{station.upper()}/{product_type}/{plot_type} {text} {trend}")
    except Exception as e:
        pass

    path = f"{folder_modified}/ACIS Graphics/{station.upper()}/{product_type}/{plot_type} {text} {trend}"

    return path







