class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12

    def displayAll(self):
        if self.price >10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        print self.price, self.speed, self.fuel, self.mileage, self.tax
        return self

car1 = Car(3000,"35mph","Full","30mpg")
print car1.displayAll()