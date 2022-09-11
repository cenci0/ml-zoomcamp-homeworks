import pandas as pd


# Load dataset
df = pd.read_csv('./resources/car-prices.csv')

# Filter Audi cars
df_audi_count = df[df['Make'] == 'Audi']

# Print them
print(df_audi_count['Model'].nunique())
