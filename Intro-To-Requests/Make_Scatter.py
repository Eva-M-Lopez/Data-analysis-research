import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("Intro-To-Requests/American_Census_data.csv")

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

plt.figure(figsize=(12, 6))
plt.scatter(X, y, alpha=0.5)
plt.title('Percentage Below Poverty Level by Category')
plt.xlabel('Category')
plt.ylabel('Percentage Below Poverty Level')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability if necessary
plt.tight_layout()
plt.show()
