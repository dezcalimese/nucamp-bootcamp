import random

high_score = 0


def dice_game():
    while True:
        global high_score
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            roll_1 = random.randint(1, 6)
            print("\nYou rolled a...", roll_1)
            roll_2 = random.randint(1, 6)
            print("You rolled a...", roll_2, "\n")
            total = roll_1 + roll_2
            print("You have rolled a total of:", total, "\n")
            if total > high_score:
                print("New high score!\n")
                high_score = total
        if choice == "2":
            print("Goodbye!")
            break


dice_game()
