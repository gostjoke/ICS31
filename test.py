#h
from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]

#h.1
print(RC[2][0])
#h.2
print(RC[0][1] == RC[3][1])
#h.3
print(RC[6][4])
#h.4
RC.sort()
print(RC) #cannot print sort.(functionn)
#print(sorted(RC))
#h.5
print(sorted(RC)[-1][-2])
#print(sorted.RC[-1].dish)
#h.6
lst=[sorted(RC)[0], sorted(RC)[1], sorted(RC)[-1], sorted(RC)[-2]]
print(lst)

#i
Python exercises:

Python comes with a library called tkinter that enables drawing and other image processing. (It also supports graphical user interfaces (GUIs)—meaning code that displays menus and buttons and responds to mouse actions—but that's a topic for ICS 32.)

Here is the code to create a window and draw an "X":

import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 100, 300, 300, fill='orange') # Draw orange line
my_canvas.create_line(300, 100, 100, 300, fill='blue')   # Draw blue line

tkinter.mainloop()          # Combine all the elements and display the window

