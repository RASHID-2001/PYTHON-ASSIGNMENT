"""
QN:MAY 2023
Temperature(°C) on different dates is stored in a CSV file as "WEATHER_DATA" as fields
date, temperature and humidity.
1.Draw a plot of the weather report with date as the x-axis and temperature as
the y-axis.
2. .Draw a scatter plot of the weather report with date as the x-axis and humidity
as the y-axis.
Give appropriate titles and labels in the plot.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("WEATHER_DATA.csv")

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# 2
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['temperature'], marker='o', linestyle='-', color='b', label="Temperature (°C)")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over Time")
plt.xticks(rotation=45)  # Rotate dates for better readability
plt.legend()
plt.grid(True)
plt.show()

# 2
plt.figure(figsize=(10, 5))
plt.scatter(df['date'], df['humidity'], color='r', label="Humidity (%)")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.title("Humidity Levels Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()