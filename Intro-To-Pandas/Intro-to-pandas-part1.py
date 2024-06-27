import pandas as pd
import matplotlib.pyplot as plt
#import pandas and graph availability

df = pd.read_csv("Intro-To-Pandas/weather_data.csv")
#reader

#print(df.head())
#prints the top few entries

#print(df[["Temperature (°C)", "Precipitation (mm)"]].mean())
#got the mean of the temperature and precipitation

#print(df.describe())
#gives some general statistics

#print(df[["Location", "Precipitation (mm)"]].groupby("Location").mean())
#average the group by city

def celsius_to_fahrenheit(temp: float):
    return (temp *(9/5))+32

def km_to_m(wind_speed: float):
    return wind_speed*0.6213712

def mm_to_in(rain_fall: float):
    return rain_fall*0.03937

#converts from metric to non-metric values

df["Temperature (°F)"] = df["Temperature (°C)"].apply(celsius_to_fahrenheit)
df["Wind Speed (mph)"] = df["Wind Speed (km/h)"].apply(km_to_m)
df["Precipitation (in)"] = df["Precipitation (mm)"].apply(mm_to_in)
#adds the non-metric information in

df.drop(["Temperature (°C)","Wind Speed (km/h)","Precipitation (mm)"], axis=1, inplace=True)
#gets rid of the metric information

print(df)
#print the information

df["Temperature (°F)"].plot()
#how to seperate the temperature
plt.show()
