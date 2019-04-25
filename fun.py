def off_even(x):
    for i in range(1,2000):
        if(i % 2 == 0):
            print "Number is ", i, "This is an even number"
        else:
            print "Number is ", i, "This is an odd number"
x=0
off_even(x)

def multiply(a,y):
    for count in range(0,len(a)):
        a[count] *= y
    print a
y=5
a = [2,4,10,16]
multiply(a,y)

def layered_multiples(m):
    g=[]
    g.append(multiply(m,3))
    print g
m=[1,2,3]
layered_multiples(m)
