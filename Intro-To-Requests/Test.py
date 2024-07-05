import pandas as pd
from sklearn.base import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import confusion_matrix, mean_squared_error
from sklearn.metrics import classification_report
from sklearn.base import accuracy_score

# Load your dataset
df = pd.read_csv("Intro-To-Requests/American_Census_data.csv")

# Select relevant columns and clean data
characteristic_data = df[df['Label (Grouping)'].str.contains('18 to 64 years|65 years and over|Under 5 years|' + 
'5 to 17 years|graduate|degree|race|alone|hispanic|races|Employed|Unemployed')]

#print(characteristic_data)

#characteristic_data.to_csv('test1.csv')

# Clean the 'United States!!Percent below poverty level!!Estimate' column
#characteristic_data['United States!!Percent below poverty level!!Estimate'] = characteristic_data['United States!!Percent below poverty level!!Estimate'].str.replace(',', '').str.replace('%', '').astype(float)

# Select features (X)
X = characteristic_data[['Label (Grouping)']]
y = characteristic_data[['United States!!Percent below poverty level!!Estimate']]
# y = characteristic_data['United States!!Percent below poverty level!!Estimate']

# # Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

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


# # Assuming X_train, X_test, y_train, y_test are your prepared data sets
# # Instantiate the model
# model = LogisticRegression(multi_class='multinomial', solver='lbfgs')

# # Fit the model
# model.fit(X_train, y_train)

# # Predict on the test set
# y_pred = model.predict(X_test)

# # Evaluate the model
# print(classification_report(y_test, y_pred))