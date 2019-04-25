class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 0
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -=5
        return self
    def displayHealth(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog,self).__init__(name,health)
        self.health =150
    def pet(self):
        self.health +=5

dog1 = Dog("barko",100)
print dog1.walk().walk().walk().run().run().displayHealth()

class Dragon(Animal):
    def __init__(self,name, health):
        super(Dragon,self).__init__(name,health)
        self.health =170
    def fly(self):
        self.health -=10

dragon1 = Dragon("Burno",100)
print dragon1.walk().walk().walk().run().run().displayHealth()