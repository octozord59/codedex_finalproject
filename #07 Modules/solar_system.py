# #03 of Modules

from math import pi

from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)


if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    print('Oops! An error occured.')

area = 4 * pi * r * r

print(area, random_planet)




