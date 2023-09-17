class player:
  def pay(self):
    print("The player is playing cricket.")
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")
#create objects of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()
#call the play() method for each object
bastman.play()
bowler.play()
