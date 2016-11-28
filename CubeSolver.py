import time
import Rubik_Info
import Solving_algorithm

try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *
    

# This Function sets the color that is chosen to the square it was clicked on
def hello(color):
    global coordinates, side, all_sides
    print("Hello at " + str(coordinates[0]) + " " + str(coordinates[1]))
    print("This is color " + color)
    Rubik_Info.ChangeColor(canvas, color, coordinates)
    Rubik_Info.Update_Array(all_sides[all_sides.index(side)+1], side, color, coordinates)
    

# When the mouse is clicked on a certain coordinates, then it will display
# The menu. When clicked outside the coordinates, then the menu dissapears
def callback(event):
    global Clicked, coordinates
    print("Hello World at coordinates " + str(event.x) + " " + str(event.y))
    if (event.x >= 98 and event.x <= 278 and event.y >= 90 and event.y <= 270):
            coordinates[0] = event.x
            coordinates[1] = event.y
            Clicked = True
            menu.post(event.x_root, event.y_root)
            
    elif (Clicked):
        Clicked = False
        menu.unpost()
        

# This adjusts the cube to the Top side when the button is clicked
def TopRubikCube():
    print("I am in my top section")
    global SideText, side, all_sides
    side = "Top"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
# This adjusts the cube to the Back side when the button is clicked
def BackRubikCube():
    print("I am in my Back section")
    global SideText, side, all_sides
    side = "Back"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    

# This adjusts the cube to the Front side when the button is clicked
def FrontRubikCube():
    print("I am in the front  section")
    global SideText, side, all_sides
    side = "Front"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    

# This adjusts the cube to the Bottom side when the button is clicked
def BottomRubikCube():
    print("I am in the bottom of the rubik cube")
    global SideText, side, all_sides
    side = "Bottom"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    

# This adjusts the cube to the Left side when the button is clicked
def LeftRubikCube():
    print("I am in the left of the left cube")
    global SideText, side, all_sides
    side = "Left"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    

# This adjusts the cube to the Right side when the button is clicked
def RightRubikCube():
    print("I am in the right of the rubik cube")
    global SideText, side, all_sides
    side = "Right"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    

# This checks for errors before solving the rubik cube
# (too little of a color or too many of a color).
# If error occurs, it exits the function and tells the user to fix it.
# If there are no errors, it will call the Solving_algorithm function
def Solve():
    global SideText, side, all_sides, ErrorText
    ErrorText.set("")
    print("In the solve function")
    colors = ["Red", 0, "White", 0, "Yellow", 0, "Green", 0, "Blue", 0, "Orange", 0, "dark gray", 0]  

    # Checks to see if there are any gray spots, or if there are more than 9 of a single color
    for i in xrange(1, len(all_sides), 2):
        print("I am in side " + str(all_sides[i-1]))
        # time.sleep(5)
        
        # 7 Colors to look for
        for j in xrange(1, len(colors), 2):
            # print("j is " + str(j))
            print("I am looking for color " + str(colors[j-1]))
            # print("Showing side \"" + str(all_sides[i-1]) + "\" colors\n" + str(all_sides[i]))
            # time.sleep(5)
            indices = [q for q, x in enumerate(all_sides[i]) if x == colors[j-1]]
            print("There are " + str(len(indices)) + " of the color " + str(colors[j-1]))
            # time.sleep(4)
            colors[j] += len(indices)
            print("There is a total of " + str(colors[j]) + " of  color " + colors[j-1])
            if (colors[j] > 9):
                ErrorText.set("ERROR! there is too many " + colors[j-1] + "\'s on this cube, there is a max of 9 of any color")
                return
            
            # print("There is " + str(colors[i]) + " of Color " + colors[j-1])
            if colors[13] != 0:
                ErrorText.set("ERROR!! You have unfilled out spots")
                # print(str(all_sides[i]))
                Rubik_Info.RubikSetup(canvas, all_sides[i])
                side = all_sides[i-1]
                SideText.set("You are currently on side: " + side)
                return
    Solving_algorithm.Solve_Cube(canvas, all_sides)
    
root = Tk()

menu = Menu(root, tearoff= 0)
menu.add_command(label="Red", command=lambda: hello("Red"))
menu.add_command(label="White", command=lambda: hello("White"))
menu.add_command(label="Yellow", command=lambda: hello("Yellow"))
menu.add_command(label="Green", command=lambda: hello("Green"))
menu.add_command(label="Blue", command=lambda: hello("Blue"))
menu.add_command(label="Orange", command=lambda: hello("Orange"))

Clicked = False
coordinates = [0,0]
all_sides = Rubik_Info.CreateCube()

Xmove = (root.winfo_screenwidth()*(1-0.3))/2  # 390, 120
Ymove = (root.winfo_screenheight()*(1-0.2))/2
# print("Xmove is " + str(Xmove) + " Ymove is " + str(Ymove))
root.geometry("%dx%d%+d%+d" % (480, 480, Xmove, Ymove-100))
canvas = Canvas(root, width = 480, height= 480)

canvas.bind("<Button-1>", callback)

TopButton = Button(root, text = "Top", command=TopRubikCube)
BackButton = Button(root, text = "Back", command =BackRubikCube)
FrontButton = Button(root, text = "Front", command =FrontRubikCube)
BottomButton = Button(root, text = "Bottom", command=BottomRubikCube)
LeftButton = Button(root, text = "Left", command=LeftRubikCube)
RightButton = Button(root, text = "Right", command=RightRubikCube)
SolveButton = Button(root, text = "Solve", command=Solve)

side = "Top"
SideText = StringVar()
SideText.set("You are currently on side: " + side)
outputs = Canvas(root, width = 30, height = 20)
SideFormatter = Label(root, textvariable=SideText)

ErrorText = StringVar()
ErrorText.set("")
# outputs = Canvas(root, width = 30, height = 20)
ErrorFormatter = Label(root, textvariable=ErrorText)

Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])


TopButton.pack(side=TOP)
BackButton.pack(side=TOP)
SideFormatter.pack(side=TOP)
ErrorFormatter.pack(side=TOP)
# outputs.pack(side=TOP)
BottomButton.pack(side=BOTTOM)
FrontButton.pack(side=BOTTOM)
LeftButton.pack(side=LEFT)
RightButton.pack(side=RIGHT)
SolveButton.pack()
SolveButton.place(bordermode=INSIDE, height = 100, width = 100, x = 370, y = 370)

canvas.pack(side=LEFT)
root.mainloop()
