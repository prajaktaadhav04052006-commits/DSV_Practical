import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset of student marks
data = {
    "Student_Name": [
        "Amit", "Priya", "Rahul", "Sneha", "Rohan",
        "Pooja", "Akash", "Neha", "Kiran", "Anjali"
    ],
    "Marks": [70, 80, 65, 90, 75, 85, 60, 95, 72, 88]
}

# Convert dataset into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("====================================")
print("       STUDENT MARKS DATASET")
print("====================================")
print(df)

# Extract marks as a NumPy array
marks = np.array(df["Marks"])

# Calculate statistical values
total = np.sum(marks)
average = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)
minimum = np.min(marks)
maximum = np.max(marks)
variance = np.var(marks)

# Display statistical results
print("\n====================================")
print("       STATISTICAL ANALYSIS")
print("====================================")

print("Total Marks:", total)
print("Average Marks:", average)
print("Mean Marks:", average)
print("Median Marks:", median)
print("Standard Deviation:", round(std_dev, 2))
print("Variance:", round(variance, 2))
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)

# Add result category for each student
def calculate_result(mark):
    if mark >= 85:
        return "Excellent"
    elif mark >= 70:
        return "Good"
    elif mark >= 50:
        return "Average"
    else:
        return "Needs Improvement"

df["Result"] = df["Marks"].apply(calculate_result)

print("\n====================================")
print("       STUDENT RESULT")
print("====================================")
print(df)

# Find the student with highest marks
topper = df.loc[df["Marks"].idxmax()]

print("\nTopper Name:", topper["Student_Name"])
print("Topper Marks:", topper["Marks"])

# Find the student with lowest marks
lowest = df.loc[df["Marks"].idxmin()]

print("Lowest Marks Student:", lowest["Student_Name"])
print("Lowest Marks:", lowest["Marks"])

# Display summary statistics
print("\n====================================")
print("       SUMMARY STATISTICS")
print("====================================")
print(df["Marks"].describe())

# Plot a bar chart of student marks
plt.figure(figsize=(10, 5))
plt.bar(df["Student_Name"], df["Marks"])

plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()

# Plot a histogram
plt.figure(figsize=(8, 5))
plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()

print("\nProgram executed successfully!")
