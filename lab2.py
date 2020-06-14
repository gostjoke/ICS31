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






