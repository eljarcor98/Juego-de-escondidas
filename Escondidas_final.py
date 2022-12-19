import turtle
import random


puntaje = 0
mayor_puntaje = 0 


wn = turtle.Screen()
wn.bgcolor("black")  
wn.title("Maze Game")
wn.setup(1000,900)
wn.tracer(0)



class Marcador(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,320)
        self.write('puntaje:0          mayor puntaje: 0', align=('center'), font = ('Courier', 15, 'normal'))

class Objeto(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('triangle')
        self.color('red')
        self.penup()
        self.speed(0)



class Muros(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 0
 
class Jugador(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

    def arriba(self):
        x = jugador.xcor()
        y = jugador.ycor() +24

        if(x, y) not in paredes:
            self.goto(self.xcor(),      self.ycor() + 24)

    def abajo(self):
        x = jugador.xcor()
        y = jugador.ycor() -24
        
        if(x, y) not in paredes:
            self.goto(self.xcor(),      self.ycor() - 24)

    def izquierda(self):
        x = jugador.xcor() -24
        y = jugador.ycor()

        if(x, y) not in paredes:
            self.goto(self.xcor() -24,   self.ycor())

    def derecha(self):
        x = jugador.xcor() +24
        y = jugador.ycor()

        if(x, y) not in paredes:
            self.goto(self.xcor() +24,   self.ycor())


#create level list
niveles = [""]

nivel_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX       XXXXXX              X XXXXX     XXX",
"X           XXXXXX  XXX  XXXXXXXXXXX    XX    XXXXXX",
"X  XXXXXXX          XX  XXXXXXX  X   XXXXX X      XX",
"X  XXXXXXXXXXXXXXX        XXXXX XX      XX  XXXXXXXX",
"X  XXXXXXXXXXXXXXXXXXXXXXXXXXXX XXXX XXXXX  XX    XX",
"X                      XXXXXXX  XXXX    XX      XXXX",
"XXXXXXX  XXXXXXXXXXXX   XXXXX        XX  X XXX   XXX",
"XXXXXX   XXXXXXXXXXXXX    XXXXXXXXX  XX    X   XXXXX",
"XXX              XXXX  X   XX   XX      XXXXX   XXXX",
"XXXXXX   XXXXXXXXXXXXX XX  XXXX    XXXXXXXXXXXX    X",
"XXXXXX   XXXXXXXXXXXXX XX     XXX   XXXXXXXXXXX  XXX",
"X                    O XXXXX   XXXX    XXXXX      XX",
"XXXXX    XXXXXXXXXX    XXXXXXXXXX   XXXXXXXXXXXXXXXX",
"X            XXXXXXX                      XXXXXXXXXX",
"XXXXXX   XXXXXXXXXXX XXXXXXXXXXXX   XXXXXX    XXXXXX",
"X                      XXXXXXXX        XXX   XXXXXXX",
"XXXXXX   XXXX   XXXXXXXXXXXXXXXX    X      X      XX",
"XXXXXX   XXXX   XXXXXXXXXXXX  XXXX      XXXXX  XXXXX",
"XXXXX    XXXX          XX           XX  XX       XXX",
"X               X      XXX   XXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXX   XXXXXXX  XXXXX      XXXXXXX      XXXXXXXXX",
"XXXXXX   XXXXXXXX  XXXXXX        XXXXXXXXX         X",
"XXXXXXXX           XXXXXXXXXXX                     X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

niveles.append (nivel_1)

def mapa(nivel):
 
    for y in range(len(nivel)):
        for x in range(len(nivel[y])):
 
            personaje = nivel[y][x]

            pantalla_x = -620 + (x * 24)
            pantalla_y =  290 - (y * 24)
 
            if personaje == "X":
                muros.goto(pantalla_x, pantalla_y)
                muros.stamp()
                paredes.append((pantalla_x,pantalla_y))

            if personaje == "P":
                jugador.goto(pantalla_x, pantalla_y)
            
            if personaje == 'O' and personaje != 'X':
                objeto.goto(pantalla_x, pantalla_y)

paredes = []

#class instances
muros = Muros()
jugador = Jugador()
objeto = Objeto()
objeto1 = Objeto()
marcador = Marcador()


mapa(niveles[1])
#print(walls)

turtle.listen()
turtle.onkey(jugador.izquierda, 'Left')      ##entrada de teclado flecha izquierda
turtle.onkey(jugador.derecha, 'Right')       ##entrada de teclado flecha derecha
turtle.onkey(jugador.arriba, 'Up')           ##entrada de teclado flecha arriba
turtle.onkey(jugador.abajo, 'Down')          ##entrada de teclado flecha abajo

wn.tracer(0)




#main game loop
while True:

    escondido  = random.randint(0, 1)
    escondido2 = random.randint(0, 1)
    if jugador.distance(objeto) < 60:
        pantalla_x =  random.randint(-450, 450)
        pantalla_y =  random.randint(-290, 290)
        objeto.goto(pantalla_x, pantalla_y)
        if escondido == 1:
            puntaje += 10
        else: 
            puntaje -= 5
    if jugador.distance(objeto1) < 60:
        pantalla_x1 =  random.randint(-450, 450)
        pantalla_y1 =  random.randint(-290, 290)
        objeto1.goto(pantalla_x1, pantalla_y1)
        if escondido2 == 1:
            puntaje += 10
        else:
            puntaje -=5
        #puntaje
        
    if puntaje > mayor_puntaje:
        mayor_puntaje = puntaje

    marcador.clear() 
    marcador.write('puntaje:{}          mayor puntaje: {}'.format(puntaje, mayor_puntaje), align=('center'), font = ('Courier', 15, 'normal'))
    # PANTALLA FINAL

    if puntaje >=30:
        muros.clear()
        marcador.clear()
        jugador.clear()
        objeto1.clear()
        objeto.clear()
        
        muros.goto(0,0)
        muros.write('GAME OVER!', align='center', font=('Arial',100,'normal'))
        wn.update()

    wn.update()