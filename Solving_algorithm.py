import time
import Rubik_Info
import collections
import random

#############
import pudb


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
    if (number == 7):
        
        directions = []
        temp_directions = ["Up", "Down", "Left", "Right"]
        temp_sides = ["Front", "Back", "Left", "Right", "Top", "Bottom"]
        for i in range(30):
            row_col = random.randint(0, 2)
            direction = temp_directions[random.randint(0, 3)]
            side = temp_sides[random.randint(0, 5)]
            side_index = all_Sides.index(side) + 1
            Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
            directions.append((side, direction, row_col, move_amount))
            print("row_col is " + str(row_col) + " and direction is " + str(direction) + " at side " + side)
            #time.sleep(10)
            
        return directions
        

    '''
    if (number == 0):
        # Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
        Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
   
    # Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
    # Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
    '''
    
    if (number == 0 or number == 1):
        cube_rotation_tracker = Yellow_Cross(all_Sides)
        print("These are all the moves to get the yellow flower\n" + str(cube_rotation_tracker))
        Yellow_to_White_side(all_Sides)
        '''
        #side = "Front"
        side = "Front"
        side_index = all_Sides.index(side) + 1
        direction = "Left"
        row_col = 0
        move_amount = 1
        # Rubik_Info.RubikSetup(canvas, all_Sides[side_index])
        Rotate_Cube(all_Sides,side, all_Sides[side_index], row_col, direction, move_amount)
        '''
        
    ErrorText.set("Moving " + direction + " at row/col " + str(row_col) + " at " + side + " side")
    # cube_rotation_tracker.reverse()
    return cube_rotation_tracker


def Yellow_to_White_side(full_cube):

    temp = full_cube[full_cube.index("Bottom") + 1]
    indexes = [i for i, x in enumerate(temp) if x == "Yellow"]
        
    yellow_indexes = [s for s in indexes if s == 1
                      or s == 3
                      or s == 5
                      or s == 7]
    
    print("Yellow indexes on the yellow side are" + str(yellow_indexes))

    
    sides = ["Left", "Right", "Back", "Front"]
    print("Front side is " + str(full_cube[full_cube.index("Front") + 1]))
    time.sleep(10)
    while (len(yellow_indexes) != 4):
        
        for n in range(4):
            # top_index_color = Adjacent_to(sides[n], 1, "Top")
            # if (full_cube[full_cube.index("Top") + 1][top_index_color] == "Yellow"):
                
            if (full_cube[full_cube.index(sides[n]) + 1][1] == full_cube[full_cube.index(sides[n]) + 1][4]):
                print("The colors are both " + full_cube[full_cube.index(sides[n]) + 1][4] + " on side " + sides[n])
                current_edges = affected_sides(sides[n])
                
                if ([0, 1, 2] == current_edges[n][2]
                    or [0, 3, 6] == current_edges[n][2]):
                    row_col = 0
                else:
                    row_col = 2

                Rotate_Cube(full_cube, current_edges[n][0], full_cube[full_cube.index(current_edges[n][0])+1],row_col,  current_edges[n][1], 2)
                # cube_rotations.append([current_edges[n][0], current_edges[n][1], row_col, 2])

        Rotate_Cube(full_cube, "Left", full_cube[full_cube.index("Left") + 1], 0, "Left", 1)
        # cube_rotations.append([current_edges[n][0], current_edges[n][1], row_col, 2])
        indexes = [i for i, x in enumerate(temp) if x == "Yellow"]
        
        yellow_indexes = [s for s in indexes if s == 1
                          or s == 3
                          or s == 5
                          or s == 7]
    Rotate_Cube(full_cube, "Left", full_cube[full_cube.index("Left") + 1], 0, "Right", 1)

    
