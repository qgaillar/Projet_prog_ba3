
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from test_class_planètes import *

"""
def plot_planète():

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack()

root = Tk()
root.title('planètes plotting in tkinter')
root.geometry("1000x1000")

plot_button = Button(
    master = root,
    command= plot_planète, 
    height = 2, 
    width = 10, 
    text = "plot")

plot_button.pack()

root.mainloop()

#Button(root,text="Draw",command=draw_chart).pack()

from tkinter import * 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
  
def plot(): 
  
    
    fig = Figure(figsize = (5, 5), 
                 dpi = 100) 
    y = [i**2 for i in range(101)] 
    plot1 = fig.add_subplot(111) 
    plot1.plot(y) 
    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
    canvas.get_tk_widget().pack() 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
    canvas.get_tk_widget().pack() 
  
window = Tk() 
  
window.title('Plotting in Tkinter') 
  
window.geometry("500x500") 
  
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Start Simulation") 
  
plot_button.pack() 
  
window.mainloop() 

"""


root = Tk()

root.title("planète ploting")

data_plot = FigureCanvasTkAgg(fig, master = root)
data_plot.draw()
data_plot.get_tk_widget().pack()

root.mainloop()

