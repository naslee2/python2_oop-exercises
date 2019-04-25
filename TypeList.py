l = ['magical unicorns',19,'hello',98.98,'world']
st = []
su = []

#if all(isinstance(check, int) for check in l) == False:
    #print "The list you entered is of mixed type"
for check in l:
    if type(check) == str:
        st.append(check)
    elif type(check) == float:
        su.append(check)
    elif type(check) == int:
        su.append(check)
    else:
        print "Nope"
print "String: ", st
print "Sum: ", sum(su)
