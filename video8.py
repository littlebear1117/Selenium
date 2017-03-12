# About Class and object and

class Animal(object):
    name = '"'

    def eat(self):
        print ("%s Eating..." % self.name)

    def sleep(self):
        print ("%s Sleeping..." % self.name)

# Inheritance:
class Mammal(Animal):
    hasBackBone = True
    hasHaire = True

    def growHair(self):
        print("Growing ")

snake = Animal()
cat = Mammal()
dog = Mammal()

cat.name = "Shakes"
dog.name = "Molly"

cat.eat()
dog.sleep()

cat.growHair()
dog.growHair()

snake.eat()