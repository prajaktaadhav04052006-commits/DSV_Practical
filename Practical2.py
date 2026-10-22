
import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

df = pd.DataFrame({"Marks": arr})

print("\nDataFrame:")
print(df)

print("\nFirst 5 Records:")
print(df.head())
