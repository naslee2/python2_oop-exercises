import random

def score(list):
    print "Scores and Grades"
    for i in range(0,10):
        x= random.randint(60, 100)
        if x > 89:
            print "Score: ", x,"; Your Grade is A"
        elif x <89 and x>79:
            print "Score: ", x,"; Your Grade is B"
        elif x <79 and x>69:
            print "Score: ", x,"; Your Grade is C"
        elif x <69 and x>59:    
            print "Score: ", x,"; Your Grade is D"
        else:
            print "Score: ", x,"; Your Grade is F"
    print "End of the Program. Bye!"
list = 0
score(list)