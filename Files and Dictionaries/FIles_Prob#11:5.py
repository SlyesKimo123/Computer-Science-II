# Luke Chase --- 9/13
# Chap. 11 --- Files.  Problem 11.5
import turtle
file = open("mysterypicture.txt", "r")

t = turtle.Turtle()
screen = turtle.Screen()
for line in file:
    item = line.split()
    if item[0] == "UP":
        t.up()
    else:
        if item[0] == "DOWN":
            t.down()
        else:
            t.goto(int(item[0]), int(item[1]))

print(lines)
