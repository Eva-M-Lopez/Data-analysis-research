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