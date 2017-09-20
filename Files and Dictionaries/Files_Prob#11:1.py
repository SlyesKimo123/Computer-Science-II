# Luke Chase --- 9/13
# Chap. 11 --- Files.  Problem 11.1
file = open("studenttestscores.txt", "r")
for aline in file:
    item = aline.split()
    if len(item[1:]) > 6:
        print(item[0])

