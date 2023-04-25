# #02 of Classes and Objects

class Resturant():
    name = ''
    type = ''
    rating = 0.0
    two_doors = False


bobs_burgers = Resturant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.type = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.two_doors = False

print(vars(bobs_burgers))

mcdonalds = Resturant()

mcdonalds.name = 'McDonalds'
mcdonalds.type = 'Fast Food'
mcdonalds.rating = '2.3'
mcdonalds.two_doors = True

print(vars(mcdonalds))

chick_fil_a = Resturant()

chick_fil_a.name = "Chick-Fil-A"
chick_fil_a.type = 'Fast Food'
chick_fil_a.rating = 4.6
chick_fil_a.two_doors = False

print(vars(chick_fil_a))
