import time

try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *

# The begining function of solving the rubik cube
def Solve_Cube(canvas, all_Sides):
    print("\n\n\nI am in the solving portion, good luck!")
    

# Shifts a section of the cube in the direction desired
def Rotate_Cube(all_sides, current_side, square, direction):
    print("Im shifting square " + str(square) + " in the " + direction + " direction")
    
    
