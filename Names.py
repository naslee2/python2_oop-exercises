def names():
    users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
    }

    print "Students"
    x =0
    for values in users['Students']:
        x+=1
        print x,"-", values['first_name'], values['last_name'],"-", len(values['first_name']+values['last_name'])

    print "Instructors"
    y =0
    for values in users['Instructors']:
        y+=1
        print y,"-", values['first_name'], values['last_name'],"-", len(values['first_name']+values['last_name'])
names()

#for i in range(0, len(users)):
        #for value in data:
        #print students[i].get('first_name'), students[i].get('last_name')