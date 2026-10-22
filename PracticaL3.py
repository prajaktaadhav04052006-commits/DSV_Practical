
import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Priya"],
    "Marks": [80, None, 70, None],
    "Age": [20, 21, 19, 21]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

df.to_csv("cleaned_data.csv", index=False)

print("\nDataset saved successfully!")
