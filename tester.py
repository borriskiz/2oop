from cars import PoliceCar, SportCar, TownCar, WorkCar
from game import Enemy, Player
from factory import ToyFactory
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
    enemy = Enemy("Gobburin", 80, 25, 8)

    print("Battle begins!")
    while player.get_health() > 0 and enemy.get_health() > 0:
        player.attack(enemy)
        if enemy.get_health() <= 0:
            print(f"{enemy.get_name()} defeated! {player.get_name()} wins!")
            break

        enemy.attack(player)
        if player.get_health() <= 0:
            print(f"{player.get_name()} defeated! {enemy.get_name()} wins!")
            break

def third():
    factory = ToyFactory()
    toys = [ 
        factory.makeToy("Freddy Fazbear", "golden", "TeddyBear"),
        factory.makeToy("My best friend", "brown", "Cheburashka"),
        factory.makeToy("The great communicator", "red", "Chainsaw"),
        factory.makeToy("Huggy Waggy", "blue", "Huggy Waggy"),
    ]
    for toy in toys:
        toy.read_label()
        toy.play()