## 2. Introduction to Ndarrays ##

import numpy as np
data_ndarray = np.array([10,20,30])

## 4. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)
print(taxi)

## 5. Array Shapes ##

taxi_shape = taxi.shape
print(taxi_shape)

## 6. Selecting and Slicing Rows and Items from Ndarrays ##

row_0 = taxi[0]
print(row_0)
rows_391_to_500 = taxi [391 : 501]
print(rows_391_to_500)
row_21_column_5 = taxi[21, 5]
print(row_21_column_5)

## 7. Selecting Columns and Custom Slicing Ndarrays ##

cols = (1,4,7)
columns_1_4_7 = taxi[:, cols]
print(columns_1_4_7)

row_99_columns_5_to_8 = taxi[99, 5:9]
print(row_99_columns_5_to_8)

rows_100_to_200_column_14 = taxi[100:201, 14]
print(rows_100_to_200_column_14)

## 8. Vector Math ##

fare_amount = taxi[:,9]
fees_amount = taxi[:,10]

fare_and_fees = fare_amount + fees_amount
print(fare_and_fees)

## 9. Vector Math (Continued) ##

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 

trip_mph = trip_distance_miles / trip_length_hours
print(trip_mph)

## 10. Calculating Statistics for 1D Ndarrays ##

mph_min = trip_mph.min()
print(mph_min)

mph_max = trip_mph.max()
print(mph_max)

mph_mean = trip_mph.mean()
print(mph_mean)

## 12. Calculating Statistics for 2D Ndarrays ##

# we'll compare against the first 5 rows only
taxi_first_five = taxi[:5]
# select these columns: fare_amount, fees_amount, tolls_amount, tip_amount
fare_components = taxi_first_five[:,9:13]

fare_sums = fare_components.sum(axis = 1)

fare_totals = taxi_first_five[:, 13]

print(fare_sums)
print(fare_totals)