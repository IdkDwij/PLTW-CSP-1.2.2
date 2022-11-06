import json

b_s = 15
s_s = 20
g_s = 25


#return the leaderboard dict
def getLeaderBoard():
  with open('plist.json', 'r') as f:
    myDict = json.loads(f.read())
  return myDict


'''def setLeaderBoard(name, score):
  myDict = getLeaderBoard()
  y, z, index, g, h = 1, 100, 0, 0, 0
  for x in myDict["score"]:
    if y < x:
      y = x
    if z > x:
      z = x
      g = index
    index += 1
  print(myDict)
  for x in myDict["score"]:
    if x < score:
      del myDict["name"][g]
      del myDict["score"][g]
      myDict["name"].append(name)
      myDict["score"].append(score)

  with open('plist.json', 'w') as f:
    f.write(json.dumps(myDict, indent=4))'''


def sortLeaderBoard(name, score):
  myDict = getLeaderBoard()
  index = 0
  for x in myDict["score"]:
    if x < score:
      del myDict["name"][index]
      del myDict["score"][index]
      myDict["name"].insert(index, name)
      myDict["score"].insert(index, score)
      with open('plist.json', 'w') as f:
        f.write(json.dumps(myDict, indent=4))
        break
    index += 1


def drawLeaderBoard(lb_text, scoreDict):
  font_setup = ("Arial", 20, "normal")
  lb_text.clear()
  lb_text.penup()
  lb_text.goto(-160, -50)
  lb_text.hideturtle()
  lb_text.down()
  index = 0
  lbstr = ""
  for x in scoreDict["score"]:
    lbstr += scoreDict["name"][index] + ": " + str(
      scoreDict["score"][index]) + "\n"
    index += 1
  lb_text.write(lbstr, font=font_setup)
