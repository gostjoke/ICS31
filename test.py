# d
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

print('---------- Part (d.1) ----------')

#d.1
def restaurant_price(Restaurant:str) -> float:
    "takes a Restaurant and returns the value of the price."
    return Restaurant.price
    #should put .price not [ ]

assert restaurant_price(RC[0]) == 12.50
assert restaurant_price(RC[1]) == 5.50

print(restaurant_price(RC[2]))

print()

print('---------- Part (d.2) ----------')
#(d.2)

RC.sort(key=restaurant_price, reverse = False)
# reverse = False, from least expensive to most expensive
# reverse = True, from most expensive to least expensive
# no reverse, same as reverse = False
print(RC)

print()

print('---------- Part (d.3) ----------')

#(d.3)
def costliest(RC:list) -> str:
    "take a list of Restaurants, returns"
    RC.sort(key=restaurant_price, reverse = True)
    return RC[0].name
assert costliest(RC) == "Noma"

print (costliest(RC))

print()
print('---------- Part (d.4) ----------')
#(d.4) #not sure

def costliest2(RC:list) -> str:
    #no side effect
    sorted(RC, key = restaurant_price,reverse = False)
    return RC[-1].name


print(costliest2(RC))
print(RC)

print()





