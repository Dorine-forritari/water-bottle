# Write a class called `PlayerCharacter`, whose constructor can take 2 parameters: max_hp (default 10) and level (default 1). 
# If the user enters in max hp less than 0, set it as 10
# if the user sets level less than 1, set it as 1.
# (hp means hitpoints or health points)

# The PlayerCharacter should have the following methods:
# __str__() : displays a string like this: "Player with {current hp} HP out of {max hp} HP at level {level}".
# take_damage(damage) : subtract damage from current hp of the player character.
# heal(heal_amount) : add heal_amount to the current health, if it surpasses max hp, set it as max hp.
# level_up() : level increments up by one, max hp increases by 3*level and current hp becomes equal to max hp
# is_dead() : returns true if current hp is less than 1.

# player = PlayerCharacter()
# print(player)
# player.take_damage(5)
# print(player)
# player.heal(3)
# print(player)
# player.level_up()
# print(player)
# player.take_damage(15)
# print(player.is_dead())
# player.take_damage(2)
# print(player)
# print(player.is_dead())
# player.heal(50)
# print(player)

# Player with 10 HP out of 10 HP at level 1
# Player with 5 HP out of 10 HP at level 1
# Player with 8 HP out of 10 HP at level 1
# Player with 16 HP out of 16 HP at level 2
# False
# Player with -1 HP out of 16 HP at level 2
# True
# Player with 16 HP out of 16 HP at level 2

class PlayerCharacter:
    def __init__(self, max_hp=10, level=1) -> None:
        if max_hp < 0:
            max_hp = 10
        if level < 1:
            level = 1
        self.max_hp = max_hp
        self.level = level
        self.current_hp = max_hp

    def __str__(self) -> str:
        return f"Player with {self.current_hp} HP out of {self.max_hp} HP at level {self.level}"

    def take_damage(self, damage):
        self.current_hp = self.current_hp - damage

    def heal(self, heal_amount):
        self.current_hp = self.current_hp + heal_amount
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def level_up(self):
        self.level += 1
        self.max_hp += self.level * 3
        self.current_hp = self.max_hp

    def is_dead(self):
        return self.current_hp < 1

player = PlayerCharacter()
print(player)
player.take_damage(5)
print(player)
player.heal(3)
print(player)
player.level_up()
print(player)
player.take_damage(15)
print(player.is_dead())
player.take_damage(2)
print(player)
print(player.is_dead())
player.heal(50)
print(player)