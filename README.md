# xmACIS2Py
**Creating xmACIS2 Summary Graphics in Python**

### Table Of Contents

1) [plot_temperature_summary(station, product_type)](#plot_temperature_summarystation-product_type)


#### plot_temperature_summary(station, product_type)

This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 
2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
   A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:
1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)
2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)
