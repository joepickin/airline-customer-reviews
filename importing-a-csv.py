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

# preview the first 5 rows
print(airline_raw_df.head())

# show the data types
print(airline_raw_df.dtypes)