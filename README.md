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
> For all of the datasets below, examine the data types of each column, ensure that the dates are in the proper format, and set the dataframe's index to the date column as appropriate.
 
For this exercise you'll need to install a library that will provide us access to some more datasets:

`pip install vega_datasets`
You can use this library like so:
from vega_datasets import data
data.sf_temps()

## Use the above (`sf_temps`) dataset for the exercises below:

## Resample by the day and take the average temperature. Visualize the average temperature over time.

## Write the code necessary to visualize the minimum temperature over time.
## Write the code necessary to visualize the maximum temperature over time.
## Which month is the coldest, on average?
## Which month has the highest average temperature?
## Resample by the day and calculate the min and max temp for the day (Hint: .agg(['min', 'max'])). 
* Use this resampled dataframe to calculate the change in temperature for the day
## Which month has the highest daily temperature variability?

#  Bonus: Visualize the daily min, average, and max temperature over time on a single line plot, i.e. the min, average, and maximum temperature should be 3 seperate lines.

from vega_datasets import data
data.seattle_weather()
Use the dataset to answer the following questions:

Which year and month combination has the highest amount of precipitation?
Visualize the amount of monthly precipitation over time.
Visualize the amount of wind over time. Choose a time interval you think is appropriate.
Which year-month combination is the windiest?
What's the sunniest year? (Hint: which day has the highest number of days where weather == sun?)
In which month does it rain the most?
Which month has the most number of days with a non-zero amount of precipitation?

data.flights_20k()
Convert any negative delays to 0.
Which hour of the day has the highest average delay?
Does the day of the week make a difference in the delay amount?
Does the month make a difference in the delay amount?