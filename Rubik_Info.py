try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *
import time
import Solving_algorithm


# Converts a set of coordinates into indexes in the cube
# returns square index horizontally and vertically (x,y)
def CoordinatesToIndex(coordinates):
    t = (coordinates[0] - 98) / 60
    
    i = (coordinates[1] - 90) / 60
    
    return[t, i]



# Creates the cubes defaults at startup
def CreateCube():
    '''
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
    '''

    # If you want the pieces filled in (for testing purposes),
    # Uncomment this section and comment out the previous section
    '''
    side1 = ["Yellow", "Yellow", "Yellow",
             "Yellow", "Yellow", "Yellow",
             "Yellow", "Yellow", "Yellow"]

    side2 = ["Blue", "Blue", "Blue",
             "Blue", "Blue", "Blue",
             "Blue", "Blue", "Blue"]

    side3 = ["Green", "Green", "Green",
             "Green", "Green", "Green",
             "Green", "Green", "Green"]

    side4 = ["Red", "Red", "Red",
             "Red", "Red", "Red",
             "Red", "Red", "Red"]

    side5 = ["Orange", "Orange", "Orange",
             "Orange", "Orange", "Orange",
             "Orange", "Orange", "Orange"]

    frontside = ["White", "White", "White",
                 "White", "White", "White",
                 "White", "White", "White"]
    '''

    # For debugging turning up/down
    '''
    side1 = ["Green", "Green", "Green",
             "Yellow", "Yellow", "Yellow",
             "Blue", "Blue", "Blue"]

    side2 = ["White", "White", "White",
             "Blue", "Blue", "Blue",
             "Yellow", "Yellow", "Yellow"]

    side3 = ["Yellow", "Yellow", "Yellow",
             "Green", "Green", "Green",
             "White", "White", "White"]

    side4 = ["Red", "Red", "Red",
             "Red", "Red", "Red",
             "Red", "Red", "Red"]

    side5 = ["Orange", "Orange", "Orange",
             "Orange", "Orange", "Orange",
             "Orange", "Orange", "Orange"]

    frontside = ["Green", "Green", "Green",
                 "White", "White", "White",
                 "Blue", "Blue", "Blue"]
    '''

    # For debugging turning left/right
    '''
    
    side1 = ["Blue", "Yellow", "White",
             "Blue", "Yellow", "White",
             "Blue", "Yellow", "White"]

    side2 = ["Orange", "Orange", "Orange",
             "Orange", "Orange", "Orange",
             "Orange", "Orange", "Orange"]

    side3 = ["Red", "Red", "Red",
             "Red", "Red", "Red",
             "Red", "Red", "Red"]

    side4 = ["Green", "Blue", "White",
             "Green", "Blue", "White",
             "Green", "Blue", "White"]

    side5 = ["Blue", "Green", "Yellow",
             "Blue", "Green", "Yellow",
             "Blue", "Green", "Yellow"]

    frontside = ["Yellow", "White", "Green",
                 "Yellow", "White", "Green",
                 "Yellow", "White", "Green"]
    '''
    
    # For testing the yellow cross
    side1 = ["White", "Orange", "Yellow",
             "Green", "Orange", "Orange",
             "White", "Blue", "Red"]

    side2 = ["Green", "Green", "Orange",
             "Yellow", "Blue", "Yellow",
             "Blue", "White", "White"]

    side3 = ["Red", "Yellow", "Green",
             "Red", "Green", "Orange",
             "Red", "Green", "Blue"]

    side4 = ["Orange", "White", "Orange",
             "White", "Yellow", "Green",
             "Yellow", "Blue", "Green"]

    side5 = ["Red", "Red", "Green",
             "Red", "White", "Red",
             "Yellow", "White", "Orange"]

    frontside = ["Blue", "Orange", "Yellow",
                 "Blue", "Red", "Blue",
                 "Blue", "Yellow", "White"]
    
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
    

def Before_After(canvas, all_sides, colors, temp):
    
    canvas.delete("line")
    if (temp[1] == "Down"):
        x1 = 65
        y1 = 80
        x2 = 65
        y2 = 40
        if temp[2] == 1:
            x1 += 50
            x2 = x1
        elif temp[2] == 2:
            x1 += 100
            x2 = x1
    elif (temp[1] == "Up"):
        x1 = 65
        y1 = 260
        x2 = 65
        y2 = 290
        
        if (temp[2] == 1):
            x1 += 50
            x2 = x1
        elif (temp[2] == 2):
            x1 += 100
            x2 = x1
    elif (temp[1] == "Left"):
        x1 = 200
        y1 = 115
        x2 = 230
        y2 = 115
        if (temp[2] == 1):
            y1 += 50
            y2 = y1
        elif (temp[2] == 2):
            y1 += 100
            y2 = y1
    elif (temp[1] == "Right"):
        x1 = 35
        y1 = 115
        x2 = 5
        y2 = 115
        if (temp[2] == 1):
            y1 += 50
            y2 = y1
        elif (temp[2] == 2):
            y1 += 100
            y2 = y1

    # Where you start the end of x, where you start the end of y (arrow spot)
    # The lines x axis at the end, the y axis at the end (begin line spot)
    w = canvas.create_line(x1, y1, x2, y2, arrow=FIRST, tag = "line") 
    
        
    print(colors)
    # time.sleep(10)
    for r in range(0, 2):
        i = 90
        counter = 0
        if r ==1:
            print("This spot needs to change the rubiks cube to the \"after\" section")
            Solving_algorithm.Rotate_Cube(all_sides, temp[0], all_sides[all_sides.index("Front")+1], temp[2], temp[1], temp[3])
        for z in range(0, 3):
            if r == 1:
                t = 260 #98
            else:
                t = 40
            for q in range(0, 3):
                canvas.create_rectangle(t, i, t+50, i+50, fill=colors[counter])
                t += 50
                counter += 1
            #i += 60
            i += 50
