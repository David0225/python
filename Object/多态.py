
class Animal:
    def __init__(self,name):
        self.name = name

    def talk(self):
        pass

    # @classmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('Mewo!')

class Dog(Animal):
    def talk(self):
        print('Woof!')



c = Cat('test1')
d = Dog('test2')

Animal.animal_talk(c)
Animal.animal_talk(d)