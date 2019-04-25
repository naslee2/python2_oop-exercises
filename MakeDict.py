# def MakeDict():
#     name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
#     favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

#     newdict ={}
#     newdict = zip(name, favorite_animal)
#     print newdict

# MakeDict()

def MakeDict2():
    name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
    favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

    newdict =[]
    if len(name) > len(favorite_animal):
        
    elif len(name) < len(favorite_animal):
        newdict.append((favorite_animal,name))
    elif len(name) == len(favorite_animal):
        newdict.append((name, favorite_animal))
    else:
        print "nope"
    
    
    print newdict

MakeDict2()