"""
QN:MAY 2024
Create a Matplotlib plot with two lines representing the functions y=sin(x) for
0≤x≤2π (use a solid line) and y=cos(x) for 0≤x≤2π (use a dashed line).
Customize the plot by adding appropriate ticks, labels for the x and y axes, and a
legend to distinguish between the two functions.
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 100)  


y_sin = np.sin(x)
y_cos = np.cos(x)


plt.figure(figsize=(8, 5)) 

plt.plot(x, y_sin, label="sin(x)", linestyle='-', color='blue')   
plt.plot(x, y_cos, label="cos(x)", linestyle='--', color='red')   


plt.xlabel("X values (radians)")   
plt.ylabel("Y values")             
plt.title("Sine and Cosine Functions") 
plt.xticks(np.arange(0, 2*np.pi+0.1, np.pi/2),  
           labels=['0', 'π/2', 'π', '3π/2', '2π'])  
plt.yticks(np.arange(-1, 1.1, 0.5)) 

plt.legend() 
plt.grid(True) 
plt.savefig("exam.png")
# Show the plot
plt.show()