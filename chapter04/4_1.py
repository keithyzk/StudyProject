class Cat(object):
    def say(self):
        print ("I am a cat")

class Dog(object):
    def say(self):
        print ("I am a dog")

class Duck(object):
    def say(self):
        print("I am a duck")

# animal = Cat
# animal().say()

animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()