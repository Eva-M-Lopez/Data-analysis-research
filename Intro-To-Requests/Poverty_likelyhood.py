#https://data.census.gov/table?q=crime%20and%20poverty%20in%20United%20states
#The purpose of this census is to show the status of poverty in the US
#The goal of this project is to create an easy way to calculate your likely hood of poverty based on the characteristics of this census.
import pandas as pd

df = pd.read_csv("Intro-To-Requests/American_Census_data.csv")
#reader

# Get the total population
total_population = df.loc[df['Label (Grouping)'] == 'Population for whom poverty status is determined', 'United States!!Total!!Estimate'].values[0]
print(total_population)


