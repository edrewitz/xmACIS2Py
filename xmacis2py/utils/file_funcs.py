"""
xmACIS2Py is software that makes visualizations of ACIS2 data for any station in the ACIS2 database. 

This is the file that holds the functions that build the directories to save the CSV files and graphics.  

This file was written by: (C) Meteorologist Eric J. Drewitz
                                       USDA/USFS

"""
import os
import warnings
warnings.filterwarnings('ignore')

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
        os.makedirs(f"ACIS Data/{station}/{product_type}")
    except Exception as e:
        pass

    path = f"ACIS Data/{station}/{product_type}"

    return path

def update_image_file_paths(station, 
                            product_type, 
                            plot_type, 
                            show_running_data, 
                            running_type=None):

    """
    This function creates the file path for the graphics files.

    Required Arguments:

    1) station (String) - The Station ID

    2) product_type (String) - The type of summary (30 Day, 90 Day etc.)

    3) plot_type (String) - The type of summary (i.e. temperature or precipitation)

    4) show_running_data (Boolean) - Makes the file path take into account if users are choosing to show running means and/or sums
    
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
        
    try:
        os.makedirs(path = f"ACIS Graphics/{station.upper()}/{product_type}/{plot_type} {text}")
    except Exception as e:
        pass

    path = f"ACIS Graphics/{station.upper()}/{product_type}/{plot_type} {text}"

    return path







