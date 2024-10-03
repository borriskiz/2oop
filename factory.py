class Toy:
    name = "blank"
    color = "blank"
    type = "blank"

    def __init__(self, name, color, type) -> None:
        self.name = name
        self.color = color
        self.type = type

    def read_label(self) -> None:
        print(f"This is a {self.type}, made in color of {self.color}, it's name is {self.name}")

class TeddyBear(Toy):
    def __init__(self, name, color) -> None:
        super().__init__(name, color, "TeddyBear")


class Cheburashka(Toy):
    def __init__(self, name, color) -> None:
        super().__init__(name, color, "Cheburashka")


class Chainsaw(Toy):
    def __init__(self, name, color) -> None:
        super().__init__(name, color, "Chainsaw")

class ToyFactory():
     def makeToy(self, name, color, type):
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