def Adjacent_to(current_side, current_white_index, adjacent_side):
    [0, 2, 6]
    if (current_side == "Top"):
        if current_white_index in [0, 3, 6] and adjacent_side == "Left":
            index = current_white_index / 3
            
        elif current_white_index in [6, 7, 8] and adjacent_side == "Front":
            index = current_white_index - 6
            
        elif current_white_index in [2, 5, 8] and adjacent_side == "Right":
            if current_white_index == 2:
                index = 2
            elif current_white_index == 5:
                index = 1
            else:
                index = 0
        elif current_white_index in [0, 1, 2] and adjacent_side == "Back":
            index = 2 - current_white_index

        else:
            print("ERROR!! Invalid Adjacency angle")
            
    elif (current_side == "Bottom"):
        if current_white_index in [0, 1, 2] and adjacent_side == "Front":
            index = 6 + current_white_index

        elif current_white_index in [0, 3, 6] and adjacent_side == "Left":
            if current_white_index == 0:
                index = 8
            elif current_white_index == 3:
                index = 7
            else:
                index = 6
                
        elif current_white_index in [2, 5, 8] and adjacent_side == "Right":
            if current_white_index == 2:
                index = 6
            elif current_white_index == 5:
                index = 7
            else:
                index = 8
                
        elif current_white_index in [6, 7, 8] and adjacent_side == "Back":
            if current_white_index == 6:
                index = 8
            elif current_white_index == 7:
                index = 7
            else:
                index = 6
                
    elif (current_side == "Front"):
        if current_white_index in [0, 1, 2] and adjacent_side == "Top":
            index = 6 + current_white_index
            
        elif current_white_index in [0, 3, 6] and adjacent_side == "Left":
            index = 2 + current_white_index

        elif current_white_index in [2, 5, 8] and adjacent_side == "Right":
            index = current_white_index - 2

        elif current_white_index in [6, 7, 8] and adjacent_side == "Bottom":
            index = current_white_index - 6
            
    elif (current_side == "Back"):
        if current_white_index in [0, 1, 2] and adjacent_side == "Top":
            index = 2 - current_white_index
            
        elif current_white_index in [0, 3, 6] and adjacent_side == "Right":
            index = 2 + current_white_index

        elif current_white_index in [2, 5, 8] and adjacent_side == "Left":
            index = current_white_index - 2

        elif current_white_index in [6, 7, 8] and adjacent_side == "Bottom":
            if current_white_index == 6:
                index = 8
            elif current_white_index == 7:
                index = 7
            else:
                index = 6
                
    elif (current_side == "Left"):
        if current_white_index in [0, 1, 2] and adjacent_side == "Top":
            index = current_white_index * 3
            
        elif current_white_index in [0, 3, 6] and adjacent_side == "Back":
            index = 2 + current_white_index

        elif current_white_index in [2, 5, 8] and adjacent_side == "Front":
            index = current_white_index - 2

        elif current_white_index in [6, 7, 8] and adjacent_side == "Bottom":
            if current_white_index == 6:
                index = 6
            elif current_white_index == 7:
                index = 3
            else:
                index = 0
    elif (current_side == "Right"):
        if current_white_index in [0, 1, 2] and adjacent_side == "Top":
            if current_white_index == 0:
                index = 8
            elif current_white_index == 1:
                index = 5
            else:
                index = 2
            
        elif current_white_index in [0, 3, 6] and adjacent_side == "Front":
            index = 2 + current_white_index

        elif current_white_index in [2, 5, 8] and adjacent_side == "Back":
            index = current_white_index - 2

        elif current_white_index in [6, 7, 8] and adjacent_side == "Bottom":
            if current_white_index == 6:
                index = 2
            elif current_white_index == 7:
                index = 5
            else:
                index = 8
    else:
        print("Invalid current side!!")

    return index
    # I need to write the adjacency of every side
    # Ex: White side index 0 is related to Left side index 0
    # Left side index 5 is adjacent to front side index 3
    # Might not need to return what side its from since the index number
    # identifies what side its on
    

