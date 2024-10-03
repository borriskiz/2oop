class iCar:
    speed = 0
    color = "blank"
    name = "blank"
    is_police = False
    it_is_allright = True
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) -> bool:
        if self.it_is_allright:
            print(f"The {self.name} car is now moving.")
            return True
        else:
            print(f"The {self.name} car isn't moving.")
            return False

    def stop(self) -> bool:
        print(f"The {self.name} car has stopped.")
        return True

    def turn(self, direction) -> bool:
        if direction >= -360 and direction <= 360:
            print(f"The {self.name} car turned {direction}.")
            return True
        else:
            print(f"The {self.name} car can't move {direction}.")
            return False

class TownCar(iCar):
    def __init__(self, speed, color, name):
        iCar().__init__(speed, color, name)


class SportCar(iCar):
    def __init__(self, speed, color, name):
        iCar().__init__(speed, color, name)


class WorkCar(iCar):
    def __init__(self, speed, color, name):
        iCar().__init__(speed, color, name)


class PoliceCar(iCar):
    def __init__(self, speed, color, name):
        iCar().__init__(speed, color, name, is_police=True)

    def DoSignal(self):
        print(f"Beep!!!.")