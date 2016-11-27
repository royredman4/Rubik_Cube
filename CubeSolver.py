import time
import Rubik_Info

try:
    # for Python 2
    from Tkinter import *
except ImportError:
    # for Python 3
    from tkinter import *
    
    
def hello(color):
    global coordinates, side, all_sides
    print("Hello at " + str(coordinates[0]) + " " + str(coordinates[1]))
    print("This is color " + color)
    Rubik_Info.ChangeColor(canvas, color, coordinates)
    Rubik_Info.Update_Array(all_sides[all_sides.index(side)+1], side, color, coordinates)
    
    
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
        
        
def TopRubikCube():
    print("I am in my top section")
    global SideText, side, all_sides
    side = "Top"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
def BackRubikCube():
    print("I am in my Back section")
    global SideText, side, all_sides
    side = "Back"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
def FrontRubikCube():
    print("I am in the front  section")
    global SideText, side, all_sides
    side = "Front"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
def BottomRubikCube():
    print("I am in the bottom of the rubik cube")
    global SideText, side, all_sides
    side = "Bottom"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
def LeftRubikCube():
    print("I am in the left of the left cube")
    global SideText, side, all_sides
    side = "Left"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
def RightRubikCube():
    print("I am in the right of the rubik cube")
    global SideText, side, all_sides
    side = "Right"
    SideText.set("You are currently on side: " + side)
    Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])
    
    
def Solve():
    global SideText, side, all_sides
    print("In the solve function")
    colors = ["Red", 0, "White", 0, "Yellow", 0, "Green", 0, "Blue", 0, "Orange", 0, "dark gray", 0]  

    # Checks to see if there are any gray spots, or if there are more than 9 of a single color
    for i in range(1, len(all_sides)):
        # 7 Colors to look for
        print("I am in side " + str(all_sides[i]))
        time.sleep(5)
        for j in range(1, (len(colors)/2)):
            indexing = 0
            print("I am looking for color " + str(colors[j-1]))
            print("Showing side \"" + str(all_sides[i-1]) + "\" colors\n" + str(all_sides[i][0]))
            time.sleep(5)
            # Check for 9 of each color
            for z in range(1, 9):
                # indexing = all_sides[i][all_sides[i].index(colors[j-1], indexing)]
                indices = [i for i, x in enumerate(all_sides[i]) if x == colors[j-1]]
                print("There are " + str(len(indices)) + " of the color " + colors[j-1])
                time.sleep(4)
                if indexing == -1:
                    break
                colors[i] += 1
                print("There is " + str(colors[i]) + " of Color " + colors[i-1])
                if colors[13] != 0:
                    print("ERROR!! You have unfilled out spots")
                    Rubik_Info.RubikSetup(canvas, all_sides[i][all_sides.index(i+1)])
            j += 1
        i += 1
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
SideFormatter = Label(root, textvariable=SideText)  #, font= ("Helvetica",10), width = 12, height = 12, anchor=CENTER).pack()
Rubik_Info.RubikSetup(canvas, all_sides[all_sides.index(side)+1])


TopButton.pack(side=TOP)
BackButton.pack(side=TOP)
SideFormatter.pack(side=TOP)
# outputs.pack(side=TOP)
BottomButton.pack(side=BOTTOM)
FrontButton.pack(side=BOTTOM)
LeftButton.pack(side=LEFT)
RightButton.pack(side=RIGHT)
SolveButton.pack()
SolveButton.place(bordermode=INSIDE, height = 100, width = 100, x = 370, y = 370)

canvas.pack(side=LEFT)
root.mainloop()
