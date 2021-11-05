import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
  
y, x = np.mgrid[:5, 1:6]
poly_coords = [
    (0.25, 2.75), (3.25, 2.75),
    (2.25, 0.75), (0.25, 0.75)
]
fig, ax = plt.subplots()
  
cells = ax.plot(x, y, x + y, color ='green')
ax.add_patch(
    Ellipse(xy=(157.18, 68.4705), width=0.036, height=0.012, 
                        edgecolor='r', fc='yellow', lw=2)
    )
ax.margins(x = 0.1, y = 0.05)
ax.set_aspect('auto')
  
fig.suptitle('matplotlib.axes.Axes.add_patch() \
function Example\n\n', fontweight ="bold")
plt.show()