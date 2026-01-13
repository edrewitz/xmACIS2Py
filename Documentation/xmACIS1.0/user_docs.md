***xmACIS2Py < 2.0 (Legacy) Documentation and Jupyter Lab Tutorials***
***Jupyter Lab Tutorials***

1) In this example we will make 30 and 90-day temperature and precipitation summaries for KRAL - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/KRAL.ipynb)
2) In this example we will use a custom date range (via changing the optional arguments) and make a temperature and precipitation graphic for PASN (This also is an example with missing data!") - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/PASN.ipynb)
3) In this example we will remove the running mean from a temperature summary (via changing the optional arguments) for KJFK - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/running_mean.ipynb)
4) In this example we will add the running sum to a precipitation summary graphic (via changing the optional arguments) for KRAL - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/running_sum.ipynb)
5) In this example we will plot the maximum temperature summary for KLAX - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/LAX.ipynb)
6) In this example we will plot the minimum temperature summary for KONT - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/ONT.ipynb)
7) In this example we will plot the average temperature summary for KSTC - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/avg.ipynb)
8) In this example we will plot the average temperature departure summary for KSTC - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/avg_dep.ipynb)
9) In this example we will plot the heating degree days summary for KRAL - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/hdd.ipynb)
10) In this example we will plot the cooling degree days summary for KBRO - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/cdd.ipynb)
11) In this example we will plot the growing degree days summary for KBRO - [click here](https://github.com/edrewitz/xmACIS2Py-Jupyter-Lab-Tutorials/blob/main/Tutorials/gdd.ipynb)

**Documentation**

***plot_temperature_summary(station, product_type)***

This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

***plot_precipitation_summary(station, product_type)***

This function plots a graphic showing the Precipitation Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_sum (Boolean) - Default = False. When set to True, running sums will be shown

***plot_maximum_temperature_summary(station, product_type)***

This function plots a graphic showing the Maximum Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

***plot_minimum_temperature_summary(station, product_type)***

This function plots a graphic showing the Minimum Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

***plot_average_temperature_summary(station, product_type)***

This function plots a graphic showing the Average Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

***plot_average_temperature_departure_summary(station, product_type)***

This function plots a graphic showing the Average Temperature Departure Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

***plot_hdd_summary(station, product_type)***

This function plots a graphic showing the Heating Degree Days Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means and sums will be hidden

***plot_cdd_summary(station, product_type)***

This function plots a graphic showing the Cooling Degree Days Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means and sums will be hidden

***plot_gdd_summary(station, product_type)***

This function plots a graphic showing the Growing Degree Days Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means and sums will be hidden
