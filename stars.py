def stars():
    x=[4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    char = "*"
    for count in range(0, len(x)):
        if type(x[count]) == int:
            print x[count]*char
        else:
            y = count
            print (len(x[count])*x[count][0]).lower()
stars()