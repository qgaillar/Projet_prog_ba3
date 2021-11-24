import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import turtle



bob = turtle.Turtle()

bob(60)

turtle.done()






"""
r = 3
def circle(phi, phi_off,offset_x, offset_y):
        return np.array([r*np.cos(phi+phi_off), r*np.sin(phi+phi_off)]) + np.array([offset_x, offset_y])

plt.rcParams["figure.figsize"] = 8,6

fig, ax = plt.subplots()
ax.axis([-30,30,-30,30])
ax.set_aspect("equal")

# create initial conditions
phi_offs = [0, np.pi/2, np.pi] 
offset_xs = [0, 0, 0]
offset_ys = [0, 0, 0]
# amount of points
N = len(phi_offs)

# create a point in the axes
points = []
for i in range(N):
  x,y = circle(0, phi_offs[i], offset_xs[i], offset_ys[i])
  points.append(ax.plot(x, y, marker="o")[0])


def update(phi, phi_off, offset_x,offset_y):
        # set point coordinates
        for i in range(N):
          x, y = circle(phi,phi_off[i], offset_x[i], offset_y[i])
          points[i].set_data([x],[y])
        return points

ani = animation.FuncAnimation(fig,update,
      fargs=(phi_offs, offset_xs, offset_ys), 
      interval = 2, 
      frames=np.linspace(0,2*np.pi,360, endpoint=False),
      blit=True)

plt.show()

"""

