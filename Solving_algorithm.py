import time
import Rubik_Info

try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *

# The begining function of solving the rubik cube
def Solve_Cube(canvas, all_Sides):
    print("\n\n\nI am in the solving portion, good luck!")

    side = "Front"
    side_index = all_Sides.index(side) + 1
    direction = "Up"
    square_index = 3
    move_amount = 2
    
    Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
    Rotate_Cube(all_Sides,side, all_Sides[side_index], square_index, direction, move_amount)
    

# Shifts a section of the cube in the direction desired
def Rotate_Cube(all_sides, side_name, current_side, row_column, direction, turns):
    print("Im shifting square " + str(row_column) + " in the " + direction + " direction" + " " + str(turns) + " times")
    current_color = []
    replacement_color = []
    sides = []
    
    if direction == "Up":
        print("Going UP!")
        if (side_name == "Front"):
            sides = ["Front", "Top", "Back", "Bottom"]
            if (row_column == 0):
                print("HEllo")
            if (row_column == 1):
                print("Hello")
            else:
                for n in range(turns):
                    current_color[:] = []
                    replacement_color[:] = []
                    # print("Current Side is " + str(current_side))
                    
                    for i in range(len(sides)):
                        current_side = all_sides.index(sides[i])+1
                        if i == 3:
                            next_side = all_sides.index(sides[0])+1
                        else:
                            next_side = all_sides.index(sides[i+1]) + 1

                        if i == 0:
                            current_color.append((all_sides[current_side][2], all_sides[current_side][5], all_sides[current_side][8]))
                        print("Current color is " + str(current_color))
                        #time.sleep(10)
                        replacement_color.append((all_sides[next_side][2], all_sides[next_side][5], all_sides[next_side][8]))
                        print("Replacement color is " + str(replacement_color))
                        #time.sleep(10)
                        all_sides[next_side][2] = current_color[0][0] #all_sides[current_side][2]
                        all_sides[next_side][5] = current_color[0][1] #all_sides[current_side][5]
                        all_sides[next_side][8] = current_color[0][2] #all_sides[current_side][8]
                        current_color[:] = []
                        current_color.append((replacement_color[0][0], replacement_color[0][1], replacement_color[0][2]))
                        print("New current color is " + str(current_color))
                        #time.sleep(10)
                        replacement_color[:] = []
                        # print("Current color after clearing replacement_color is " + str(current_color))
                        # time.sleep(10)
                        print("current side is " + str(all_sides[current_side]))
                        print("next side " + str(all_sides[next_side]))
                        #time.sleep(10)
                        
                    right_side = all_sides.index("Right") + 1
                    temp = list(all_sides[right_side])
                    all_sides[right_side][2] = temp[0]
                    all_sides[right_side][5] = temp[1]
                    all_sides[right_side][8] = temp[2]
                    all_sides[right_side][1] = temp[3]
                    all_sides[right_side][7] = temp[5]
                    all_sides[right_side][0] = temp[6]
                    all_sides[right_side][3] = temp[7]
                    all_sides[right_side][6] = temp[8]
                    #print("the side is now " + str(all_sides[right_side]))
                    #time.sleep(10)
                    temp[:] = []

                        
                print("You need to update the whole cube now!!")
                
    elif direction == "Down":
        print("Going Down!")

    elif direction == "Left":
        print("Going Left")

    else:
        print("Going Right")
        

    
