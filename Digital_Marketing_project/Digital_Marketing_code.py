import pandas as pd
import numpy as np

df = pd.read_csv('File Date/Digital_Marketing_Row_Data.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df.head())
print('#' * 50)
print(df.shape)
print('#' * 50)
print(df.info())
print('#' * 50)
print(df.index)
print('#' * 50)
print(df.describe().T)
print('#' * 50)
print(df.isnull().sum())
print('#' * 50)


df.columns = df.columns.str.strip().str.replace(' ', '_').str.capitalize()
# print(df.head())
# print('#' * 50)


Text_columns = ['Lead_id', 'Channel', 'Campaign',
                'Region', 'Product', 'Customer_type']
for i in Text_columns:
    df[i] = df[i].astype(str).str.strip()
    df[i] = df[i].replace(('NAN', 'Nan', 'nan'), np.nan)
    df[i] = df[i].str.title()
print(df.head())
print('#' * 50)


df['Channel'] = df['Channel'].fillna(df['Channel'].mode()[0])
df['Campaign'] = df['Campaign'].fillna(df['Campaign'].mode()[0])
df['Region'] = df['Region'].fillna(df['Region'].mode()[0])
df['Ad_spend'] = df['Ad_spend'].fillna(df['Ad_spend'].median())
df['Clicks'] = df['Clicks'].fillna(df['Clicks'].median())
df['Leads'] = df['Leads'].fillna(df['Leads'].median())

print(df.isnull().sum())
print('#' * 50)
print(df.describe().T)
print('#' * 50)
print(df.head())

df['Date'] = pd.to_datetime(
    df['Date'],
    format='%d/%m/%Y',
    errors='coerce')
# print(df.head())


df['Date_of_Month'] = df['Date'].dt.to_period('M')
# print(df['Date_of_Month'])

df['Revenue_per_orders'] = round(df['Revenue'] / df['Orders'], 2)
# print(df['Revenue_per_orders'])

df['Cost_per_unit'] = round(df['Cogs'] / df['Orders'], 2)
# print(df['Cost_per_unit'])

df['Profit'] = df['Revenue'] - df['Cogs']
# print(df['Profit'])

print(df.head())

# KPI Analysis

# Total spend
print(f'Total spend = {df['Ad_spend'].sum()}')
print('#' * 50)

# Total Clicks
print(f'Total Clicks  = {df['Clicks'].sum()}')
print('#' * 50)

# Total Leads
print(f'Total Leads  = {df['Leads'].sum()}')
print('#' * 50)

# Total Orders
print(f'Total Orders  = {df['Orders'].sum()}')
print('#' * 50)

# Total Revenue
print(f'Total Revenue  = {df['Revenue'].sum()}')
print('#' * 50)

# Total  Cost of gods sold ->> COGS
print(f'COGS = {round(df['Cogs'].sum(), 2)}')
print('#' * 50)

# Click Trough Rate ->> CTR
CtR = (df['Clicks'].sum() / df['Impressions'].sum()) * 100.0
print(f'CTR = {round(CtR, 2)}')
print('#' * 50)

# Profit Margin
profit_margin = (df['Profit'].sum() / df['Revenue'].sum()) * 100.0
print(f'profit_margin = {round(profit_margin, 2)}')


Product_Analysis = df.groupby('Product').agg(
    Total_Orders=('Orders', 'sum'),
    Total_Revenue=('Revenue', 'sum'),
    Total_Cogs=('Cogs', 'sum'),
    Total_Profit=('Profit', 'sum')
).sort_values('Total_Profit', ascending=False).reset_index()
print(Product_Analysis)
print('#' * 50)


Channal_Analysis = df.groupby('Channel').agg(
    Total_Spend=('Ad_spend', 'sum'),
    Total_Leads=('Leads', 'sum'),
    Total_Orders=('Orders', 'sum'),
    Total_Revenue=('Revenue', 'sum'),
    Total_Profit=('Profit', 'sum')
).sort_values('Total_Spend', ascending=False).reset_index()
print(Channal_Analysis)
print('#' * 50)


Campaign_Analysis = df.groupby('Campaign').agg(
    Total_Revenue=('Revenue', 'sum'),
    Total_Cogs=('Cogs', 'sum'),
    Total_Profit=('Profit', 'sum')
).sort_values('Total_Revenue', ascending=False).reset_index()
print(Campaign_Analysis)
print('#' * 50)


Ragional_Analysis = df.groupby('Region').agg(
    Total_Revenue=('Revenue', 'sum'),
    Total_Cogs=('Cogs', 'sum'),
    Total_Profit=('Profit', 'sum')
).sort_values('Total_Revenue', ascending=False).reset_index()
print(Ragional_Analysis)
print('#' * 50)


Time_Analysis = df.groupby('Date_of_Month').agg(
    Total_Spend=('Ad_spend', 'sum'),
    Total_Revenue=('Revenue', 'sum'),
    Total_Orders=('Orders', 'sum'),
).sort_values('Total_Revenue', ascending=False).reset_index()
print(Time_Analysis)
print('#' * 50)


# df.to_csv('Digital_Marketing_Cleaned.csv', index= False)
