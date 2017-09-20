# Luke Chase --- 9/13
# Chap. 11 --- Files.  Problem 11.2
file = open("studenttestscores.txt", "r")

counter = 0
adding = 0
for line in file:
    item = line.split()

    for i in item[1:]:
        counter += 1
        adding += int(i)
    avg = adding / counter
    print(item[0] ,"average = ", avg)

