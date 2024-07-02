#https://data.census.gov/table?q=crime%20and%20poverty%20in%20United%20states
#The purpose of this census is to show the status of poverty in the US
#The goal of this project is to create an easy way to calculate your likely hood of poverty based on the characteristics of this census.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Intro-To-Requests/American_Census_data.csv")
#reader

age_group_data = df[df['Label (Grouping)'].str.contains('graduate|degree')]
#gets the data related to age

#get the columns related
age_groups = age_group_data['Label (Grouping)']
below_poverty = age_group_data['United States!!Percent below poverty level!!Estimate']

# Convert the 'below_poverty' values to numeric by removing commas
below_poverty = below_poverty.str.replace('%', '').astype(float)

# Plot the bar graph
plt.figure(figsize=(12, 6))
plt.bar(age_groups, below_poverty, color='blue')
plt.xlabel('Origin')
plt.ylabel('Percentage below poverty level')
plt.title('Percentage of Population Below Poverty Level by Education')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



