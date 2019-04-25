# class MathDojo(object):
#     def __init__(self):
#         self.total = 0
#     def add(self,*num):
#         for i in num:
#             self.total += i
#         return self
#     def subtract(self,*num):
#         for i in num:
#             self.total -= i
#         return self
#     def result(self):
#         print self.total
#         return self
# math1 = MathDojo()
# print math1.add(2,2,4).subtract(5).result()

class MathDojo2(object):
    def __init__(self):
        self.total = 0
    def add(self,*num):
        for i in num:
            if type(i) == list or type(i) == tuple:
                for x in i:
                    self.total += x
            else:    
                self.total += i
        return self
    def subtract(self,*num):
        for e in num:
            if type(e) == list or type(e) == tuple:
                for y in e:
                    self.total -= y
            else:
                self.total -= e
        return self
    def result(self):
        print self.total
        return self

math2 = MathDojo2()
print math2.add(1,2,3,[1,3,1],(1,2)).subtract(1,2,3,[1,1,1,],(2,7)).result()