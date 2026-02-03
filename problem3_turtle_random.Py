import turtle
import random

def dessiner_carre(t, taille):
    for _ in range(4):
        t.forward(taille)
        t.right(90)

def dessiner_triangle(t, taille):
    for _ in range(3):
        t.forward(taille)
        t.left(120)

def dessiner_cercle(t, taille):
    t.circle(taille)

N = int(input("Entrez un nombre entre 0 et 9 : "))

screen = turtle.Screen()
screen.colormode(255)

t = turtle.Turtle()
t.speed(0)

for _ in range(N):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.penup()
    t.goto(x, y)
    t.pendown()

    couleur = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    t.color(couleur)

    taille = random.randint(20, 100)

    forme = random.choice(["carre", "triangle", "cercle"])
    if forme == "carre":
        dessiner_carre(t, taille)
    elif forme == "triangle":
        dessiner_triangle(t, taille)
    else:
        dessiner_cercle(t, taille)

turtle.done()