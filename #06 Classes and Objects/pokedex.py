# #05 FINAL of Classes and Objects

class Pokemon():
    def __init__(self, entry, name, type, description, is_caught):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        if self.name == 'Gyarados':
            return 'rawr'
        elif self.name == 'Pikachu':
            return 'pika-pika'
        elif self.name == 'Slowpoke':
            return 'moo'
        else:
            return "Unrecognized"

        

pikachu = Pokemon(1, 'Pikachu', ['Lightning', 'Speed'], 'Very fast pokemon', True)

print(pikachu.speak())

gyarados = Pokemon(2, 'Gyarados', ['Water', 'Wind'], 'Swims fast', False)

print(gyarados.speak())

slowpoke = Pokemon(3, 'Slowpoke', ['Dark', 'Slow'], 'Very slow, attacks hard', True)

print(slowpoke.speak())


