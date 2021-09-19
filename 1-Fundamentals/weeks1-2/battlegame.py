# Wizard
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150

# Elf
elf = "Elf"
elf_hp = 100
elf_damage = 100

# Human
human = "Human"
human_hp = 150
human_damage = 20

# Dragon
dragon_hp = 300
dragon_damage = 50

while True:
    print("1) " + wizard)
    print("2) " + elf)
    print("3) " + human)
    option = input("Choose your character: ")
    if option == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif option == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif option == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")

print("You have chosen the character: " + character)
print("Health: ", my_hp)
print("Damage: ", my_damage)
print("")

while True:

    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now:", dragon_hp)
    print("")
    print("The Dragon strikes back at", character)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    # Dragon's Turn
    my_hp = my_hp - dragon_damage
    print("The Dragon has damaged the " + character + "!")
    print("The " + character + "'s health is now: ", my_hp)
    print("")
    if my_hp <= 0:
        print("The", character, "has lost the battle! :(")
        break
