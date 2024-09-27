import pandas as pd
df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name = 'Flight')

df_filtered = df[df['days'] != 'wed']

df_filtered['Route'] = df_filtered[['Departure airport 3code', 'Arrival airport 3code']].apply(lambda x: tuple(sorted(x)), axis=1)

unique_routes_count = df_filtered['Route'].nunique()
print(f"Number of unique routes (excluding Wednesday): {unique_routes_count}")

df_filtered['duration'] = df_filtered['duration'].astype(str).fillna('00:00')

def duration_to_minutes(duration_str):
    if ':' in duration_str:  # Check if the duration has a colon
        hours, minutes = map(int, duration_str.split(':'))
        return hours * 60 + minutes
    return 0  

df_filtered['DurationInMinutes'] = df_filtered['duration'].apply(duration_to_minutes)

min_duration = df_filtered['DurationInMinutes'].min()

shortest_flights = df_filtered[df_filtered['DurationInMinutes'] == min_duration]
shortest_airlines = shortest_flights['Airline 2code'].unique()

print("\nAirlines with the shortest duration flights:")
print(shortest_airlines)
