# time-series-exercises
* Repository holds excercises from the Time Series module for codeup

# Data Acquisition: Excercises
Create a new local git repository and remote repository on github named time-series-exercises. 
Save this work for this module in your time-series-exercises repo.
The end result of this exercise should be a file named acquire.py.

## Using the code from the lesson as a guide and the REST API from https://python.zgulde.net/api/v1/items as we did in the lesson, create a dataframe named items that has all of the data for items.
## Do the same thing, but for stores (https://python.zgulde.net/api/v1/stores)
## Extract the data for sales (https://python.zgulde.net/api/v1/sales). 
* There are a lot of pages of data here, so your code will need to be a little more complex.  
* Your code should continue fetching data from the next page until all of the data is extracted.
* Save the data in your files to local csv files so that it will be faster to access in the future.
## Combine the data from your three separate dataframes into one large dataframe.
## Acquire the Open Power Systems Data for Germany, which has been rapidly expanding its renewable energy production in recent years. 
* The data set includes country-wide totals of electricity consumption, wind power production, and solar power production for 2006-2017. 
* You can get the data here: https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv
## Make sure all the work that you have done above is reproducible. 
* That is, you should put the code above into separate functions in the acquire.py file and be able to re-run the functions and get the same data.

------------
# Working with Time Series Data: Exercises