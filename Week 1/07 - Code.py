import numpy as np
import pandas as pd


# Load dataset
df = pd.read_csv('./resources/car-prices.csv')

# (7.1) Select all the "Lotus" cars
df_lotus = df[df['Make'] == 'Lotus']

# (7.2) Select only columns "Engine HP" and "Engine Cylinders"
df_lotus_engines = df_lotus[['Engine HP', 'Engine Cylinders']]

# (7.3) Drop all duplicated rows (you should get a dataframe with 9 rows)
df_lotus_engines = df_lotus_engines.drop_duplicates()

# (7.4) Get the underlying NumPy array (call it `X`)
X = df_lotus_engines.to_numpy()

# (7.5) Compute matrix-matrix multiplication between the transpose of `X` and `X` (call the result `XTX`)
# XTX = np.matmul(X.T, X)
XTX = X.T @ X

# (7.6) Invert `XTX`
XTX_inv = np.linalg.inv(XTX)

# (7.7) Create an array `y` with values `[1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800]`
y = [1100, 800, 750, 850, 1300, 1000, 1000, 1300, 800]

# (7.8) Multiply the inverse of `XTX` with the transpose of `X`, and then multiply the result by `y` (call the result `w`)
# w = np.matmul(np.matmul(XTX_inv, X.T), y)
w = XTX_inv @ X.T @ y

# (7.9) What's the value of the first element of `w`?
print(w[0])
