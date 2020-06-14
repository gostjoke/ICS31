#c
print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)


hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)

#C2

Name = (input('what is your name?'))
print('Hello', Name)
print('It is nice to meet you.')
Age = int(input('How old are you?'))
print('Next year you will be', Age+1, 'years old')
print('Good-bye!')

#d

Krone_per_Euro = 7.42
Krone_per_Pound = 8.6 
Krone_per_Dollar = 6.62 

print('Please provide this information: ')
Business_Name = (input('Business name: '))
Number_of_Euros = int(input('Number of Euro: ', ))
Number_of_Pounds = int(input('Number of Pound: ', ))
Number_of_Dollars = int(input('Number of Dollar: ', ))

print('Copenhagen Chamber of Commerce')
Business_Name = (input('Business name: '))

print(Number_of_Euros, 'Euros is', float(Number_of_Euros*Krone_per_Euro), 'Krone')
print(Number_of_Pounds, 'Pounds is', float(Number_of_Pounds*Krone_per_Pound), 'Krone')
print(Number_of_Dollars, 'Dollars is', float(Number_of_Dollars*Krone_per_Dollar), 'Krone')

print('Total Krone: ', float(Number_of_Euros*Krone_per_Euro)+float(Number_of_Pounds*Krone_per_Pound)+float(Number_of_Dollars*Krone_per_Dollar))

#e
from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)

#e.1
print('the title of the book in the variable', still_another[0])
#e.2
print('the price of the book', another[-1])
#e.3
print('the average price of all three books', (favorite[-1]+still_another[-1]+still_another[-1])/3)
#e.4
print(favorite[-2] < 1900)
#e.5
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 26.00)
#e.6
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00*1.2)

#f
from collections import namedtuple
animal = namedtuple("Name", "species age weight favorite food")

#i
Elephant = animal('Jumbo', 'Elephant', 50, 1000, 'peanuts')
#ii
platypus = animal('Perry', 'platypus', 7, 1.7, 'shrimp')
print(Elephant[-2] < platypus[-2])

#g
booklist = [favorite, another, still_another]
#g1
print(favorite[-1]<another[-1])
print(booklist[1][-1]>booklist[1][-1]) #?

#g2
print(favorite[-2]>still_another[-2])
print(booklist[1][-2]<booklist[-1][-2])

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


