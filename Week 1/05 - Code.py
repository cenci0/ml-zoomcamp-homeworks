import pandas as pd


# Load dataset
df = pd.read_csv('./resources/car-prices.csv')

df_nullable_cols = df.isna().any()
df_nullable_cols = df_nullable_cols[df_nullable_cols]

# Print
print(df_nullable_cols.count())
