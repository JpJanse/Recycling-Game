#Recycling Game By JP

from tkinter import messagebox
import time
import sys
import math
import turtle
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Trash Hunter")
wn.setup(700,700)


#Create Pen
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("black")
    self.penup()
    self.speed(0)

class Muro(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(color_1)
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

    def change_color(self):
         self.color(color_2)

    def change_color_again(self):
        self.color(color_1)

color_1 = ("black")
color_2 = ("gold")
    
#create player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
        
    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_close_to(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 125:
            return True
        else:
            return False

    def is_far_away_from(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance > 125:
            return True
        else:
            return False

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

#Create Treasure
class Treasure(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape("circle")
    self.color("green")
    self.penup()
    self.speed(0)
    self.gold = 150
    self.goto(x, y)

  def destroy(self):
    self.goto(2000, 2000)
    self.hideturtle()

#create Gate
class Gate(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("lightgrey")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
 
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("lightgrey")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
 
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

class Door2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
 
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()

#Create Enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0


        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.xcor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"    
           

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])   

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt(( a ** 2) + ( b ** 2 ))

        if distance < 50:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle() 

#Create Player 2
class Player2(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("red")
    self.penup()
    self.speed(0)
    self.gold = 0

  def go_up(self):
    #Calculate the spot to move to
    move_to_x = self.xcor()
    move_to_y = self.ycor() + 24

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)

  def go_down(self):
    #Calculate the spot to move to
    move_to_x = self.xcor()
    move_to_y = self.ycor() - 24

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


  def go_left(self):
    #Calculate the spot to move to
    move_to_x = self.xcor() - 24
    move_to_y = self.ycor()

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


  def go_right(self):
    #Calculate the spot to move to
    move_to_x = self.xcor() + 24
    move_to_y = self.ycor()

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)

  def is_collision(self, other):
    a = self.xcor()-other.xcor()
    b = self.ycor()-other.ycor()
    distance = math.sqrt((a ** 2) + (b ** 2) )

    if distance < 5:
      return True
    else:
      return False

#Create levels list
levels = [""]

#Define first level
level_1 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "XMMMMXXXXMMMMMMMMMMMMXXXX",
  "XM PMMMMMM         EMXXXX",
  "XM      MM  MMMMMM  MMMXX",
  "XM      MM  MMM        MX",
  "XMMMMM  MM  MMM        MX",
  "XXXXXM  MM  MMMMMM  MMMXX",
  "XMMMMM  MM    MXXM  MXXXX",
  "XM EMM        MXXMTGMXXXX",
  "XM  MM  MMMMMMMXXMMMMXXXX",
  "XM        MMMMMMMXXXXXXXX",
  "XMT              MXXMMMMX",
  "XMMMMMMMMMMM     MXXM EMX",
  "XXMMMMXXXXXMMMM EMMMM  MX",
  "XXM  MMMMMMMMMM        MX",
  "XXM                   TMX",
  "XXM        MMMMMMMMMMMMMX",
  "XXMMMMMMM  MMMMMMMMMMMMMX",
  "XMMMMXXXM              MX",
  "XMT MXXXM              MX",
  "XM  MMMMMMMMMMMMMM EMMMMX",
  "XM        MMMM         MX",
  "XM                     MX",
  "XMMMMMMMMMMMMMMMMMMMMMMMX",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define second level
level_2 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "XMMMMXXXXMMMMMMMMMMMMXXXX",
  "XMLTMMMMMM         EMXXXX",
  "XM      MM  MM   M  MMMMX",
  "XM      MM EMM   M     MX",
  "XMMMMM  MMMMMMMMMM  MT MX",
  "XMMMMM  MM  MMMMXM  MMMMX",
  "XMD MM  MM    MXXM     MX",
  "XME MM        MXXM     MX",
  "XM  MM  MMMMMMMXXMMMM  MX",
  "XM        MMMMMMMMM    MX",
  "XM               MM    MX",
  "XMMMMMMMMMMM     MMMM EMX",
  "XXMMMMXXXXXMMMM EMMMM  MX",
  "XXMT MMMMMXXXXM        MX",
  "XXM      MMMXXM        MX",
  "XXM        MXXMM  MMMMMMX",
  "XXM  MMMM  MMMMM  MMMMMMX",
  "XMM  MXXM              MX",
  "XMP  MXXM              MX",
  "XM   MMMMMMMMMMMMM EMMMMX",
  "XM        EMMMM     MMMMX",
  "XME                   TMX",
  "XMMMMMMMMMMMMMMMMMMMMMMMX",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define third level
level_3 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "XP XX     XXT           X",
  "X  XX  XXXXXXXX  XX     X",
  "X  XX  XX    XXFEXXXX   X",
  "X            XXXXXXT    X",
  "X  XXXXXXXX    XXXXXX   X",
  "X     XX       XX       X",
  "XXX  XXXXXX  XXXX   XXXXX",
  "X    XX        XX       X",
  "X  XXXXXX  XX  XXXXXX   X",
  "X  XX      XX  XX       X",
  "X  XXXX  XXXXXXXX   XXXXX",
  "X   EXX        XX      EX",
  "XXXXXXXXXXXXX  XXXXXX   X",
  "X              XX       X",
  "X  XXXXXXXXXX  XX   XXXXX",
  "X     XX       XX       X",
  "X  XXXXXXXXXX  XXXXXX   X",
  "X  XX   LXX    XX       X",
  "X  XX  XXXXXX  XX   XXXXX",
  "X      XXTE    XX       X",
  "X  XXXXXXXXXXXXXX TXX   X",
  "X    XX        XXXXXX   X",
  "X        XXXX           X",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define Fourth level
level_4 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "X           P           X",
  "XXXX XX           XX XXXX",
  "X      X         X      X",
  "XE      X       X      EX",
  "XTT      X     X      TTX",
  "XE        X   X        EX",
  "X          X X          X",
  "XXXXXXXXXXXX XXXXXXXXXXXX",
  "X   TT    EX XE    TT   X",
  "X   TT    EX XE    TT   X",
  "X XXXXXXXXXXTXXXXXXXXXX X",
  "X   TT    EX XE    TT   X",
  "X   TT    EX XE    TT   X",
  "X XXXXXXXXXX XXXXXXXXXX X",
  "X          X X          X",
  "XE        X   X        EX",
  "XTT      X     X      TTX",
  "XE      X       X      EX",
  "X      X         X      X",
  "X     X           X     X",
  "XXX XX             XX XXX",
  "X                       X",
  "X           L           X",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add muros to list
muros = []

#Add a treasure to list
treasures = []

#Add a enemy to list
enemys = []

#Add Gate to List
gates = []

#Add A Second Gate to List
second_gates = []

#Add A Second Gate to List
third_gates = []


#Add maze to maze list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)

#Create level setup function
def setup_maze(level):
  global player
  global player2
  global walls
  global muros
  global enemys
  player = Player()
  player2 = Player2()

  #Keyboard binding
  turtle.listen()
  turtle.onkey(player.go_left,"a")
  turtle.onkey(player.go_right,"d")
  turtle.onkey(player.go_up,"w")
  turtle.onkey(player.go_down,"s")
    
  #Keyboard binding
  turtle.listen()
  turtle.onkey(player2.go_left,"Left")
  turtle.onkey(player2.go_right,"Right")
  turtle.onkey(player2.go_up,"Up")
  turtle.onkey(player2.go_down,"Down")

  muros = []
  walls = []
  enemys = []

  for y in range(len(level)):
    for x in range(len(level[y])):
      #Get the character at each x,y coordinates
      #NOTE the order of y and x in the next line
      character = level[y] [x]
      #Calculate the screen x, y coordinates
      screen_x = -288 + (x * 24)
      screen_y = 288 - (y *24)

      #Cheak if it is an X (representing a wall)
      if character == "X":
        pen.goto(screen_x, screen_y)
        pen.stamp()
        #Add coordinantes to wall list
        walls.append((screen_x, screen_y))
      
      #Cheak if it is a P (representing the player)
      if character == "P":
        player.goto(screen_x, screen_y)

      #Cheak if it is a M (representing the muro)
      if character == "M":
        muros.append(Muro(screen_x, screen_y))

        walls.append((screen_x, screen_y))

      #Cheak if it is a P (representing the player2)
      if character == "L":
        player2.goto(screen_x, screen_y)
      
      #Check if it is a T (representing Treasure)
      if character == "T":
        treasures.append(Treasure(screen_x, screen_y))

      #Cheak if it is a E (representing Enemy)
      if character == "E":
        enemys.append(Enemy(screen_x, screen_y))

      #Check if it is G representing gate
      if character == "G":
        gates.append(Gate(screen_x, screen_y))
        
      #Check if it is D representing secound gate
      if character == "D":
        second_gates.append(Door(screen_x, screen_y))

      if character == "F":
        third_gates.append(Door2(screen_x, screen_y))
   

#Create class instance
pen = Pen()
player = Player()

#Create class instance
pen = Pen()
player2 = Player2()

#create wall coorinate list
walls = []

#Set up level
setup_maze(levels[1])

#Keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"a")
turtle.onkey(player.go_right,"d")
turtle.onkey(player.go_up,"w")
turtle.onkey(player.go_down,"s")

#Keyboard binding
turtle.listen()
turtle.onkey(player2.go_left,"Left")
turtle.onkey(player2.go_right,"Right")
turtle.onkey(player2.go_up,"Up")
turtle.onkey(player2.go_down,"Down")

#Turn off screen updates
wn.tracer(0)

for enemy in enemys:
    turtle.ontimer(enemy.move, t=250)

for enemy in enemys:
         if player.is_collision(enemy):
             print ("You Died!")

#Main Game Loop
while True:

  #Check if player is close to muros
  for muro in muros:
    if player.is_close_to(muro):
        muro.change_color()
        
    if player.is_far_away_from(muro):
        muro.change_color_again()
  
  #Check for player collision with treasure
  #Iterate through treasure list
  for treasure in treasures:
    if player.is_collision(treasure):
      #Add the treasure gold to the player gold
      player.gold += treasure.gold
      print("Player Gold: {}".format(player.gold))
      #destroy the treasure
      treasure.destroy()
      #Remove the treasure from the treasures list
      treasures.remove(treasure)
      #Checks if player gold is same as 400
      if player.gold > 400:
        #Displays Win screen
        print("*" * 49)
        print("*" * 49)
        print("*" * 20, "YOU WIN", "*" * 20)
        print("*" * 49)
        print("*" * 49)
        time.sleep(5)
        
         
    if player2.is_collision(treasure):
      #Add the treasure gold to the player gold
      player2.gold += treasure.gold
      print("Player2 Gold: {}".format(player2.gold))
      #destroy the treasure
      treasure.destroy()
      #Remove the treasure from the treasures list
      treasures.remove(treasure)
      #Checks if player gold is same as 400
      if player2.gold > 400:
        #Displays Win screen
        print("*" * 49)
        print("*" * 49)
        print("*" * 20, "YOU WIN", "*" * 20)
        print("*" * 49)
        print("*" * 49)
        time.sleep(5)
        
      
  #Check for player collision with enemy
  #Iterate through enemy list
  for enemy in enemys:
    if player.is_collision(enemy):
      #Remove the treasure gold from the player
      player.gold -= enemy.gold
      print("Player Gold: {}".format(player.gold))
      #destroy enemy
      enemy.destroy()
      #remove the enemy from the enemy list
      enemys.remove(enemy)


  #Check for player collision with enemy
  #Iterate through enemy list
  for enemy in enemys:
    if player2.is_collision(enemy):
      #Remove the treasure gold from the player
      player2.gold -= enemy.gold
      print("Player2 Gold: {}".format(player2.gold))
      #destroy enemy
      enemy.destroy()
      #remove the enemy from the enemy list
      enemys.remove(enemy)

  #Check for player collision with player2
  if player.distance(player2) < 5:
    #Remove the treasure gold from the player
    player.gold -= 75
    print("Player Gold: {}".format(player.gold))
    if player.gold > -399:
      #Displays Lose screen
      print("*" * 48)
      print("*" * 48)
      print("*" * 19, "YOU LOSE", "*" * 19)
      print("*" * 48)        
      print("*" * 48)
      time.sleep(5)
      sys.exit("Good Bye!")
      
    #Remove the treasure gold from the player
    player2.gold -= 75
    print("Player2 Gold: {}".format(player.gold))
    if player2.gold > -399:
      #Displays Lose screen
      print("*" * 48)
      print("*" * 48)
      print("*" * 19, "YOU LOSE", "*" * 19)
      print("*" * 48)        
      print("*" * 48)
      time.sleep(5)
      sys.exit("Good Bye!")

    #Remove the treasure gold from the player
    player.gold -= 75
    print("Player Gold: {}".format(player.gold))
    if player.gold > -399:
      #Displays Lose screen
      print("*" * 48)
      print("*" * 48)
      print("*" * 19, "YOU LOSE", "*" * 19)
      print("*" * 48)        
      print("*" * 48)
      time.sleep(5)
      sys.exit("Good Bye!")
      

  #Check for player collision with gate
  #Iterate through gate list
  for gate in gates:
    if player.is_collision(gate):
      messagebox.showinfo("You Have Reached Gate!", "Good Job On Getting To Level 2!")
      wn.clear()
      wn.bgcolor("black")
      enemys.clear()
      treasures.clear()
      setup_maze(levels[2])

  #Check for player collision with door
  #Iterate through second_door list
  for door in second_gates:
    if player.is_collision(door):
      messagebox.showinfo("You Have Reached Door!", "Be Careful, This Level Has Some Spikey Walls")
      print("E")
      wn.clear()
      wn.bgcolor("black")
      enemys.clear()
      treasures.clear()
      setup_maze(levels[3])

  #Check for player collision with door
  #Iterate through third_door list
  for door in third_gates:
    if player.is_collision(door):
      messagebox.showinfo("You Have Reached Door!", "Be Careful, This Level Has Some Spikey Walls")
      print("E")
      wn.clear()
      wn.bgcolor("black")
      enemys.clear()
      treasures.clear()
      setup_maze(levels[4])

        
  #Update screen
  wn.update()