import pandas as pd

flights_df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name='Flight')
airports_df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name='Airport')

user_from = input("Enter your departure airport code (From): ")
user_to = input("Enter your arrival airport code (To): ")

flights_filtered = flights_df[(flights_df['Departure airport 3code'] == user_from) &
                               (flights_df['Arrival airport 3code'] == user_to)]

flights_filtered['duration'] = flights_filtered['duration'].astype(str).fillna('00:00')

def duration_to_minutes(duration_str):
    if ':' in duration_str:  
        hours, minutes = map(int, duration_str.split(':'))
        return hours * 60 + minutes
    return 0  

flights_filtered['DurationInMinutes'] = flights_filtered['duration'].apply(duration_to_minutes)

if not flights_filtered.empty:
    shortest_duration_flight = flights_filtered.loc[flights_filtered['DurationInMinutes'].idxmin()]
    print(f"\nShortest duration flight:\n{shortest_duration_flight[['Departure airport 3code', 'Arrival airport 3code', 'Airline 2code', 'duration']]}")
else:
    print("No direct flights found for the specified route.")

user_airport_country = airports_df.loc[airports_df['IATA 3 Letter Airport Code'] == user_from, 'Country code'].values
if user_airport_country.size > 0:
    same_country_airports = airports_df[airports_df['Country code'] == user_airport_country[0]]
    print("\nSuggested alternative airports in the same country:")
    print(same_country_airports['IATA 3 Letter Airport Code'].tolist())
else:
    print("Country for the departure airport not found.")