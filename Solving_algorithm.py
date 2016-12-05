import time
import Rubik_Info

try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *

# The begining function of solving the rubik cube
def Solve_Cube(canvas, all_Sides, number):
    print("\n\n\nI am in the solving portion, good luck!")

    side = "Front"
    side_index = all_Sides.index(side) + 1
    direction = "Left"
    row_col = 2
    move_amount = 1

    if (number == 0):
        Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
        Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)

    if (number == 1):
        side = "Front"
        side_index = all_Sides.index(side) + 1
        direction = "Down"
        row_col = 0
        move_amount = 1
        Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
        Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
    

# Shifts a section of the cube in the direction desired
def Rotate_Cube(all_sides, side_name, current_side, row_column, direction, turns):
    print("Im shifting square " + str(row_column) + " in the " + direction + " direction" + " " + str(turns) + " times")
    current_color = []
    replacement_color = []
    sides = []
    indexes = []
    places = []
    Back_indexes = []
    affected_side = ""
    
    if direction == "Up":
        print("Going UP!")
        if (side_name == "Front"):
            sides = ["Front", "Top", "Back", "Bottom"]
            if (row_column == 1):
                indexes = [1, 4, 7]
                
            elif (row_column == 0):
                print("Hello")
                indexes = [0, 3, 6]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Left"
            else:
                print("Hi")
                indexes = [2, 5, 8]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Right"
            
    elif direction == "Down":
        print("Going Down!")
        if (side_name == "Front"):
            sides = ["Front", "Bottom", "Back", "Top"]
            if (row_column == 0):
                indexes = [0, 3, 6]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Left"
                
            elif (row_column == 1):
                indexes = [1, 4, 7]
                
            else:
                indexes = [2, 5, 8]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Right"
            
    elif direction == "Left":
        print("Going Left")
        if (side_name == "Front"):
            sides = ["Front", "Left", "Back", "Right"]
            if (row_column == 0):
                indexes = [0, 1, 2]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                Back_indexes = [8, 7, 6]
                affected_side = "Top"
            elif(row_column == 1):
                print("Hello")
                indexes = [3, 4, 5]
                Back_indexes = [5, 4, 3]
                
            else:
                print("Bottom affected")
                indexes = [6, 7, 8]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                Back_indexes = [2, 1, 0]
                affected_side = "Bottom"
                
    else:
        print("Going Right")
        # Start here (everything before has already been tested)
        
    for n in range(turns):
        current_color[:] = []
        replacement_color[:] = []
        # print("Current Side is " + str(current_side))
        sleep_time = 0
        for i in range(len(sides)):
            current_side = all_sides.index(sides[i])+1
            if i == 3:
                next_side = all_sides.index(sides[0])+1
            else:
                next_side = all_sides.index(sides[i+1]) + 1
                        
            if i == 0:
                current_color.append((all_sides[current_side][indexes[0]], all_sides[current_side][indexes[1]], all_sides[current_side][indexes[2]]))
            print("Current color is " + str(current_color))
            print(str(indexes[0]) + " " + str(indexes[1]) + " " + str(indexes[2]))
            time.sleep(sleep_time)
            
            # print("Replacement color is " + str(replacement_color))
            # print(str(indexes[0]) + " " +str(indexes[1]) + " " + str(indexes[2]))
            # print("Next side is " + sides[i+1])
            # time.sleep(sleep_time)
            
            if ((direction == "Left" or direction == "Right") and (i != 3) and (sides[i+1] == "Back")):
                replacement_color.append((all_sides[next_side][Back_indexes[0]], all_sides[next_side][Back_indexes[1]], all_sides[next_side][Back_indexes[2]]))
                print("This should only be for the back side")
                print("Current Color is " + str(current_color))
                print(str(indexes[0]) + " " + str(indexes[1]) + " " + str(indexes[2]))
                print("Replacement color is " + str(replacement_color))
                print(str(indexes[0]) + " " +str(indexes[1]) + " " + str(indexes[2]))
                time.sleep(sleep_time)
                # current_color.reverse()
                all_sides[next_side][Back_indexes[0]] = current_color[0][0]
                all_sides[next_side][Back_indexes[1]] = current_color[0][1]
                all_sides[next_side][Back_indexes[2]] = current_color[0][2]
                current_color[:] = []
                current_color.append((replacement_color[0][0], replacement_color[0][1], replacement_color[0][2]))
            else:
                replacement_color.append((all_sides[next_side][indexes[0]], all_sides[next_side][indexes[1]], all_sides[next_side][indexes[2]]))
                all_sides[next_side][indexes[0]] = current_color[0][0] #all_sides[current_side][2]
                all_sides[next_side][indexes[1]] = current_color[0][1] #all_sides[current_side][5]
                all_sides[next_side][indexes[2]] = current_color[0][2] #all_sides[current_side][8]
                current_color[:] = []
                current_color.append((replacement_color[0][0], replacement_color[0][1], replacement_color[0][2]))
            print("New current color is " + str(current_color))
            time.sleep(sleep_time)
            replacement_color[:] = []
            # print("Current color after clearing replacement_color is " + str(current_color))
            # time.sleep(10)
            print("current side is " + str(all_sides[current_side]))
            print("next side " + str(all_sides[next_side]))
            time.sleep(sleep_time)
            
        if (affected_side != ""):
            right_side = all_sides.index(affected_side) + 1
            temp = list(all_sides[right_side])
            all_sides[right_side][places[0]] = temp[0]
            all_sides[right_side][places[1]] = temp[1]
            all_sides[right_side][places[2]] = temp[2]
            all_sides[right_side][places[3]] = temp[3]
            all_sides[right_side][places[4]] = temp[4]
            all_sides[right_side][places[5]] = temp[5]
            all_sides[right_side][places[6]] = temp[6]
            all_sides[right_side][places[7]] = temp[7]
            all_sides[right_side][places[8]] = temp[8]
            # print("the side is now " + str(all_sides[right_side]))
            # time.sleep(10)
            temp[:] = []
                  
    print("You need to update the whole cube now!!")
