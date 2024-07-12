import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load your dataset
df = pd.read_csv("Summer_project_1/American_Census_data.csv")

characteristics = [
    '18 to 64 years', '65 years and over', 'Under 5 years', 
    '5 to 17 years'
]

pattern = '|'.join(characteristics)
filtered_df = df[df['Label (Grouping)'].str.contains(pattern, case=False, na=False)]

percentage_df = filtered_df[[
    "Label (Grouping)", 
    "United States!!Percent below poverty level!!Estimate", 
]]

percentage_df.loc[:, "United States!!Percent below poverty level!!Estimate"] = (
    percentage_df["United States!!Percent below poverty level!!Estimate"]
    .str.replace('%', '')
    .astype(float)
)

X = percentage_df['Label (Grouping)']
y = percentage_df['United States!!Percent below poverty level!!Estimate']

# One-hot encode the categorical features
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X.values.reshape(-1, 1)).toarray()

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Plotting
plt.figure(figsize=(12, 6))

# Scatter plot for actual values
plt.scatter(X, y, color='blue', label='Actual Data', alpha=0.5)

# Scatter plot for predicted values
plt.scatter(X, model.predict(X_encoded), color='red', label='Predicted Data', alpha=0.5)

# Add a line for the predicted values
plt.plot(X, model.predict(X_encoded), color='orange', label='Prediction Line', linewidth=2)

# Fit a line to the predicted data
linear_fit = LinearRegression()
linear_fit.fit(np.arange(len(y)).reshape(-1, 1), model.predict(X_encoded))
fit_line = linear_fit.predict(np.arange(len(y)).reshape(-1, 1))

# Add the fitted line to the plot
plt.plot(X, fit_line, color='pink', label='Best Fit Line', linewidth=2)


plt.title('Percentage Below Poverty Level by Category')
plt.xlabel('Category')
plt.ylabel('Percentage Below Poverty Level')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()
plt.show()
