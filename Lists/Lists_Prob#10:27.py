

def replace(letter, newletter):
    string = open("Strings_lists_tuples_LukeChase.txt", 'r')
    string = string.read()
    string = str(string)

    string = string.replace(letter, newletter)
    print(string)
    
##    current = 0
##    while string[current] != letter:
##        current += 1
##        if string[current] == letter:
##            string[current] = newletter
##            current += 1

replace("a", "e")
