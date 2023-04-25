# #03 of Classes and Objects



class City():
    def __init__(self, name, country, population, landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


nyc = City('New York City', 'U.S.A', 8468000, ['Empire State building,', 'Statue of Liberty', 'Central Park'])

print(vars(nyc))

asburn = City('Ashburn', 'U.S.A', 44000, ['Ashburn Park', 'Almano Drafthouse Cinema One Loudoun', 'iFLY indoor Skydiving - Loudoun'])

print(vars(asburn))




