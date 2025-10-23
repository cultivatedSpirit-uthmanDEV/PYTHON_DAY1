"""
class Enemy:
  life = 3

  def attack(self):
    print("ounch!")
    self.life -= 1


enemy1 = Enemy()

enemy1.attack()
"""



class Enemies:
  lifes = 3

  def attacks(selves):
    print("ounchs!")
    selves.lifes -= 1

  def checkLifes(selves):
    if selves.lifes <= 0:
      print("I am dead")
    else:
      print(str(selves.lifes) + "life left")


enemyy = Enemies()
enemyy1 = Enemies()


enemyy.attacks()
enemyy.attacks()
enemyy.checkLifes()

enemyy1.attacks()
enemyy1.checkLifes()