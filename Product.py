class Product(object):
    def __init__(self,price,item_name,weight,brand,status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        if self.status == "sell":
            self.status = "sold"
        elif self.status == "defective":
            self.status = "defective"
        elif self.status == "opened":
            self.status = "used"
        else:
            self.status = "for sale"
        return self

    def addTax(self):
        if self.status == "sold":
            self.price = (self.price * 0.0975) + self.price
        return self

    def Return(self):
        if self.status == "used":
            self.price = self.price - (self.price*0.20)
        elif self.status == "defective":
            self.price = 0
        else:
            "nope"
        return self

    def displayInfo(self):
        print self.price, self.item_name, self.weight, self.brand, self.status
        return self

product1 = Product(30,"Kitten Sandwich","3 ounces","Subway","opened")
print product1.sell().addTax().Return().displayInfo()