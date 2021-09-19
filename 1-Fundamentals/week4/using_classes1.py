class Player:
    max_hp = 4000   # This is a class attribute.
    # A class attribute is attached to the class itself.
    # When we change the class attribute, it changes the classes that use it, even after the object was created.


# Object instantiation
player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)

# Class attributes
Player.max_hp = 5000
print(player1.max_hp)
print(player2.max_hp)

# Instance attributes and the constructor method
# These are stored per instance, rather than on the class
# When you change instance attributes,
# it does not affect the other instances.


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0


player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1:", player1.name, "-- HP:", player1.hp, "-- SCORE:", player1.score)
print("P2:", player2.name, "-- HP:", player2.hp, "-- SCORE:", player2.score)

player1.hp += 500
player1.score += 10
print("P1:", player1.name, "-- HP:", player1.hp, "-- SCORE:", player1.score)
print("P2:", player2.name, "-- HP:", player2.hp, "-- SCORE:", player2.score)
