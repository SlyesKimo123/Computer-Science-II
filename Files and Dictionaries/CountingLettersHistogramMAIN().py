import turtle

def main():

    t = turtle.Turtle()
    t.speed(0)
    wn = turtle.Screen()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    d = {}

    for letter in alphabet:
        d[letter] = 0
    def countAll(text):
        for letter in text:
            d[letter] = text.count(letter)
        return d
        return user_input

    d = countAll(input("Write a random word (no caps pls)\n"))
    print(d)

    def create():
        t.penup()
        t.goto(-200, -200)
        t.pendown()
        #t.right(90)
        for letter in alphabet:
            t.left(90)
            t.fd(20 * d[letter])
            t.right(90)
            t.fd(10)
            t.right(90)
            t.fd(20 * d[letter])
            t.left(90)


    def drawThangies():
        t.goto(-200, -200)
        t.pendown()
        #t.right(90)
        for i in range(26):
            t.left(90)
            t.fd(10)
            t.left(180)
            t.fd(10)
            t.left(90)
            t.fd(10)

    def writeLeets():
        t.goto(-200, -220)
        t.right(90)
        t.penup()
        t.fd(5)
        for letters in alphabet:
            t.write(letters)
            t.forward(10)


    def drawGraph():
        wn.setworldcoordinates(-500, -500, 500, 500)
        t.penup()
        t.goto(-200, -200)
        t.pendown()
        t.fd(300)
        t.fd(-300)
        t.left(90)
        t.fd(400)

    drawGraph()
    writeLeets()
    drawThangies()
    create()

main()
