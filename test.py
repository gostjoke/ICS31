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
print()







