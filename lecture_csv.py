import numpy as np
import matplotlib.pyplot as plt


planète = np.genfromtxt('/Users/quentingaillard/Documents/EPFL/BA3/PROGRAMMATION/Projet_gros/planete_test.csv', delimiter = ',', dtype = None)
print(planète[0,0])

x = planète[:, 0]
y = planète[:, 1]
print(x)
print(y)

#plt.plot(x, y)
#plt.show()