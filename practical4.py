
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Rohan"],
    "Marks": [70, 80, None, 90, 75]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

df.to_csv("cleaned_data.csv", index=False)

print("Data cleaning and graph completed!")
