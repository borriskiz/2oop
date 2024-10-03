class Toy:
    name = "blank"
    color = "blank"
    type = "blank"

    def __init__(self, name: str, color: str, type: str) -> None:
        self.name = name
        self.color = color
        self.type = type

    def read_label(self) -> None:
        print(
            f"This is a {self.type}, made in color of {self.color}, it's name is {self.name}"
        )

    def play(self) -> None:
        return


class TeddyBear(Toy):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, color, "TeddyBear")

    def play(self) -> None:
        print(f"{self.name} makes a 'rawr' sounds")


class Cheburashka(Toy):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, color, "Cheburashka")

    def play(self) -> None:
        print(f"{self.name} sings a cool song")


class Engine:
    def start(self) -> None:
        print(f"WrOoM wRoOm WrOoOoOoOoM")


class Chainsaw(Toy, Engine):
    def __init__(self, name: str, color: str) -> None:
        super().__init__(name, color, "Chainsaw")
    def play(self) -> None:
        print(f"{self.name} starts int's engine")
        Engine().start()


class ToyFactory:
    def makeToy(self, name: str, color: str, type: str):
        if type == "TeddyBear":
            toy = TeddyBear(name, color)
        elif type == "Cheburashka":
            toy = Cheburashka(name, color)
        elif type == "Chainsaw":
            toy = Chainsaw(name, color)
        else:
            print(f"We don't know {type} type of toys.")
            print(f"MAKES CHEBURASHKA")
            toy = Cheburashka(name, color)

        self.buyMaterials()
        self.sewing()
        self.coloring()
        return toy

    def buyMaterials(self):
        print("Buying materials.")

    def sewing(self):
        print("Sewing of a toy.")

    def coloring(self):
        print("Coloring of a toy.")