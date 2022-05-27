#Recycling Game By JP

from tkinter import messagebox
import os
import time
import sys
import math
import turtle


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
    self.gold = 100
    self.goto(x, y)

  def destroy(self):
    self.goto(2000, 2000)
    self.hideturtle()

#create Gate
class Gate(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Exit_Door.gif")
        self.color("pink")
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
    self.gold = 50
    self.goto(x, y)

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
    self.gold = 75

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
  "X EXXX        XXXXT XXXXX",
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
  "XXTGXXXXX               X",
  "XX  XXXXXXXXXXXXXX EXXXXX",
  "XX   YXXXXXXXXXXXX  XXXXX",
  "XX          XXXX        X",
  "XXXX                   LX",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Define second level
level_2 = [
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "XL XXXXXXXE         XXXXX",
  "XT XXXXXXX  XX   X EXXXXX",
  "X       XX  XX   X  XXXXX",
  "X       XXXXXX   X     XX",
  "XXXXXX  XXXXXXXXXX  XT XX",
  "XXXXXX  XX  XXXXXX  XXXXX",
  "X  XXX  XX    XXXX      X",
  "X EXXX        XXXX      X",
  "X  XXX  XXXXXXXXXXXXXX  X",
  "X         XXXXXXXXX     X",
  "X                XXXXX  X",
  "XXXXXXXXXXXX     XXXXX EX",
  "XXXXXXXXXXXXXXX EXXXXX  X",
  "XXXT XXXXXXXXXX         X",
  "XXX      XXXXXX         X",
  "XXX        XXXXX  XXXXXXX",
  "XXX  XXXX  XXXXX  XXXXXXX",
  "XXX  XXXX               X",
  "XXP  XXXX               X",
  "XX   XXXXXXXXXXXXX EXXXXX",
  "XX   YXXXXXXXXXXXX  XXXXX",
  "XXE         XXXX        X",
  "XXXX                   TX",
  "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add a treasure to list
treasures = []

#Add a enemy to list
enemys = []

#Add Gate to List
gates = []

#Add maze to maze list
levels.append(level_1)
levels.append(level_2)

#Create level setup function
def setup_maze(level):
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
setup_maze(levels[2])

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
      if player.gold >= 400:
        #Displays Win screen
        print("*" * 49)
        print("*" * 49)
        print("*" * 20, "YOU WIN", "*" * 20)
        print("*" * 49)
        print("*" * 49)
        time.sleep(5)
        os.system("clear")

    for gate in gates:
      if player.is_collision(gate):
        messagebox.showinfo("Congratulations", "You reached the first gate")
      pen.clear()

      if maze == ("level1"):
          setup_maze(levels[2])
          maze = ("level2")
      else:
          turtle.bye()

              
    if player2.is_collision(treasure):
      #Add the treasure gold to the player gold
      player2.gold += treasure.gold
      print("Player2 Gold: {}".format(player2.gold))
      #destroy the treasure
      treasure.destroy()
      #Remove the treasure from the treasures list
      treasures.remove(treasure)
      
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
    player.gold -= player2.gold
    print("Player Gold: {}".format(player.gold))
    if player.gold >= -400:
      #Displays Lose screen
      print("*" * 48)
      print("*" * 48)
      print("*" * 19, "YOU LOSE", "*" * 19)
      print("*" * 48)        
      print("*" * 48)
      time.sleep(5)
      os.system("clear")
      sys.exit("Thank You For Playing!")


    
  #Update screen
  wn.update()
