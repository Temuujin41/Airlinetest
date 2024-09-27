import pandas as pd
df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name = 'Flight')

df['dep_time'] = df['dep_time'].astype(str).str.slice(0, 5)  

df['dep_time'] = pd.to_datetime(df['dep_time'], format='%H:%M', errors='coerce').dt.time

start_time = pd.to_datetime('15:00', format='%H:%M').time()
end_time = pd.to_datetime('21:00', format='%H:%M').time()
exclude_start = pd.to_datetime('18:00', format='%H:%M').time()
exclude_end = pd.to_datetime('19:00', format='%H:%M').time()

filtered_df = df[(df['dep_time'] >= start_time) &
                 (df['dep_time'] < end_time) &
                 ~((df['dep_time'] >= exclude_start) &
                   (df['dep_time'] < exclude_end))]

available_airports = filtered_df['Departure airport 3code'].unique()
available_airlines = filtered_df['Airline 2code'].unique()

print("Airports 15:00 and 21:00, excluding 18:00 to 19:00:")
print(available_airports)

print("\n Airlines 15:00 and 21:00, excluding 18:00 to 19:00:")
print(available_airlines)
