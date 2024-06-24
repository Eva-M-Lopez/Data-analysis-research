import pandas as pd
df = pd.read_csv("Intro-To-Pandas/weather_data.csv")
#print(df.head())
#print(df[["Temperature (°C)", "Precipitation (mm)"]].mean())
#print(df.describe())
#average the group by city
#print(df[["Location", "Precipitation (mm)"]].groupby("Location").mean())

def celsius_to_fahrenheit(temp: float):
    return (temp *(9/5))+32

def km_to_m(wind_speed: float):
    return wind_speed*0.6213712

def mm_to_in(rain_fall: float):
    return rain_fall*0.03937

df["Temperature (°F)"] = df["Temperature (°C)"].apply(celsius_to_fahrenheit)
df["Wind Speed (mph)"] = df["Wind Speed (km/h)"].apply(km_to_m)
df["Precipitation (in)"] = df["Precipitation (mm)"].apply(mm_to_in)
df.drop(["Temperature (°C)","Wind Speed (km/h)","Precipitation (mm)"], axis=1, inplace=True)
print(df)