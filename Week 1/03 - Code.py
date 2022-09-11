import pandas as pd


# Load dataset
df = pd.read_csv('./resources/car-prices.csv')

# Get top 3 manufacturers
df_top_manufacturers = df.groupby(df['Make'])\
    .size()\
    .sort_values(ascending=False)\
    .head(3)

# Print them
print(dict(df_top_manufacturers))
