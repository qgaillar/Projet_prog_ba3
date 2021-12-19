import numpy as np
import matplotlib.pyplot as plt

x_min = 0
x_max = 10000000
y_min = 0
y_max = 10000000


fig = plt.figure()
ax = plt.subplot(111)                                 #définiton de notre figure composé de seulement une ligne et une colonne
ax.set_facecolor((0, 0, 0))  
plt.xlim([x_min, x_max])                              #definie l'échelle de notre plot
plt.ylim([y_min, y_max])


plt.title("Asteroid in solar system simulation")
plt.grid(alpha = 0.2)
plt.show()