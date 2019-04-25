word_list = ['hello','world','my','name','is','Anna']
words =[]
char = 'o'

for count in word_list:
    if char in count:
        words.append(count)
print words