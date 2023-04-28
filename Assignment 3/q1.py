wordlist = [] 
#change to empty list
n = int(input(""))
for i in range(n):
    word = input("")
    lowerword = word.lower() #make lowercase
    special = [" ", ","]
    #remove comma and spaces
    def remove(lowerword):
        final_word = lowerword.replace(" ","")
        return final_word.replace(",", "")
#make list from user input words
    wordlist.append(remove(lowerword))
# print(wordlist)
dict = {}
for i in wordlist:
    sorted_list = ''.join(sorted(i))
    if sorted_list in dict:
        dict[sorted_list].append(i) #add word to dict as key
    else:
        dict[sorted_list] = [i] #add words that are the same as value
# print(dict)
value_list = []
for value in dict:
    last_list = dict.get(value)
    value_list += str(len(last_list))
print(max(value_list))