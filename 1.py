import pandas as pd
df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name = 'Flight')
df['Route'] = df.apply(lambda row: tuple(sorted([row['Departure airport 3code'], row['Arrival airport 3code']])), axis=1)
unique_routes = df.drop_duplicates(subset='Route')
unique_route_count = unique_routes['Route'].nunique()
print(f"unique routes: {unique_route_count}")