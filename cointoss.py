import random

def cointoss():
    heads=0
    tails=0
    for count in range(1, 5001):
        x= random.randint(1,2)
        if x == 1:
            heads +=1
            print "Attempt #",count,": Throwing a coin... It's a head! ... Got", heads, "head(s) so far and ",tails," tail(s) so far"
        else:
            tails +=1
            print "Attempt #",count,": Throwing a coin... It's a tail! ... Got", heads, "head(s) so far and ",tails," tail(s) so far"
    print "Ending the Program, Thank You!"

cointoss()