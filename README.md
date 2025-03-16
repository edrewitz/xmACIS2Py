![image](https://github.com/user-attachments/assets/fb5ecdf9-bd51-4243-be7d-92af0952bfd8) ![image](https://github.com/user-attachments/assets/da1b43c0-2b6a-4a5c-9eb4-f08b30cab42b)

<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/version.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/latest_release_date.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/platforms.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/license.svg" /> </a>
<a href="https://anaconda.org/conda-forge/xmacis2py"> <img src="https://anaconda.org/conda-forge/xmacis2py/badges/downloads.svg" /> </a>


# xmACIS2Py
**Creating xmACIS2 Summary Graphics in Python**

### Jupyter Lab Tutorials

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

### Table Of Contents

1) [plot_temperature_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/tree/main?tab=readme-ov-file#plot_temperature_summarystation-product_type)
2) [plot_precipitation_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/tree/main?tab=readme-ov-file#plot_precipitation_summarystation-product_type)
3) [plot_maximum_temperature_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_maximum_temperature_summarystation-product_type)
4) [plot_minimum_temperature_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_minimum_temperature_summarystation-product_type)
5) [plot_average_temperature_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_average_temperature_summarystation-product_type)
6) [plot_average_temperature_departure_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_average_temperature_departure_summarystation-product_type)
7) [plot_hdd_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_hdd_summarystation-product_type)
8) [plot_cdd_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_cdd_summarystation-product_type)
9) [plot_gdd_summary(station, product_type)](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#plot_gdd_summarystation-product_type)
10) [References](https://github.com/edrewitz/xmACIS2Py/blob/main/README.md#references)


#### plot_temperature_summary(station, product_type)

This function plots a graphic showing the Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

#### plot_precipitation_summary(station, product_type)

This function plots a graphic showing the Precipitation Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_sum (Boolean) - Default = False. When set to True, running sums will be shown

#### plot_maximum_temperature_summary(station, product_type)

This function plots a graphic showing the Maximum Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

#### plot_minimum_temperature_summary(station, product_type)

This function plots a graphic showing the Minimum Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

#### plot_average_temperature_summary(station, product_type)

This function plots a graphic showing the Average Temperature Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

#### plot_average_temperature_departure_summary(station, product_type)

This function plots a graphic showing the Average Temperature Departure Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means will be hidden

#### plot_hdd_summary(station, product_type):

This function plots a graphic showing the Heating Degree Days Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means and sums will be hidden

#### plot_cdd_summary(station, product_type):

This function plots a graphic showing the Cooling Degree Days Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means and sums will be hidden

#### plot_gdd_summary(station, product_type):

This function plots a graphic showing the Growing Degree Days Summary for a given station for a given time period. 

Required Arguments:

1) station (String) - The identifier of the ACIS2 station. 

2) product_type (String or Integer) - The type of product. 'Past 7 Days' as a string or enter 7 for the same result. 
 A value of 'custom' or 'Custom' will result in the user entering a custom start/stop date. 

Optional Arguments:

1) start_date (String) - Default=None. Enter the start date as a string (i.e. 01-01-2025)

2) end_date (String) - Default=None. Enter the end date as a string (i.e. 01-01-2025)

3) show_running_mean (Boolean) - Default = True. When set to False, running means and sums will be hidden

#### References


1) xmACIS2: https://www.rcc-acis.org/docs_webservices.html 

2) MetPy: May, R. M., Goebbert, K. H., Thielen, J. E., Leeman, J. R., Camron, M. D., Bruick, Z., Bruning, E. C., Manser, R. P., Arms, S. C., and Marsh, P. T., 2022: MetPy: A Meteorological Python Library for Data Analysis and Visualization. Bull. Amer. Meteor. Soc., 103, E2273-E2284, https://doi.org/10.1175/BAMS-D-21-0125.1.

3) NumPy: Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2. (Publisher link).

4) Pandas:
    author       = {The pandas development team},
    title        = {pandas-dev/pandas: Pandas},
    publisher    = {Zenodo},
    version      = {latest},
    doi          = {10.5281/zenodo.3509134},
    url          = {https://doi.org/10.5281/zenodo.3509134}
}
