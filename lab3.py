print('---------- Part (c) ----------')
#c.1
def abbreviate(a:str) -> str:
    " take a month as input and return month three-letter abbreviation"
    return a[0]+a[1]+a[2]
assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr'

print()
#(c.2)
def find_area_square(l) -> int:
    "take input number as length of a side and return the area of that square"
    return l*l
assert find_area_square(1) == 1
assert find_area_square(5) == 25

print()
#(c.3)
pi = 3.14159
def find_area_circle(r:int) -> int:
    "take its input the radius of a circl and return the area of that square"
    return r*r*pi
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975

print()
#(c.4)
def print_even_numbers(lst):
    "takes a list of integers as input and prints each even number on the list."
    for i in lst:
        if 1%2 == 0
            print(i)
print()

#(c.5)
def calculate_shipping(weight:int) -> int:
    "under 2 pounds, the rate is $2.00."
    if weight < 2:
        return 2
    "2 pounds but under 10 pounds, the rate is $5.00."
    if 2 <= weight < 10:
        return 5
    "packages of 10 pounds or more, the rate is $5.00 plus $1.50 per pound for each pound over 10."
    if weight >= 10:
        return 5 + (weight-10) * 1.5

assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50

print()


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

#(7)
def create_circle(x1, y1, r:int) -> int:
    "takes x-coordinate and y-coordinate of the upper-left corner of the square that encloses the circle and the diameter"
    x2 = x1+ r
    y2 = y1+ r
    return my_canvas.create_oval(x1,y1,x2,y2)

create_circle(100, 100, 200)

tkinker.mainloop()            #combine all the elements and diplay the window

print('---------- Part (d) ----------')
