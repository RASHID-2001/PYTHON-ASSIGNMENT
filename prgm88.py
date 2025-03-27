"""
QN:JUNE2022
How to plot two or more lines on a same plot with suitable legends, labels and a
title.
ANS:
	 plot multiple lines on the same graph by using Matplotlib's plot() function and adding legends, labels, and a title for better clarity.
"""
import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 10, 100)  # 100 points between 0 and 10

# Define y values for different functions
y1 = np.sin(x)  # Sine function
y2 = np.cos(x)  # Cosine function
y3 = np.tan(x)  # Tangent function (with limits)

# Create the plot
plt.figure(figsize=(10, 5))  # Set figure size

# Plot each function with different styles
plt.plot(x, y1, label="sin(x)", color="b", linestyle="-", linewidth=2)    # Blue solid line
plt.plot(x, y2, label="cos(x)", color="r", linestyle="--", linewidth=2)   # Red dashed line
plt.plot(x, y3, label="tan(x)", color="g", linestyle=":", linewidth=2)    # Green dotted line

# Add labels, title, and legend
plt.xlabel("X-axis (Radians)")  # X-axis label
plt.ylabel("Y-axis")  # Y-axis label
plt.title("Multiple Trigonometric Functions")  # Title
plt.legend(loc="upper right")  # Legend location
plt.grid(True)  # Add grid for better readability

# Show the plot
plt.show()