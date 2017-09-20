# Luke Chase --- 9/13
# Chap. 11 --- Files.  Problem 11.3
file = open("studenttestscores.txt", "r")

for line in file:
    item = line.split()
    print(item[0], "had a maximum of ", max(item[1:]), "and a minimum of ", min(item[1:]))
