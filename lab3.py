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





