try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *
import time


def CoordinatesToIndex(coordinates):
    t = (coordinates[0] - 98) / 60
    # t = 98 + (60 * multiple)
    
    i = (coordinates[1] - 90) / 60
    # i = 90 + (60 * multiple)
    
    return[t, i]


def CreateCube():
    side1 = ["dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray"]

    side2 = ["dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray"]

    side3 = ["dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray"]

    side4 = ["dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray"]

    side5 = ["dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray",
             "dark gray", "dark gray", "dark gray"]

    frontside = ["dark gray", "dark gray", "dark gray",
                 "dark gray", "white", "dark gray",
                 "dark gray", "dark gray", "dark gray"]

    master = ["Front",frontside, "Back",side1, "Left",side2, "Right",side3, "Top",side4, "Bottom",side5]
    # master = [frontside, side, side, side, side, side]
    return master


def RubikSetup(canvas, colors):
    i = 90
    counter = 0
    print(colors)
    # time.sleep(10)
    for z in range(0, 3):
        t = 98
        for q in range(0, 3):
            canvas.create_rectangle(t, i, t+60, i+60, fill=colors[counter])
            t += 60
            counter += 1
        i += 60


def ChangeColor(canvas, color, index):
    multiple = (index[0] - 98) / 60
    t = 98 + (60 * multiple)
    
    multiple = (index[1] - 90) / 60
    i = 90 + (60 * multiple)
    canvas.create_rectangle(t, i, t+60, i+60, fill=color)
    
    
def Update_Array(Master, side, color, coordinates):
    index = CoordinatesToIndex(coordinates)
    # print(str(Master.index(side)+1))
    print(str(index))
    # time.sleep(10)
    Master[index[0] +(index[1]* 3)] = color
    
