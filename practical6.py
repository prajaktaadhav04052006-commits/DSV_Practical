
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [35, 40, 50, 60, 70]
}

df = pd.DataFrame(data)

X = df[["Study_Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(pd.DataFrame({"Study_Hours": [6]}))

print("Predicted Marks:", prediction[0])
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

plt.scatter(X["Study_Hours"], y)
plt.plot(X["Study_Hours"], model.predict(X), color="red")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.show()
