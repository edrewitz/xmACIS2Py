import os

def update_csv_file_paths(station, product_type):

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

def update_image_file_paths(station, product_type):

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

    path = f"ACIS Graphics/{station.upper()}/{product_type}"
    path_print = f"f:ACIS Graphics/{station.upper()}/{product_type}"

    return path, path_print    