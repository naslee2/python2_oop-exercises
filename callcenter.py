class Call(object):
    def __init__(self, uniqueid,callername,phonenum,time,reason):
        self.uniqueid = uniqueid
        self.callername = callername
        self.phonenum = phonenum
        self.time = time
        self.reason = reason
    def display(self):
        print self.uniqueid, self.callername, self.phonenum, self.time, self.reason
        return self


class callcenter(object):
    def __init__(self):
        self.calllist = []
        self.queue = 0
    def add(self, y):
        self.calllist.append(y)
        self.queue +=1
        return self
    def remove(self,x):
        self.callername.pop(0)
        self.queue -=1
        return self
    def info(self):
        for i in range(0, len(self.calllist)):
            print self.calllist[i].phonenum, self.calllist[i].callername
        print self.queue
        return self

call1 = Call("w1we234e", "Bob","510-456-5555", "1030", "help")
call2 = callcenter()
call2.add(call1).info()
print call1.display()
print call2.info()
