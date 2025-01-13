import pandas as pd

# Path of the file to read
flight_filepath = "../data/flight_delays.csv"

# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")

print("Setup Complete")