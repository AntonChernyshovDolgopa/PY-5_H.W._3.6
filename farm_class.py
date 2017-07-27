class Animal:
    current_weight = 0 # in kilograms
    current_age = 0
    bird = True
    mammals = True


    def __init__(self, bird, mammals):
        self.mammals = mammals
        self.bird = bird


    def age(self, days):
        self.current_age += days

    def weight (self, kg):
        self.current_weight += kg

class Beefs():
    numbers_of_legs = 4
    horns = True


    def voice(self):
        print('Mu Mu')


class Goats(Animal, Beefs):
    hooves = True


    def voice(self):
        print('Beeeee')


goat_1 = Goats(False, True)
goat_1.voice()
print(goat_1.numbers_of_legs)
print (goat_1.hooves)
