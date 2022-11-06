import turtle as trtl
import random as rand
import lb


def start_game():
  global player_name
  player_name = input("What is your name?")
  games = input("Do you want to start the game?(yes/no)")

  if games == "no":
    exit()


start_game()

colors = [
  "blue",
  "red",
  "yellow",
  "red",
  "green",
  "purple",
  "white",
]

spot = trtl.Turtle()
size = 10
spot.shapesize(size)
spot.shape("turtle")
spot.speed(5)

font_setup = ("Arial", 20)
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-250, 175)
score_writer.pendown()
score_writer.hideturtle()
score = 0


def sw():
  if timer_up == False:
    score_writer.clear()
    score_writer.write(f"Score = {str(score)}", font=font_setup)


def spot_clicked(x, y):
  global size
  size = size * 0.92
  spot.shapesize(size)
  spot.fillcolor(colors[rand.randint(0, 6)])
  spot.penup()
  spot.goto(rand.randint(-150, 150), rand.randint(-150, 150))
  global score
  score += 1
  sw()


spot.onclick(spot_clicked)

font_setup = ("Arial", 20, "normal")

timer = 5
counter_interval = 1000  #1000 represents 1 second
timer_up = False

counter = trtl.Turtle()
counter.penup()

counter.goto(115, 175)
counter.hideturtle()
ldt = trtl.Turtle()


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    spot.hideturtle()
    lb.sortLeaderBoard(player_name, score)
    lb.drawLeaderBoard(ldt, lb.getLeaderBoard())
  if timer_up:
    score_writer.clear()
    score_writer.write("You lost", font=font_setup)
    spot.fillcolor("white")
    spot.color("white")
    global rcolor
    rcolor = False
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.ontimer(sw)
wn.bgcolor("gray")
wn.mainloop()
