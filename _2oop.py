from Cars import PoliceCar, SportCar, TownCar, WorkCar

town_car = TownCar(speed=120, color='red', name='Town Ace')
sport_car = SportCar(speed=200, color='blue', name='Sporty McSport')
work_car = WorkCar(speed=80, color='yellow', name='Worky Worker')
police_car = PoliceCar(speed=150, color='black', name='Police Patrol')

town_car.go()
sport_car.turn(90)
work_car.stop()
police_car.go()
police_car.turn(-90)
police_car.doSignal()
