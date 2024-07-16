'18 to 64 years', '65 years and over', 'Under 5 years', 
    '5 to 17 years','White alone','Black or African American alone',
    'American Indian and Alaska Native alone','Asian alone',
    'Native Hawaiian and Other Pacific Islander alone','Some other race alone',
    'Two or more races','Hispanic or Latino origin (of any race)',
    'White alone, not Hispanic or Latino','graduate', 'degree','Employed', 'Unemployed'

    # encoder = OneHotEncoder()
# X_encoded = encoder.fit_transform(X.values.reshape(-1, 1)).toarray()

# X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# # # Initialize and fit the model (e.g., Linear Regression)
# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# # Evaluate
# mse = mean_squared_error(y_test, y_pred)
# r2 = model.score(X_test, y_test)

# print(f"Mean Squared Error: {mse}")
#print(f"R-squared: {r2}")


from statistics import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
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

X = percentage_df['Label (Grouping)']  # Assuming these are categorical features
y = percentage_df['United States!!Percent below poverty level!!Estimate']

plt.figure(figsize=(12, 6))
plt.scatter(X, y, alpha=0.5)

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X.values.reshape(-1, 1)).toarray()

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# # Initialize and fit the model (e.g., Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

# print(f"Mean Squared Error: {mse}")
# print(f"R-squared: {r2}")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2, color='green', label='Perfect Prediction')

plt.title('Percentage Below Poverty Level by Category')
plt.xlabel('Category')
plt.ylabel('Percentage Below Poverty Level')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if necessary
plt.tight_layout()
plt.show()
