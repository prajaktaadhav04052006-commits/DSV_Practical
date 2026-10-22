
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [2, 4, 6, 8, 5],
    "Marks": [40, 55, 75, 90, 65],
    "Attendance": [60, 70, 90, 95, 80]
}

df = pd.DataFrame(data)

print("First 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nCorrelation:")
print(df.corr())

df["Marks"].plot(kind="hist", bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.show()

print("EDA completed successfully!")
