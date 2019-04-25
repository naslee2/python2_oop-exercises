list_one = ['celery','carrots','bread']
list_two = ['celery','carrots','break']

if cmp(list_one,list_two) == -1:
    print "The Lists are not the same"
elif cmp(list_one,list_two) == 1:
    print "The Lists are not the same"
else:
    print "The Lists are the same"

