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

def update_image_file_paths(station, product_type, plot_type):

    r'''
    This function creates the file path for the graphics files.

    Required Arguments:

    1) station (String) - The Station ID

    2) product_type (String) - The type of summary (30 Day, 90 Day etc.)

    3) plot_type (String) - The type of summary (i.e. temperature or precipitation)

    Returns: A file path for the graphic to save: f:ACIS Graphics/{station}/{product_type}/{plot_type}

    '''

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

    if os.path.exists(f"ACIS Graphics/{station}/{product_type}/{plot_type}"):
        pass
    else:
        os.mkdir(f"ACIS Graphics/{station}/{product_type}/{plot_type}")

    path = f"ACIS Graphics/{station.upper()}/{product_type}/{plot_type}"
    path_print = f"f:ACIS Graphics/{station.upper()}/{product_type}/{plot_type}"

    return path, path_print    
