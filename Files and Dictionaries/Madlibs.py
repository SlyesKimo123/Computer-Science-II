# Luke Chase --- 9/13
# Chap. 11 --- Files.  Madlibs Program
string = open("Madlibs.txt", 'r')
string = string.read()

input_for_one = input("What past tense verb would you like to insert? \n")
input_for_two = input("What adjective would you like to insert? \n")
input_for_three = input("What verb would you like to insert? \n")
input_for_four = input("What noun would you like to insert? \n")
input_for_five = input("What adjective would you like to insert? \n")
input_for_six = input("What noun would you like to insert? \n")
input_for_seven = input("What ajective would you like to insert? \n")
input_for_eight = input("What plural nouns would you like to insert? \n")

stringdict = {}
stringdict['1'] = input_for_one
stringdict['2'] = input_for_two
stringdict['3'] = input_for_three
stringdict['4'] = input_for_four
stringdict['5'] = input_for_five
stringdict['6'] = input_for_six
stringdict['7'] = input_for_seven
stringdict['8'] = input_for_eight

for (k,v) in stringdict.items():

    string.replace(k, v)

listt = []
words = string.split()
for word in words:
    if word in stringdict:
        listt.append(stringdict[word])
    else:
        listt.append(word)

#string = string.replace('1', input_for_one)
#string = string.replace('2', input_for_two)
#string = string.replace('3', input_for_three)
#string = string.replace('4', input_for_four)
#string = string.replace('5', input_for_five)
#string = string.replace('6', input_for_six)
#string = string.replace('7', input_for_seven)
#string = string.replace('8', input_for_eight)

print(" ".join(listt))
