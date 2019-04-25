# def one():
#     greeting = "hello"
#     name = "Dojo"
#     print name+greeting
# one()

# def two():
#     words = ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']
#     for i in words:
#         print i
# two()

# def three(x):
#     list =[]
#     x *= 2
#     list.append(x)
#     print list*25
# three(10)

# def four(g):
#     bob=""
#     for i in range(len(g)-1,-1,-1):
#         bob += (g[i])
#     print bob
# four("chicken")

def five():
    x = 10
    x = x * 7
    y = 30
    z = y + x
    z = z * 3
    z = z - y
    z = z / 27
    x = z + y
    y = 3
    x = x + y
    if x % 10 == 0:
        return True
    else:
        return False
print five()