import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)

"""
x = np.random.rand(15)
y = np.random.rand(15)
names = np.array(list("ABCDEFGHIJKLMNO"))
c = np.random.randint(1,5,size=15)

norm = plt.Normalize(1,4)
cmap = plt.cm.RdYlGn

fig,ax = plt.subplots()
Mercure_plt = plt.scatter(x,y,c=c, s=100, cmap=cmap, norm=norm)

annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"))
                    #arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):

    pos = Mercure_plt.get_offsets()[ind["ind"][0]]
    annot.xy = pos
    text = "helllo"
    annot.set_text(text)
    annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = Mercure_plt.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
"""

class Planète:
    def __init__(self, color, coord_x, coord_y):
        self.color = color
        self.coord_x = coord_x
        self.coord_y = coord_y


Mercure = Planète('blue', [1, 2, 3], [4, 5, 6])
Venus = Planète('red', [7, 8, 9], [1, 2, 3])

list_class = [Mercure, Venus]


def printage():   
    for i in range(2):
        for j in range(3):
            print(list_class[i].coord_x[j])

printage()