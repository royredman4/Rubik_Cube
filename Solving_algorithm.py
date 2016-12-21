import time
import Rubik_Info
import collections
import random


try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *

# The begining function of solving the rubik cube
def Solve_Cube(canvas, all_Sides, number, ErrorText):
    print("\n\n\nI am in the solving portion, good luck!")
    #side = "Front"
    side = "Bottom"
    side_index = all_Sides.index(side) + 1
    direction = "Right"
    row_col = 2
    move_amount = 1

    # Delete this if you dont want the rendomizing going on
    #temp_directions = ["Up", "Down", "Left", "Right"]
    #row_col = random.randint(0, 2)
    #direction = temp_directions[random.randint(0, 3)]
    #print("row_col is " + str(row_col) + " and direction is " + str(direction))


    
    if (number == 0):
        # Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
        Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
   
    # Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
    # Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
    
    if (number == 1):
        #side = "Front"
        side = "Front"
        side_index = all_Sides.index(side) + 1
        direction = "Left"
        row_col = 0
        move_amount = 1
        # Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
        Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
        
    ErrorText.set("Moving " + direction + " at row/col " + str(row_col) + " at " + side + " side")
    return ([side, direction, row_col, move_amount])
    
# Shifts a section of the cube in the direction desired
def Rotate_Cube(all_sides, side_name, current_side, row_column, direction, turns):
    print("Im shifting square " + str(row_column) + " in the " + direction + " direction" + " " + str(turns) + " times")
    current_color = []
    temp_color = []
    next_color = []
    sides = []
    indexes = []
    places = []
    affected_side = ""
    
    if direction == "Up":
        print("Going UP!")
        if (side_name == "Front"):
            sides = ["Front", "Top", "Back", "Bottom"]
            if (row_column == 0):
                print("Hello")
                indexes = [[0, 3, 6],
                           [0, 3, 6],
                           [8, 5, 2],
                           [0, 3, 6]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Left"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [1, 4, 7],
                           [7, 4, 1],
                           [1, 4, 7]]
                
            else:
                print("Hi")
                indexes = [[2, 5, 8],
                           [2, 5, 8],
                           [6, 3, 0],
                           [2, 5, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Right"
                
        elif (side_name == "Back"):
            sides = ["Back", "Top", "Front", "Bottom"]
            if (row_column == 0):
                print("Hello")
                indexes = [[0, 3, 6],
                           [8, 5, 2],
                           [8, 5, 2],
                           [8, 5, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Right"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [7, 4, 1],
                           [7, 4, 1],
                           [7, 4, 1]]
            else:
                indexes = [[2, 5, 8],
                           [6, 3, 0],
                           [6, 3, 0],
                           [6, 3, 0]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Left"
                
        elif (side_name == "Left"):
            sides = ["Left", "Top", "Right", "Bottom"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [2, 1, 0],
                           [8, 5, 2],
                           [6, 7, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Back"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [5, 4, 3],
                           [7, 4, 1],
                           [3, 4, 5]]
            else:
                indexes = [[2, 5, 8],
                           [8, 7, 6],
                           [6, 3, 0],
                           [0, 1, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Front"
        elif (side_name == "Right"):
            sides = ["Right", "Top", "Left", "Bottom"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [6, 7, 8],
                           [8, 5, 2],
                           [2, 1, 0]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Front"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [3, 4, 5],
                           [7, 4, 1],
                           [5, 4, 3]]
            else:
                indexes = [[2, 5, 8],
                           [0, 1, 2],
                           [6, 3, 0],
                           [8, 7, 6]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Back"
        elif (side_name == "Top"):
            sides = ["Top", "Back", "Bottom", "Front"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [8, 5, 2],
                           [0, 3, 6],
                           [0, 3, 6]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Left"
            elif(row_column == 1):
                indexes = [[1, 4, 7],
                           [7, 4, 1],
                           [1, 4, 7],
                           [1, 4, 7]]
            else:
                indexes = [[2, 5, 8],
                           [6, 3, 0],
                           [2, 5, 8],
                           [2, 5, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Right"
        elif (side_name == "Bottom"):
            sides = ["Bottom", "Front", "Top", "Back"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [0, 3, 6],
                           [0, 3, 6],
                           [8, 5, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Left"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [1, 4, 7],
                           [1, 4, 7],
                           [7, 4, 1]]
            else:
                indexes = [[2, 5, 8],
                           [2, 5, 8],
                           [2, 5, 8],
                           [6, 3, 0]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Right"
        else:
            print("This is an INVALID OPTION!!")
            time.sleep(12)
            
    elif direction == "Down":
        print("Going Down!")
        if (side_name == "Front"):
            sides = ["Front", "Bottom", "Back", "Top"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [0, 3, 6],
                           [8, 5, 2],
                           [0, 3, 6]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Left"
                
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [1, 4, 7],
                           [7, 4, 1],
                           [1, 4, 7]]
            else:
                indexes = [[2, 5, 8],
                           [2, 5, 8],
                           [6, 3, 0],
                           [2, 5, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Right"
        elif (side_name == "Back"):
            sides = ["Back", "Bottom", "Front", "Top"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [8, 5, 2],
                           [8, 5, 2],
                           [8, 5, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Right"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [7, 4, 1],
                           [7, 4, 1],
                           [7, 4, 1]]
            else:
                indexes = [[2, 5, 8],
                           [6, 3, 0],
                           [6, 3, 0],
                           [6, 3, 0]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Left"
        elif (side_name == "Left"):
            sides = ["Left", "Bottom", "Right", "Top"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [6, 7, 8],
                           [8, 5, 2],
                           [2, 1, 0]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Back"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [3, 4, 5],
                           [7, 4, 1],
                           [5, 4, 3]]
            else:
                indexes = [[2, 5, 8],
                           [0, 1, 2],
                           [6, 3, 0],
                           [8, 7, 6]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Front"
        elif (side_name == "Right"):
            sides = ["Right", "Bottom", "Left", "Top"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [2, 1, 0],
                           [8, 5, 2],
                           [6, 7, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Front"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [5, 4, 3],
                           [7, 4, 1],
                           [3, 4, 5]]
            else:
                indexes = [[2, 5, 8],
                           [8, 7, 6],
                           [6, 3, 0],
                           [0, 1, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Back"
        elif (side_name == "Top"):
            sides = ["Top", "Front", "Bottom", "Back"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [0, 3, 6],
                           [0, 3, 6],
                           [8, 5, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Left"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [1, 4, 7],
                           [1, 4, 7],
                           [7, 4, 1]]
            else:
                indexes = [[2, 5, 8],
                           [2, 5, 8],
                           [2, 5, 8],
                           [6, 3, 0]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Right"
        elif (side_name == "Bottom"):
            sides = ["Bottom", "Back", "Top", "Front"]
            if (row_column == 0):
                indexes = [[0, 3, 6],
                           [8, 5, 2],
                           [0, 3, 6],
                           [0, 3, 6]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Left"
            elif (row_column == 1):
                indexes = [[1, 4, 7],
                           [7, 4, 1],
                           [1, 4, 7],
                           [1, 4, 7]]
            else:
                indexes = [[2, 5, 8],
                           [6, 3, 0],
                           [2, 5, 8],
                           [2, 5, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Right"
        else:
            print("This is an INVALID OPTION!!")
            time.sleep(12)
        
    elif direction == "Left":
        print("Going Left")
        if (side_name == "Front"):
            sides = ["Front", "Left", "Back", "Right"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Top"
            elif(row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Bottom"
        elif (side_name == "Back"):
            sides = ["Back", "Right", "Front", "Left"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Bottom"
        elif (side_name == "Left"):
            sides = ["Left", "Back", "Right", "Front"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Bottom"
        elif (side_name == "Right"):
            sides = ["Right", "Front", "Left", "Back"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Bottom"
                
        elif (side_name == "Top"):
            sides = ["Top", "Left", "Bottom", "Right"]
            if (row_column == 0):
                indexes = [[0, 1, 2],
                           [6, 3, 0],
                           [8, 7, 6],
                           [2, 5, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Back"
            elif (row_column == 1):
                indexes = [[3, 4, 5],
                           [7, 4, 1],
                           [5, 4, 3],
                           [1, 4, 7]]
            else:
                indexes = [[6, 7, 8],
                           [8, 5, 2],
                           [2, 1, 0],
                           [0, 3, 6]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Front"
        elif (side_name == "Bottom"):
            sides = ["Bottom", "Left", "Top", "Right"]
            if (row_column == 0):
                indexes = [[0, 1, 2],
                           [2, 5, 8],
                           [8, 7, 6],
                           [6, 3, 0]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Front"
            elif (row_column == 1):
                indexes = [[3, 4, 5],
                           [1, 4, 7],
                           [5, 4, 3],
                           [7, 4, 1]]
            else:
                indexes = [[6, 7, 8],
                           [0, 3, 6],
                           [2, 1, 0],
                           [8, 5, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Back"
        else:
            print("This is an INVALID OPTION!!")
            time.sleep(12)
            
    elif direction == "Right":
        print("Going Right")
        if (side_name == "Front"):
            sides = ["Front", "Right", "Back", "Left"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Bottom"
        elif (side_name == "Back"):
            sides = ["Back", "Left", "Front", "Right"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Bottom"
        elif (side_name == "Left"):
            sides = ["Left", "Front", "Right", "Back"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Bottom"

        elif (side_name == "Right"):
            sides = ["Right", "Back", "Left", "Front"]
            if (row_column == 0):
                indexes = [[0, 1, 2]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Top"
            elif (row_column == 1):
                indexes = [[3, 4, 5]]
            else:
                indexes = [[6, 7, 8]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Bottom"
        elif (side_name == "Top"):
            sides = ["Top", "Right", "Bottom", "Left"]
            if (row_column == 0):
                indexes = [[0, 1, 2],
                           [2, 5, 8],
                           [8, 7, 6],
                           [6, 3, 0]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Back"
            elif (row_column == 1):
                indexes = [[3, 4, 5],
                           [1, 4, 7],
                           [5, 4, 3],
                           [7, 4, 1]]
            else:
                indexes = [[6, 7, 8],
                           [0, 3, 6],
                           [2, 1, 0],
                           [8, 5, 2]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Front"
        elif (side_name == "Bottom"):
            sides = ["Bottom", "Right", "Top", "Left"]
            if (row_column == 0):
                indexes = [[0, 1, 2],
                           [6, 3, 0],
                           [8, 7, 6],
                           [2, 5, 8]]
                places = [6, 3, 0, 7, 4, 1, 8, 5, 2]
                affected_side = "Front"
            elif (row_column == 1):
                indexes = [[3, 4, 5],
                           [7, 4, 1],
                           [5, 4, 3],
                           [1, 4, 7]]
            else:
                indexes = [[6, 7, 8],
                           [8, 5, 2],
                           [2, 1, 0],
                           [0, 3, 6]]
                places = [2, 5, 8, 1, 4, 7, 0, 3, 6]
                affected_side = "Back"
        else:
            print("This is an INVALID OPTION!!")
            time.sleep(12)
    
    same_indexes = False
    for n in range(turns):
        current_color[:] = []
        # print("Current Side is " + str(current_side))
        sleep_time = 0
        for i in range(len(sides)):
            current_side = all_sides.index(sides[i])+1
            if i == 3:
                next_side = all_sides.index(sides[0])+1
                r = 0
            else:
                next_side = all_sides.index(sides[i+1]) + 1
                
            if i == 0:
                if (len(indexes) == 1):
                    same_indexes = True
                    q = 0
                    r = 0
                else:
                    q = 0
                    r = 1
                current_color.append((all_sides[current_side][indexes[q][0]], all_sides[current_side][indexes[q][1]], all_sides[current_side][indexes[q][2]]))
                 
            if ((same_indexes is False) and (i != 0) and (i != 3)):
                q = i
                r = i + 1
            
            temp_color[:] = []
            temp_color.append((all_sides[next_side][indexes[r][0]], all_sides[next_side][indexes[r][1]], all_sides[next_side][indexes[r][2]]))
            print("Current color is " + str(current_color))
            print(str(indexes[q][0]) + " " + str(indexes[q][1]) + " " + str(indexes[q][2]))
            time.sleep(sleep_time)
            
            # next_color.append((all_sides[next_side][indexes[r][0]], all_sides[next_side][indexes[r][1]], all_sides[next_side][indexes[r][2]])) 
            print("Next color is " + str(all_sides[next_side][indexes[r][0]]) + " " + str(all_sides[next_side][indexes[r][1]]) + " " + str(all_sides[next_side][indexes[r][2]]))
            print(str(indexes[r][0]) + " " + str(indexes[r][1]) + " " + str(indexes[r][2]))
            time.sleep(sleep_time)
            all_sides[next_side][indexes[r][0]] = current_color[0][0]
            all_sides[next_side][indexes[r][1]] = current_color[0][1]
            all_sides[next_side][indexes[r][2]] = current_color[0][2]

            current_color[:] = []
            current_color.append((temp_color[0][0], temp_color[0][1], temp_color[0][2]))
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

    
