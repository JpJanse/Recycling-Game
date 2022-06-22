#Recycling Game By JP

from tkinter import messagebox
import os
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
    self.color("white")
    self.penup()
    self.speed(0)

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
    #Calculate the spot to move to
    move_to_x = player.xcor()
    move_to_y = player.ycor() + 24

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)

  def go_down(self):
    #Calculate the spot to move to
    move_to_x = player.xcor()
    move_to_y = player.ycor() - 24

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


  def go_left(self):
    #Calculate the spot to move to
    move_to_x = player.xcor() - 24
    move_to_y = player.ycor()

    
    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


  def go_right(self):
    #Calculate the spot to move to
    move_to_x = player.xcor() + 24
    move_to_y = player.ycor()

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
    self.shape("triangle")
    self.color("red")
    self.penup()
    self.speed(0)
    self.gold = 100
    self.goto(x, y)
    self.direction = random.choice(["up", "down", "left", "right",])

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

    #check if player is close
    #If so, go in that direction
    if self.is_close(player):
      if player.xcor() < self.xcor():
        self.direction = "left"
      elif player.xcor() > self.xcor():
        self.direction = "right"
      elif player.ycor() < self.ycor():
        self.direction = "down"
      elif player.ycor() > self.ycor():
        self.direction = "up"

    #claculate the spot to move to
    move_to_x = self.xcor() + dx
    move_to_y = self.ycor() + dy

    #check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    else:
      #choose a different direction
      self.direction = random.choice(["up", "down", "left", "right",])

    #set timer to move next time
    turtle.ontimer(self.move, t=random.radiant(100, 300))
  
  def is_close(self, other):
    a = self.xcor()-other.xcor()
    b = self.xcor()-other.xcor()
    distance = math.sqrt((a ** 2) + (b ** 2) )

    if distance < 75:
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
    move_to_x = player2.xcor()
    move_to_y = player2.ycor() + 24

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)

  def go_down(self):
    #Calculate the spot to move to
    move_to_x = player2.xcor()
    move_to_y = player2.ycor() - 24

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


  def go_left(self):
    #Calculate the spot to move to
    move_to_x = player2.xcor() - 24
    move_to_y = player2.ycor()

    #Check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


  def go_right(self):
    #Calculate the spot to move to
    move_to_x = player2.xcor() + 24
    move_to_y = player2.ycor()

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
  "XP XXXXXXX          XXXXX",
  "X  XXXXXXX  XXXXXX EXXXXX",
  "X       XX  XXXXXX  XXXXX",
  "X       XX  XXX        XX",
  "XXXXXX  XX  XXX        XX",
  "XXXXXX  XX  XXXXXX  XXXXX",
  "XXXXXX  XX    XXXX  XXXXX",
  "X EXXX        XXXXTGXXXXX",
  "X  XXX  XXXXXXXXXXXXXXXXX",
  "X         XXXXXXXXXXXXXXX",
  "XT               XXXXXXXX",
  "XXXXXXXXXXXX     XXXXX EX",
  "XXXXXXXXXXXXXXX EXXXXX  X",
  "XXX  XXXXXXXXXX         X",
  "XXX                    TX",
  "XXX        XXXXXXXXXXXXXX",
  "XXXXXXXXX  XXXXXXXXXXXXXX",
  "XXXXXXXXX               X",
  "XXT XXXXX               X",
  "XX  XXXXXXXXXXXXXX EXXXXX",
  "XX   YXXXXXXXXXXXX  XXXXX",
  "XX          XXXX        X",
  "XXXX                   LX",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define second level
level_2 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "XLTXXXXXXXE         XXXXX",
  "X  XXXXXXX  XX   X EXXXXX",
  "X       XX  XX   X  XXXXX",
  "X       XXXXXX   X     XX",
  "XXXXXX  XXXXXXXXXX  XT XX",
  "XXXXXX  XX  XXXXXX  XXXXX",
  "X DXXX  XX    XXXX      X",
  "X EXXX        XXXX      X",
  "X  XXX  XXXXXXXXXXXXXX  X",
  "X         XXXXXXXXX     X",
  "X                XX     X",
  "XXXXXXXXXXXX     XXXXX EX",
  "XXXXXXXXXXXXXXX EXXXXX  X",
  "XXXT XXXXXXXXXX         X",
  "XXX      XXXXXX         X",
  "XXX        XXXXX  XXXXXXX",
  "XXX  XXXX  XXXXX  XXXXXXX",
  "XXX  XXXX              EX",
  "XXP  XXXX               X",
  "XX   XXXXXXXXXXXXX EXXXXX",
  "XX   YXXXXXXXXXXXX  XXXXX",
  "XXE        EXXXX        X",
  "XXXX                   TX",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define third level
level_3 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "XP EE     EET           X",
  "X  EE  EEEEEEEE  EE     X",
  "X  EE  EE    EEF EEEE   X",
  "X            EEEEEET    X",
  "X  EEEEEEEE    EEEEEE   X",
  "X     EE       EE       X",
  "XEE  EEEEEE  EEEE   EEEEX",
  "X    EE        EE       X",
  "X  EEEEEE  EE  EEEEEE   X",
  "X  EE      EE  EE       X",
  "X  EEEE  EEEEEEEE   EEEEX",
  "X    EE        EE       X",
  "XEEEEEEEEEEEE  EEEEEE   X",
  "X              EE       X",
  "X  EEEEEEEEEE  EE   EEEEX",
  "X     EE       EE       X",
  "X  EEEEEEEEEE  EEEEEE   X",
  "X  EE   LEE    EE       X",
  "X  EE  EEEEEE  EE   EEEEX",
  "X      EET     EE       X",
  "X  EEEEEEEEEEEEEE TEE   X",
  "X    EE        EEEEEE   X",
  "X        EEEE           X",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define Fourth level
level_4 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "X           P           X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X         EE EE         X",
  "X         EE EE         X",
  "XEEEEEEEEEEETEEEEEEEEEEEX",
  "X         EE EE         X",
  "X         EE EE         X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X                       X",
  "X           L           X",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

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

  walls = []

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

#Main Game Loop
while True:
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