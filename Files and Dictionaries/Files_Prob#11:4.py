# Luke Chase --- 9/13
# Chap. 11 --- Files.  Problem 11.4
import turtle

file = open("labdata.txt", "r")


def plotRegression():
    def createGraph():
        global t
        t = turtle.Turtle()
        t.goto(-200, 0)
        t.fd(400)
        t.fd(-200)
        t.right(90)
        t.fd(200)
        t.right(180)
        t.fd(400)
    createGraph()
    for line in file:
        item = line.split()
        xcoord = item[0]
        xcoord = str(xcoord)
        xcoord = xcoord.replace('[', '')
        xcoord = xcoord.replace(']', '')
        xcoord = xcoord.replace("'", '')
        xcoord = int(xcoord)
        ycoord = item[1]
        ycoord = str(ycoord)
        ycoord = ycoord.replace('[', '')
        ycoord = ycoord.replace(']', '')
        ycoord = ycoord.replace("'", '')
        ycoord = int(ycoord)
#        rule1 = y = c+m(x-b) # c = mean of all y-values; b = mean of all x-values
        print(item, xcoord)
        t.penup()
        t.goto(xcoord, ycoord)
        t.pendown()
        t.fd(1)

plotRegression()
