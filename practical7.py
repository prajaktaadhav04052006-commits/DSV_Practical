
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [35, 40, 50, 60, 70]
}

df = pd.DataFrame(data)

correlation = df["Study_Hours"].corr(df["Marks"])
print("Correlation:", correlation)

X = df[["Study_Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

predicted = model.predict(X)

plt.scatter(X["Study_Hours"], y, label="Actual Data")
plt.plot(X["Study_Hours"], predicted, color="red",
         label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Correlation and Regression")
plt.legend()
plt.show()

print("Analysis completed successfully!")
