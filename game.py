class Entity:
    name = "blank"
    health = 0
    damage = 0
    armor = 0
    mana = 0

    def __init__(self, name, health, damage, armor, mana):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.mana = mana

    def _calculate_damage(self, opponent_armor):
        effective_damage = max(0, self.damage * self.mana - opponent_armor)
        return effective_damage

    def attack(self, opponent):
        damage_dealt = self._calculate_damage(opponent.armor)
        opponent.health -= damage_dealt
        print(f"{self.name} deals {damage_dealt} damage to the {opponent.name}.")
        print(f"{opponent.name}'s health is now {opponent.health}.")


class Player(Entity):
    def __init__(self, name, health, damage, armor, mana):
        super().__init__(name, health, damage, armor, mana)


class Enemy(Entity):
    def __init__(self, name, health, damage, armor, mana):
        super().__init__(name, health, damage, armor, mana)