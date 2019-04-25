class Bike(object):
    
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >0:
            self.miles -= 5
        return self

bike1 = Bike("50", "25mph")
print bike1.ride().ride().reverse().displayInfo()