import pandas as pd

data_df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name='Data')
column_df = pd.read_excel(r'C:\Users\temuu\Downloads\Telegram Desktop\PythonData.xlsx', sheet_name='Column')

column_names = column_df.iloc[:, 0].tolist()

split_columns = data_df.iloc[:, 1].str.split(',', expand=True)

for i in range(len(column_names)):
    if i < split_columns.shape[1]:
        split_columns.rename(columns={i: column_names[i]}, inplace=True)

for i in range(len(column_names), split_columns.shape[1]):
    split_columns.rename(columns={i: f'New Column {i - len(column_names) + 1}'}, inplace=True)

data_df = pd.concat([data_df.drop(data_df.columns[1], axis=1), split_columns], axis=1)

data_df.to_excel('updated_data.xlsx', index=False)

print("Data has been processed and saved to 'updated_data.xlsx'.") 
