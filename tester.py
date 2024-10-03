from Cars import PoliceCar, SportCar, TownCar, WorkCar
from game import Enemy, Player
import random


def first():
    town_car = TownCar(speed=120, color="red", name="Town Ace")
    sport_car = SportCar(speed=200, color="blue", name="Sporty McSport")
    work_car = WorkCar(speed=80, color="yellow", name="Worky Worker")
    police_car = PoliceCar(speed=150, color="black", name="Police Patrol")

    town_car.go()
    sport_car.turn(90)
    work_car.stop()
    police_car.go()
    police_car.turn(-90)
    police_car.doSignal()


def second():
    player = Player("Guybrush", 100, 20, 5, random.randint(1, 3))
    enemy = Enemy("Gobburin", 80, 15, 8, random.randint(1, 3))

    print("Battle begins!")
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            print(f"{enemy.name} defeated! {player.name} wins!")
            break

        enemy.attack(player)
        if player.health <= 0:
            print(f"{player.name} defeated! {enemy.name} wins!")
            break
