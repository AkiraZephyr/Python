#write a python program to draw ellipse on output screen.
import matplotlib.pyplot as plt
import numpy as np

a = 5
b = 3
theta = np.linspace(0, 2 * np.pi, 1000)

x = a * np.cos(theta)
y = b * np.sin(theta)
plt.figure(figsize=(6, 6))
plt.plot(x, y, label='Elliptical Orbit', color='blue')
plt.plot(0, 0, 'yo', label='Focus (Sum)')
plt.title("Elliptical Orbit Simulation")
plt.xlabel("X Position (AU)")
plt.ylabel("Y Position (AU)")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()