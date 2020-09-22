class SoccerPlayer:

    def __init__(self, health, salary):

        self.health = health
        self.salary = salary

    def foul(self, player):

        player.health = 0
        self.salary = self.salary + 10**6

ronaldo = SoccerPlayer(100, 10**7)
beckham = SoccerPlayer(100, 10**6)

ronaldo.foul(beckham)

print(beckham.health)
print(ronaldo.health)

print(beckham.salary)
print(ronaldo.salary)