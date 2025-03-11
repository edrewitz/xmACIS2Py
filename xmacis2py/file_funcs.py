import os
import warnings
warnings.filterwarnings('ignore')

def update_csv_file_paths(station, product_type):

    r'''
    This function creates the file path for the data files.

    Required Arguments:

    1) station (String) - The Station ID

    2) product_type (String) - The type of summary (30 Day, 90 Day etc.)

    Returns: A file path for the graphic to save: f:ACIS Data/{station}/{product_type}

    '''

    if os.path.exists(f"ACIS Data"):
        pass
    else:
        os.mkdir(f"ACIS Data")

    if os.path.exists(f"ACIS Data/{station}"):
        pass
    else:
        os.mkdir(f"ACIS Data/{station}")

    if os.path.exists(f"ACIS Data/{station}/{product_type}"):
        pass
    else:
        os.mkdir(f"ACIS Data/{station}/{product_type}")

    path = f"ACIS Data/{station}/{product_type}"
    path_print = f"f:ACIS Data/{station}/{product_type}"

    return path, path_print

def update_image_file_paths(station, product_type, plot_type, show_running_data, running_type=None):

    r'''
    This function creates the file path for the graphics files.

    Required Arguments:

    1) station (String) - The Station ID

    2) product_type (String) - The type of summary (30 Day, 90 Day etc.)

    3) plot_type (String) - The type of summary (i.e. temperature or precipitation)

    4) show_running_data (Boolean) - Makes the file path take into account if users are choosing to show running means and/or sums

    5) running_type (String) - Default = None. If the user is showing running data, they must specify either Mean or Sum.
       If set to None, the path will say running data rather than running mean or running sum. 

    Returns: A file path for the graphic to save: f:ACIS Graphics/{station}/{product_type}/{plot_type}

    '''

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
        
    if os.path.exists(f"ACIS Graphics"):
        pass
    else:
        os.mkdir(f"ACIS Graphics")

    if os.path.exists(f"ACIS Graphics/{station}"):
        pass
    else:
        os.mkdir(f"ACIS Graphics/{station}")

    if os.path.exists(f"ACIS Graphics/{station}/{product_type}"):
        pass
    else:
        os.mkdir(f"ACIS Graphics/{station}/{product_type}")

    if os.path.exists(f"ACIS Graphics/{station}/{product_type}/{plot_type} {text}"):
        pass
    else:
        os.mkdir(f"ACIS Graphics/{station}/{product_type}/{plot_type} {text}")

    path = f"ACIS Graphics/{station.upper()}/{product_type}/{plot_type} {text}"
    path_print = f"f:ACIS Graphics/{station.upper()}/{product_type}/{plot_type} {text}"

    return path, path_print    
