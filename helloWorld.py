words = "it's Thanksgiving day. It's my birthday too!"
print words.find("day")
#18
print words.replace("day","month")
#it's Thanksgiving month. It's my birthmonth too!

x = [2,54,-2,7,12,98]
print min(x)
#-2
print max(x)
#98

x = ["hello",2,54,-2,7,12,98,"world"]
print max(x)
#world
print min(x)
#-2

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
#[-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
x1=x[:6]
x2=x[6:]
new=[x1,x2]
print new