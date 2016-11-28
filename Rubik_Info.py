try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *
import time

# Converts a set of coordinates into indexes in the cube
# returns square index horizontally and vertically (x,y)
def CoordinatesToIndex(coordinates):
    t = (coordinates[0] - 98) / 60
    
    i = (coordinates[1] - 90) / 60
    
    return[t, i]


# Creates the cubes defaults at startup
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
                 "dark gray", "White", "dark gray",
                 "dark gray", "dark gray", "dark gray"]

    master = ["Front",frontside, "Back",side1, "Left",side2, "Right",side3, "Top",side4, "Bottom",side5]
    return master


# Creates the GUI portion of the cube
# (creates all the colors on the screen
# for a cubes side).
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


# Changes a single cubes color to the users requested color on the screen
def ChangeColor(canvas, color, index):
    multiple = (index[0] - 98) / 60
    t = 98 + (60 * multiple)
    
    multiple = (index[1] - 90) / 60
    i = 90 + (60 * multiple)
    canvas.create_rectangle(t, i, t+60, i+60, fill=color)
    
    
# Changes the color of an array from its original color to its new color
def Update_Array(Master, side, color, coordinates):
    index = CoordinatesToIndex(coordinates)
    # print(str(Master.index(side)+1))
    print(str(index))
    # time.sleep(10)
    Master[index[0] + (index[1] * 3)] = color
    
