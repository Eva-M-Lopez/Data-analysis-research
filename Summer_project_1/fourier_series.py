import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load your dataset
df = pd.read_csv("Summer_project_1/American_Census_data.csv")

characteristics = [
    '18 to 64 years', '65 years and over', 'Under 5 years', 
    '5 to 17 years','White alone','Black or African American alone',
    'American Indian and Alaska Native alone','Asian alone',
    'Native Hawaiian and Other Pacific Islander alone','Some other race alone',
    'Two or more races','Hispanic or Latino origin (of any race)',
    'White alone, not Hispanic or Latino','graduate', 'degree','Employed', 'Unemployed'
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

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X.values.reshape(-1, 1)).toarray()

# def square_wave(x):
#     return np.where(np.sin(x) >= 0, 1, -1)

def fourier_series_approx(x, n_terms):
    a0 = 0  # For a square wave, the a0 term is 0
    result = a0 / 2
    
    for n in range(1, n_terms + 1):
        # Square wave only has odd harmonics
        if n % 2 != 0:
            result += (4 / (n * np.pi)) * np.sin(n * x)
    
    return result

x = np.linspace(0, len(y), len(y))
# actual = square_wave(x)
approximation = fourier_series_approx(x, 10)  # 10 terms in the Fourier series

# mse = np.mean((actual - approximation) ** 2)
# print(f'Mean Squared Error: {mse}')

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Census Data')
plt.plot(x, approximation, label='Fourier Series Approximation', linestyle='--')
plt.legend()
plt.title('Fourier Series Approximation of Census Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()







