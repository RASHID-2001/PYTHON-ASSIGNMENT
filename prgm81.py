"""
QN:Consider a CSV file ‘weather.csv’ with the following columns (date,
temperature, humidity, windSpeed, precipitationType, place, weather {Rainy,
Cloudy, Sunny}).
Write commands to do the following using Pandas library.
1. Print first 10 rows of weather data.
2. Find the maximum and minimum temperature
3. List the places with temperature less than 28oC.
4. List the places with weather = “Cloudy”
5. Sort and display each weather and its frequency
6. Create a bar plot to visualize temperature of each day.
(JANUARY 2024)
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

#1
print("\nFirst 10 rows of weather data:")
print(df.head(10))

#2
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()
print("\nMaximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

#3
cold_places = df[df["temperature"] < 28]["place"]
print("\nPlaces with temperature less than 28°C:")
print(cold_places)

#4
cloudy_places = df[df["weather"] == "Cloudy"]["place"]
print("\nPlaces with 'Cloudy' weather:")
print(cloudy_places)

# 5
weather_counts = df["weather"].value_counts()
print("\nWeather frequency:")
print(weather_counts)

# 6.
plt.figure(figsize=(10,5))
plt.bar(df["date"], df["temperature"], color='skyblue')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variation Over Days")
plt.xticks(rotation=45)  # Rotate dates for better visibility
plt.show()