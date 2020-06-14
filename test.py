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

#i.1
my_canvas.create_line(100, 100, 300, 100, fill='blue')  
my_canvas.create_line(300, 300, 300, 100, fill='orange')  
my_canvas.create_line(100, 300, 100, 100, fill='yellow')  
my_canvas.create_line(100, 300, 300, 300, fill='red')  

#i.2
my_canvas.create_line(200,100,100,200, fill='blue')
my_canvas.create_line(100,200,200,300, fill='red')
my_canvas.create_line(200,300,300,200, fill='yellow')
my_canvas.create_line(300,200,200,100, fill='orange')

#i.3
'''wall'''
my_canvas.create_line(100,100,200,100, fill='blue')
my_canvas.create_line(100,100,100,200, fill='blue')
my_canvas.create_line(200,100,200,200, fill='blue')
my_canvas.create_line(200,200,100,200, fill='blue')
'''roof'''
my_canvas.create_line(100,100,150,50, fill='red')
my_canvas.create_line(150,50,200,100, fill='red')
'''door'''
my_canvas.create_line(130,200,130,170,fill='black')
my_canvas.create_line(130,170,160,170,fill='black')
my_canvas.create_line(160,170,160,200,fill='black')
'''window'''
my_canvas.create_line(130,130,130,160,fill='yellow')
my_canvas.create_line(130,160,160,160,fill='yellow')
my_canvas.create_line(160,160,160,130,fill='yellow')
my_canvas.create_line(160,130,130,130,fill='yellow')
my_canvas.create_line(130,145,160,145,fill='yellow')
my_canvas.create_line(145,130,145,160,fill='yellow')

#i.4
'''eye'''
my_canvas.create_oval(200,300,300,400,fill='white')
my_canvas.create_oval(250,350,270,370,fill='black')


tkinter.mainloop()          # Combine all the elements and display the window

