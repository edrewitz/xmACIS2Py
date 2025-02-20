![image](https://github.com/user-attachments/assets/fb5ecdf9-bd51-4243-be7d-92af0952bfd8) ![image](https://github.com/user-attachments/assets/da1b43c0-2b6a-4a5c-9eb4-f08b30cab42b)




# xmACIS2Py
**Creating xmACIS2 Summary Graphics in Python**

### Table Of Contents

1) [plot_temperature_summary(station, product_type)](#plot_temperature_summarystation-product_type)
2) [plot_precipitation_summary(station, product_type)](#plot_precipitation_summarystation-product_type)


#### plot_temperature_summary(station, product_type)

This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 
2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
   A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:
1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)
2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

#### plot_precipitation_summary(station, product_type)

This function plots a graphic showing the Precipitation Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 
2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
   A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:
1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)
2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)
