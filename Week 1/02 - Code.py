import pandas as pd


df = pd.read_csv('./resources/car-prices.csv')

print(f'Total rows: {df.shape[0]}')
