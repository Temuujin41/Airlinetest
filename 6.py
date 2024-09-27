import pandas as pd

data_df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name='Data')
column_df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name='Column')

user_from = input("Enter your departure airport code (From): ")
user_to = input("Enter your arrival airport code (To): ")
travel_date = input("Enter your travel date (YYYY-MM-DD): ")

flights_filtered = data_df[(data_df['Departure airport 3code'] == user_from) &
                           (data_df['Arrival airport 3code'] == user_to) &
                           (data_df['Date'] == travel_date)]

if not flights_filtered.empty:
    shortest_flight = flights_filtered.loc[flights_filtered['duration'].idxmin()]
    total_duration = flights_filtered['duration'].sum()
    available_airlines = flights_filtered['Airline 2code'].unique()

    print(f"\nShortest Flight:\n{shortest_flight[['Departure airport 3code', 'Arrival airport 3code', 'Airline 2code', 'duration']]}")
    print(f"Total Duration of Flights: {total_duration}")
    print("Available Airlines:", available_airlines)
else: 
    print("No flights found for the specified criteria.")
