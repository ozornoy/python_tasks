class Player:
    def __init__(self, nickname="Unknow nickname", level=1, score=0):
        self.nickname = nickname
        self.level = level
        self.score = score

    def levelUp(self):
        self.level += 1

    def addScore(self, points):
        self.score += points

    def printPlayerInfo(self):
        print(f"Игрок: {self.nickname}, Уровень: {self.level}, Очки: {self.score}")


player = Player("Mega Player")
player.levelUp()
player.levelUp()
player.addScore(2)
player.printPlayerInfo()
