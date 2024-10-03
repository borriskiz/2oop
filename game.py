class Entity:
    name = "blank"
    health = 0
    damage = 0
    armor = 0

    def __init__(self, name:str, health:int, damage:int, armor:int):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, opponent_armor:int):
        effective_damage = max(0, self.damage - opponent_armor)
        return effective_damage

    def attack(self, opponent: 'Entity'):
        damage_dealt = self._calculate_damage(opponent.get_armor())
        opponent.sub_health(damage_dealt)
        print(f"{self.name} deals {damage_dealt} damage to the {opponent.get_name()}.")
        print(f"{opponent.name}'s health is now {opponent.get_health()}.")

    def sub_health(self, damage:int):
        self.health = max(0, self.health - damage)

    def get_health(self) -> int:
        return self.health
    
    def get_armor(self) -> int:
        return self.armor
    
    def get_name(self) -> str:
        return self.name


class Player(Entity):
    mana = 0
    def __init__(self, name:str, health:int, damage:int, armor:int, mana:int):
        super().__init__(name, health, damage, armor)
        self.mana = mana

    def _calculate_damage(self, opponent_armor:int):
        effective_damage = max(0, self.damage * self.mana- opponent_armor)
        return effective_damage

class Enemy(Entity):
    def __init__(self, name:str, health:int, damage:int, armor:int):
        super().__init__(name, health, damage, armor)