"""
This file hosts functions that print out error messages to the user

(C) Eric J. Drewitz 2025-2026
"""
from datetime import datetime

def _call_counter(func):
    """
    Checks how many time a function is called.
    """
    def _wrapper(*args, **kwargs):
        _wrapper.calls += 1
        return func(*args, **kwargs)
    _wrapper.calls = 0
    return _wrapper

@_call_counter
def climo_normals_year_error(start_date,
                             end_date,
                             interval,
                             call):
    
    """
    Prints an error to the user regarding usng a period with different years for downloading the climo normals.
    
    Required Arguments: 
    
    1) start_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
        
    2) end_date (String or Datetime) - Default=None. For users who want specific start and end dates for their analysis,
        they can either be passed in as a string in the format of 'YYYY-mm-dd' or as a datetime object.
    
    """
    interval = interval.lower()
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')    
    
    if interval != 'yearly':
        if call == 0:
            print(f"The years of the start_year ({start_date.strftime('%Y')}) and end_year ({end_date.strftime('%Y')}) variables must match.")
            print(f"The data for ({start_date.strftime('%Y')}) will be the same as ({end_date.strftime('%Y')}).")
            print(f"These are the {interval} 30-year climatological normals.")
            print(f"Defaulting to using {end_date.strftime('%Y')} for both years.")
        else:
            pass
    else:
        if call == 0:
            print(f"The data from ({start_date.strftime('%Y')}) to ({end_date.strftime('%Y')}) is the same.")
            print(f"This is the climatological normal for an entire year.")
        else:
            pass
    
def return_call_counter():
    call = climo_normals_year_error.calls
    return call
