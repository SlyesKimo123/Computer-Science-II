
mydict = {}
mydict['sir'] = 'matey'
mydict['hotel'] = 'fleabag inn'
mydict['student'] = 'swabbie'
mydict['boy'] = 'matey'
mydict['madam'] = 'proud beauty'
mydict['professor'] = 'foul blaggart'
mydict['restaurant'] = 'galley'
mydict['your'] = 'yer'
mydict['excuse'] = 'arr'
mydict['are'] = 'be'
mydict['lawyer'] = 'foul blaggart'
mydict['the'] = "th'"
mydict['restroom'] = 'head'
mydict['my'] = 'me'
mydict['hello'] = 'avast'
mydict['is'] = 'be'
mydict['man'] = 'matey'

user_input = str(input("Enter a random sentence and I will change it to Pirate language.\n"))

list_user_input = []        # Creates a new list of user_input
words = user_input.split()  # This splits up each word in the user_input
for word in words:          # This iterates thru each item of list_user_input, changing the key in mydict to the value
    if word in mydict:
        list_user_input.append(mydict[word])  # This singles out the word that is to be changed into Pirate
        print()
    else:                   # This is a list of the words that do not change to Pirate
        list_user_input.append(word)

#for k in mydict.items():
#    user_input = list_user_input.replace(k, mydict[k])
#print(user_input)

print((list_user_input))
