import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv("Intro-To-Requests/American_Census_data.csv")

characteristic_data = df[df['Label (Grouping)'].str.contains('18 to 64 years|65 years and over|Under 5 years|' + 
'5 to 17 years|graduate|degree|race|alone|hispanic|races|Employed|Unemployed')]
#gets the data - x

# Clean the 'United States!!Percent below poverty level!!Estimate' column
characteristic_data['United States!!Percent below poverty level!!Estimate'] = characteristic_data['United States!!Percent below poverty level!!Estimate'].str.replace(',', '')

#y
below_poverty = characteristic_data['United States!!Percent below poverty level!!Estimate'] 

# Convert the 'below_poverty' values to numeric by removing commas
below_poverty = below_poverty.str.replace('%', '').astype(float)

X = characteristic_data.drop(['Label (Grouping)', 'United States!!Percent below poverty level!!Estimate'], axis=1)


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, below_poverty, test_size=0.3, random_state=42)

# Initialize and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", report)