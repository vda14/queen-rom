
n = int(input(""))
count = ['0']
words = input("")    
wordlist = words.split()
for i in range(1, n + 1):    
    x = str(i)
    file = open(x + '.txt', 'r')
    dict = ''
    for line in file.readlines():
        dict = dict + ' ' + line.replace('\n', '')
        no_space_dict = dict.lstrip()
    #print(no_space_dict)
    newdict = []
    newdict = newdict + no_space_dict.split(' ') 
    #print(newdict)
    from collections import Counter
    #print(Counter(newdict))
    file.close()
# I have the count of all words in n.txt - look for key value in Counter dictionary and add the values
    value = 0
    for item in wordlist:        
        if item in (Counter(newdict)).keys():
            value += Counter(newdict).get(item)            
        else:
            value += 0
    count += str(value)
#print(count)
file_number = count.index(max(count))
if file_number >= 1:
    print(count.index(max(count)))