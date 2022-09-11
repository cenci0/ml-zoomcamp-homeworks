import pandas as pd


# Load dataset
df = pd.read_csv('./resources/car-prices.csv')

# (6.1) Find the median
pre_median = df['Engine Cylinders'].median()
# (6.2) Find the most frequent value (mode)
pre_mode = df['Engine Cylinders'].mode()
# (6.3) Fill missing values with the mode
df_filled_cylinders = df.fillna({'Engine Cylinders': 4.0})
# (6.4) Find the median of the updated dataset
post_median = df_filled_cylinders['Engine Cylinders'].median()

# Print
print(f'Median: {pre_median}',
      f'Most frequent value: {list(pre_mode)[0]}',
      f'New median: {post_median}',
      sep='\n')