def Yellow_Cross(full_cube):
    cube_rotations = []
    Left_sides = ["Front", "Left", "Back", "Right"]
    Top_sides = ["Front", "Top", "Back", "Bottom"]
    white_side = ""
    yellow_side = ""
    
    for i in range(1, len(full_cube), 2):
        # print("i is " + str(i))
        if (full_cube[i][4] == "White"):
            white_side = full_cube[i-1]
            break
        
    print("The white middle side is located on side " + white_side)

    turns = 0
    if (white_side == "Top"):
        # No changes are needed
        print("White side is Top" + white_side)
        
    elif (white_side in Left_sides):
        turns = 1
    else:
        turns = 2
        
    Rotate_Cube(full_cube, white_side, full_cube[full_cube.index(white_side) + 1], 1, "Up", turns)    
    if (turns != 0):
        cube_rotations.append([white_side, "Up", 1, turns])
    print("White side should be on the top side now\n\n" + str(full_cube[full_cube.index("Top") + 1]))
    # time.sleep(20)
    white_side = "Top"
    yellow_side = "Bottom"
    yellow_edges = affected_sides(yellow_side)
    white_edges = affected_sides(white_side)
    # Continue on from here. Should be able to easily manipulate the left right front and back side
    # Make a function that relates an index on the white side and the index of the left/right/front/back side for easy looking
    '''
    if white_side in Left_sides:
        print("in left side")
        side_index = Left_sides.index(white_side) + 2
        if (side_index > 3):
            side_index = (side_index - 3) - 1
            print("side index is " + str(side_index))
        yellow_side = Left_sides[side_index]
    else:
        print("in Top Sides")
        side_index = Top_sides.index(white_side) + 2
        print("side index is " + str(side_index))
        if (side_index > 3):
            side_index = (side_index - 3) - 1
        yellow_side = Top_sides[side_index]
        
    print("The yellow side is side " + yellow_side)
    time.sleep(0)
    yellow_edges = affected_sides(yellow_side)
    white_edges = affected_sides(white_side)
    '''
    side = ["Left", "Right", "Back", "Front", "Bottom"]
    for n in range(4):
        temp = full_cube[full_cube.index(white_edges[n][0]) + 1]
        # print("Temp is " + str(temp))
        print("The " + side[n] + " side of white_side is" + str(white_edges[n])
              + "\n" + "and the edge colors are ")
        print(temp[white_edges[n][2][0]] + " "
              + temp[white_edges[n][2][1]] + " "
              + temp[white_edges[n][2][2]])

    time.sleep(0)
    white_temp = full_cube[full_cube.index(white_side) + 1]
    print("White side is " + str(white_temp))
    white_cross_index = [j for j, x in enumerate(white_temp)
                         if ((x == "Yellow") and
                             (j == 1 or j == 3 or
                              j == 5 or j == 7))]
    print("Important yellow indexes on white side is " + str(white_cross_index))
    time.sleep(0)
    important_indexes = [1, 5, 7, 3]
    for q in range(10): # 5
        if (len(white_cross_index) == 4):
            break
        
        if (q > 4):
            q = q - 5
        if (q == 4):
            temp = full_cube[full_cube.index(yellow_side) + 1]
        # elif (q == 5):
        #    temp = full_cube[full_cube.index(white_side) + 1]
        else:
            temp = full_cube[full_cube.index(white_edges[q][0]) + 1]
        if (q != 4):
            print("Searching for yellow color on side " + str(white_edges[q][0]) + "\n" + str(temp))
        else:
            print("Searching for yellow color on side " + yellow_side + "\n" + str(temp))
            
        indexes = [i for i, x in enumerate(temp) if x == "Yellow"]
        print("Indexes is " + str(indexes))
        

        
        useful_indexes = [s for s in indexes if s == 1
                          or s == 3
                          or s == 5
                          or s == 7]
        print("Our useful_indexes is " + str(useful_indexes))
        if (q != 4):
            side_edges = affected_sides(white_edges[q][0])
            print("The side edges for " + white_edges[q][0] + " is \n" + str(side_edges))
        ####################################################################################
        time.sleep(0)
        # pudb.set_trace()
        White_rotation_count = 0

        if (q != 4):
            index_identifier = []
            index_identifier.append(Adjacent_to(side[q], 0, white_side))
            index_identifier.append(Adjacent_to(side[q], 1, white_side))
            index_identifier.append(Adjacent_to(side[q], 2, white_side))
            rotation_block = [[0, 3, 6], [6, 7, 8], [8, 5, 2], [2, 1, 0]]
            rotation_index = rotation_block.index(index_identifier)
            white_indexes = [[1, 7], [7, 1], [5, 3], [3, 5]]
        while (len(useful_indexes) > 0 and q != 4):
            needs_rotation = False
            if (3 not in useful_indexes and (5 not in useful_indexes)):
                if ([0, 1, 2] == side_edges[q][2]
                    or [0, 3, 6] == side_edges[q][2]):
                    row_col = 0
                else:
                    row_col = 2
                Rotate_Cube(full_cube, side_edges[q][0], full_cube[full_cube.index(side_edges[q][0])+1],row_col,  side_edges[q][1], 1)
                cube_rotations.append([side_edges[q][0], side_edges[q][1], row_col, 1])
                indexes = [i for i, x in enumerate(temp) if x == "Yellow"]
                print("Indexes is " + str(indexes))
                useful_indexes = [s for s in indexes if s == 1
                                  or s == 3
                                  or s == 5
                                  or s == 7]
            
            if (index_identifier == [0, 3, 6]):
                if (3 in useful_indexes):
                    if (white_indexes[q][0] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 0, "Up", 1)
                        cube_rotations.append([side[q], "Up", 0, 1])
                elif (5 in useful_indexes):
                    if (white_indexes[q][1] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 2, "Up", 1)
                        cube_rotations.append([side[q], "Up", 2, 1])
            elif (index_identifier == [6, 7, 8]):
                if (3 in useful_indexes):
                    if (white_indexes[q][0] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 0, "Up", 1)
                        cube_rotations.append([side[q], "Up", 0, 1])
                elif (5 in useful_indexes):
                    if (white_indexes[q][1] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 2, "Up", 1)
                        cube_rotations.append([side[q], "Up", 2, 1])
            elif (index_identifier == [8, 5, 2]):
                if (3 in useful_indexes):
                    if (white_indexes[q][0] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 0, "Up", 1)
                        cube_rotations.append([side[q], "Up", 0, 1])
                elif (5 in useful_indexes):
                    if (white_indexes[q][1] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 2, "Up", 1)
                        cube_rotations.append([side[q], "Up", 2, 1])
            elif (index_identifier == [2, 1, 0]):
                if (3 in useful_indexes):
                    if (white_indexes[q][0] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 0, "Up", 1)
                        cube_rotations.append([side[q], "Up", 0, 1])
                elif (5 in useful_indexes):
                    if (white_indexes[q][1] in white_cross_index):
                        White_rotation_count += 1
                        needs_rotation = True
                    else:
                        Rotate_Cube(full_cube, side[q], full_cube[full_cube.index(side[q]) + 1], 2, "Up", 1)
                        cube_rotations.append([side[q], "Up", 2, 1])
            useful_indexes = [s for s in indexes if s == 1
                              or s == 3
                              or s == 5
                              or s == 7]
            if (needs_rotation):
                print("We are in side " + side[q] + " and a yellow index on White Side is in 3 or 5 " + str(useful_indexes))
                print("We are rotating white side")
                Rotate_Cube(full_cube, "Left", full_cube[full_cube.index("Left") + 1], 0, "Left", 1)
                cube_rotations.append(["Left", "Left", 0, 1])
                if (rotation_index == 3):
                    rotation_index = 0
                else:
                    rotation_index += 1
                index_identifier = rotation_block[rotation_index]

            indexes = [i for i, x in enumerate(temp) if x == "Yellow"]
            print("Indexes is " + str(indexes))
        
            white_cross_index = [j for j, x in enumerate(white_temp)
                         if ((x == "Yellow") and
                             (j == 1 or j == 3 or
                              j == 5 or j == 7))]
            print(" White side yellow indexes are now " + str(white_cross_index))
        
            useful_indexes = [s for s in indexes if s == 1
                            or s == 3
                            or s == 5
                            or s == 7]
            print(side[q] + " side yellow indexes are now " + str(useful_indexes))
            time.sleep(0)
        Rotate_Cube(full_cube, "Left", full_cube[full_cube.index("Left") + 1], 0, "Right", White_rotation_count)
        if (White_rotation_count != 0):
            cube_rotations.append(["Left", "Right", 0, White_rotation_count])
        print("Our useful_indexes is " + str(useful_indexes))
        print("Our useful_indexes is " + str(useful_indexes))

        '''
        Check to see if both the current side and the white side are not the top or bottom. 
        If they are not, then the logic of shifting to the left/right should apply as normal
        for indexes 1 and 7. Indexes 3 and 5 will have to be rotated clockwise in order to move to the white spot.
        
        If one of the sides is the top or bottom, then the opposite is applicable to the indexes.
        index 3 and 5 can be shifted up/down and indexes 1 and 7 will need to be rotated clockwise and then moved
        in its respected spot
        '''
        
        time.sleep(0)
        side_test = [3, 5]
        horizontal_test = [1, 7]
        if (q == 4):
            for n in range(len(useful_indexes)):
                rotated_index = " "
                if ((useful_indexes[n] in white_cross_index and
                     yellow_side in ["Front", "Back", "Left", "Right"] and
                     useful_indexes[n] in horizontal_test) or

                    (useful_indexes[n] in white_cross_index and
                     yellow_side in ["Top", "Bottom"] and
                     useful_indexes[n] in side_test) or

                    (yellow_side in ["Top", "Bottom"] and
                     useful_indexes[n] in horizontal_test and
                     horizontal_test[not(horizontal_test.index(useful_indexes[n]))] in white_cross_index) or
                    
                    (yellow_side in ["Front", "Back", "Left", "Right"] and
                     useful_indexes[n] in side_test and
                     side_test[not(side_test.index(useful_indexes[n]))] in white_cross_index)):
                    
                    rotation_turns = 0
                    # pudb.set_trace()

                    # Need to look if the white/yellow side is Back/Right or Left/Right and white side has yellow in index 3 and yellow side has a yellow in index 5 or vice versa 
                    
                    while((useful_indexes[n] in white_cross_index and
                           yellow_side in ["Front", "Back", "Left", "Right"] and
                           useful_indexes[n] in horizontal_test) or

                          (useful_indexes[n] in white_cross_index and
                           yellow_side in ["Top", "Bottom"] and
                           useful_indexes[n] in side_test) or

                          (yellow_side in ["Top", "Bottom"] and
                           useful_indexes[n] in horizontal_test and
                           horizontal_test[not(horizontal_test.index(useful_indexes[n]))] in white_cross_index) or
                    
                          (yellow_side in ["Front", "Back", "Left", "Right"] and
                           useful_indexes[n] in side_test and
                           side_test[not(side_test.index(useful_indexes[n]))] in white_cross_index)):

                        
                        print(str(useful_indexes[n]) + " is in the white indexes " + str(white_cross_index))
                        
                        print("I need to rotate the yellow cube and then move the yellow index into its proper spot on the white side of the cube")
                        print("Yellow side is " + str(full_cube[full_cube.index(yellow_side) + 1]))
                        rotated_index = important_indexes.index(useful_indexes[n])
                        if (rotated_index == 3):
                            rotated_index = important_indexes[0]
                        else:
                            rotated_index = important_indexes[rotated_index + 1]
                        
                        rotation_turns += 1
                        useful_indexes[n] = rotated_index
                        print("Your new rotated index is " + str(useful_indexes[n]))
                    
                    
                    if (yellow_edges[0][1] == "Up" or yellow_edges[0][1] == "Down"):
                        temp_helper = ["Up", "Down"]
                        direction = yellow_edges[0][1]
                        if (yellow_edges[0][2][0] == 2):
                            row_col = 2
                        else:
                            row_col = useful_indexes[n] / 3

                    elif (yellow_edges[0][1] == "Left" or yellow_edges[0][1] == "Right"):
                        temp_helper = ["Left", "Right"]
                        direction = yellow_edges[0][1]
                        if (yellow_edges[0][2][0] == 0):
                            row_col = 0
                        else:
                            row_col = 2

                    # rotates the yellow side clockwise
                    if (rotation_turns == 0):
                        Rotate_Cube(full_cube, yellow_edges[0][0], full_cube[full_cube.index(yellow_edges[0][0]) + 1], row_col, direction, 1)
                        cube_rotations.append((yellow_edges[0][0], direction, row_col, 1))
                    else:
                        for i in range(rotation_turns):
                            Rotate_Cube(full_cube, yellow_edges[0][0], full_cube[full_cube.index(yellow_edges[0][0]) + 1], row_col, direction, 1)
                        cube_rotations.append([yellow_edges[0][0], direction, row_col, rotation_turns])
                
                print(str(useful_indexes[n]) + " is not in the white indexes " + str(white_cross_index))
                if (useful_indexes[n] == 1 or useful_indexes[n] == 7):
                    print(str(useful_indexes[n]) + " divided by 3 is row_col " + str(useful_indexes[n] / 3))
                    direction = "Left"
                    new_row = useful_indexes[n] / 3
                else:
                    direction = "Up"
                    if (useful_indexes[n] in [0, 3, 6]):
                        print("we are moving up in column 0")
                        new_row = 0
                    else:
                        print("we are moving up in collumn 2")
                        new_row = 2

                print("Now rotating the yellow sections to the white side")
                Rotate_Cube(full_cube, yellow_side, full_cube[full_cube.index(yellow_side) + 1], new_row, direction, 1)
                Rotate_Cube(full_cube, yellow_side, full_cube[full_cube.index(yellow_side) + 1], new_row, direction, 1)
                cube_rotations.append([yellow_side, direction, new_row, 2])
                if (rotated_index != " "):
                    direction = temp_helper[not(temp_helper.index(yellow_edges[0][1]))]
                    for i in range(rotation_turns):
                        Rotate_Cube(full_cube, yellow_edges[0][0], full_cube[full_cube.index(yellow_edges[0][0]) + 1], row_col, direction, 1)
                    cube_rotations.append([yellow_edges[0][0], direction, row_col, rotation_turns])
                print("Yellow side should back in its original indexes now \n" + str(full_cube[full_cube.index(yellow_side) + 1]))
                time.sleep(10)
                
        '''
        if (useful_indexes):
            print("Im in the shifting section")
            # If there isn't an important yellow piece on the white side
            # if (len(white_cross_index) == 0):
            if (useful_indexes):
                if (white_edges[q][1] == "Up" or white_edges[q][1] == "Down"):
                    new_turn = "Left"
                    if (white_edges[q][2][0] == 2):
                        old_row = 2
                    else:
                        old_row = 0
                        
                    if (1 in useful_indexes):
                        new_row = 0
                        number = 1
                    elif (3 in useful_indexes):
                        new_row = 1
                        number = 3
                        print("This 3 and 5 index wont work right")
                    elif (5 in useful_indexes):
                        new_row = 1
                        number = 5
                        print("This 3 and 5 index wont work right")
                    elif (7 in useful_indexes):
                        new_row = 2
                        number = 7
                    else:
                        print("End of useful_indexes")
                else:
                    new_turn = "Up"
                    if (white_edges[q][2][0] == 0):
                        old_row = 0
                    else:
                        old_row = 2
                    if (1 in useful_indexes):
                        print("Figure index 1 and 7 later")
                        new_row = 1
                        number = 1
                    elif (7 in useful_indexes):
                        number = 7
                        print("Figure index 1 and 7 later")
                        new_row = 1
                    elif (3 in useful_indexes):
                        new_row = 0
                        number = 3
                    elif (5 in useful_indexes):
                        new_row = 2
                        number = 5
                    else:
                        print("ERROR, bad move")
                if (number in white_cross_index):
                    Rotate_Cube(full_cube, white_edges[q][0], full_cube[full_cube.index(white_edges[q][0])], white_edges[q][3], old_row, 1)
                    Rotate_Cube(full_cube, white_edges[q][0],full_cube[full_cube.index(white_edges[q][0])], new_row, new_turn, 1)
                    Rotate_Cube(full_cube, white_edges[q][0], full_cube[full_cube.index(white_edges[q][0])], white_edges[q][3], old_row, 3)
                    
                white_temp = full_cube[full_cube.index(white_side) + 1]
                print("White side is " + str(white_temp))
                white_cross_temp = [j for j, x in enumerate(white_temp)
                                    if ((x == "Yellow") and
                                        (j == 1 or j == 3 or
                                         j == 5 or j == 7))]
                if (len(white_cross_index) == len(white_cross_temp)):
                    Rotate_Cube(full_cube, white_edges[q][0],full_cube[full_cube.index(white_edges[q][0])], new_row, new_turn, 1)
                print("White side is now " + str(full_cube[full_cube.index(white_side) + 1]))
                time.sleep(10)
        time.sleep(10)
    '''

    '''
    The sides that we care about are the sides before and after
    the white_side. If we look at index 1, 3, 5, or 7 of the
    other two sides for the color yellow, we could manipulate
    those to be sent to the white_side
    '''
    '''
    Make a function to tell the program what is adjacent to
    the white_side. Use the "Affected side" from the Rotate_Cube
    to easily identify which row_col  is one row below the white
    side and to identify all of the sides that are adjacent to the
    white side.
    '''
    
    return cube_rotations

