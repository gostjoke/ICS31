#c.6
import tkinter              # load the library; do this just once per program

my_window = tkinker.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500) # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

#x-values extend positively to the right and y-values extend positively down

#(6)
def create_square(x1, y1, l:int) -> int: 
    "take x-coordinate and y-coordinate of the upper-left corner and the length of a side."
    x2 = x1+ l
    y2 = y1+ l
    return my_canvas.create_rectangle(x1,y1,x2,y2)

create_square(100,100,200)



tkinker.mainloop()           #combine all the elements and diplay the window

