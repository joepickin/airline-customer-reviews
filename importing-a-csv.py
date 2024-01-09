# Airlines Customer Satisfaction
# Source: kaggle
# https://www.kaggle.com/datasets/sjleshrac/airlines-customer-satisfaction

# Open the following folder in VSCode: /Users/josephpickin/Documents/GitHub/airline-customer-reviews"
# cd "/Users/josephpickin/Documents/GitHub/airline-customer-reviews"


# First, import pandas
import pandas as pd

# load the csv file Invistico_Airline.csv

airline_file_path = "Invistico_Airline.csv"
airline_raw_df = pd.read_csv(
    airline_file_path
)

# Explore the data

# preview the first 10 rows
print(airline_raw_df.head(10))

# show the data types
print(airline_raw_df.dtypes)#

# convert to the best possible data types
airline_df = airline_raw_df.convert_dtypes()
print(airline_df.dtypes)

# Get info about the dataset
print(airline_df.info())

# Add a new Id column using the index +1 (the +1 moves the first number from 0 to 1)
airline_df["Response Id"] = airline_df.index + 1
print(airline_df["Response Id"].head(10))

# Pivot from wide to long: this makes analyising survey data easier

# Find the response columns (all columns scored from 0-5) that we want to pivot.
response_columns = ['Seat comfort', 'Departure/Arrival time convenient', 'Food and drink', 'Gate location', 
                       'Inflight wifi service', 'Inflight entertainment', 'Online support', 'Ease of Online booking', 
                       'On-board service', 'Leg room service', 'Baggage handling', 'Checkin service', 'Cleanliness', 
                       'Online boarding']

# Everything else is info about the customer/ flight, plus the satisfaction column
categorical_columns = ['Response Id', 'satisfaction', 'Gender', 'Customer Type', 'Type of Travel', 'Class', "Age", 
                       "Flight Distance", "Departure Delay in Minutes", "Arrival Delay in Minutes"]

airline_long_df = pd.melt(airline_df, id_vars=categorical_columns, value_vars=response_columns)
print(airline_long_df.head(20))

# Sort by Response Id to make it look better
airline_long_df = airline_long_df.sort_values(by=['Response Id'])
print(airline_long_df.head(20))

# Convert the data types so variable is a string and value is an int64
airline_long_df = airline_long_df.convert_dtypes()
print(airline_long_df.dtypes)