def affected_sides(current_side):
    # Current Side could be either the white side or yellow side
    #[["Top", "Up", 2, 1]]
    ## side, direction, row_col, move_amount
    '''
    Make sure these are ordered as so:
    (Left side of current_side, right_side of current_side,
    front_side of current_side, back_side of current_side)
    '''

    # I Might need to change from row_col 1 to indexes [3, 4, 5] instead
    if (current_side == "Front"):
        return ([["Left", "Up", [2, 5, 8], 1],
                 ["Right", "Up", [0, 3, 6], 1],
                 ["Top", "Left", [6, 7, 8], 1],
                 ["Bottom", "Left", [0, 1, 2], 1]])

    elif (current_side == "Back"):
        return([["Right", "Up", [2, 5, 8], 1],
                ["Left", "Up", [0, 3, 6], 1],
                ["Top", "Left", [0, 1, 2], 1],
                ["Bottom", "Left", [6, 7, 8], 1]])

    elif (current_side == "Left"):
        return([["Back", "Up", [2, 5, 8], 1],
                ["Front", "Up", [0, 3, 6], 1],
                ["Top", "Up", [0, 3, 6], 1],
                ["Bottom", "Up", [0, 3, 6], 1]])

    elif (current_side == "Right"):
        return([["Front", "Up", [2, 5, 8], 1],
                ["Back", "Up", [0, 3, 6], 1],
                ["Top", "Up", [2, 5, 8], 1],
                ["Bottom", "Up", [2, 5, 8], 1]])

    elif (current_side == "Top"):
        return([["Left", "Left", [0, 1, 2], 1],
                ["Right", "Left", [0, 1, 2], 1],
                ["Back", "Left", [0, 1, 2], 1],
                ["Front", "Left", [0, 1, 2], 1]])

    elif (current_side == "Bottom"):
        return([["Left",  "Right", [6, 7, 8], 1],
                ["Right", "Left", [6, 7, 8], 1],
                ["Front", "Left", [6, 7, 8], 1],
                ["Back", "Left", [6, 7, 8], 1]])

    else:
        print("ERROR!! WRONG INPUT!!")
        time.sleep(12)

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

    
