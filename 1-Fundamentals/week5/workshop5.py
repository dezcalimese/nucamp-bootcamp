import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    while tries != 0:
        print("Number of tries remaining: ", tries)
        guessing = int(input("Guess a number between 0 and 10: "))
        if guessing == random_number:
            print("You guessed the correct number!")
            break
        elif guessing < random_number:
            print("Guess higher!")
            tries -= 1
        elif guessing > random_number:
            print("Guess lower!")
            tries -= 1
        else:
            break
    print("You have failed to guess the number:", random_number)


guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    random_number = random.randrange(start, stop)
    print("The number for the program to guess is:", random_number)
    print("Number of tries left:", tries)
    for num in range(start, stop):
        print("The program is guessing...", num)
        if num == random_number:
            print("The program has guessed the correct number!")
            return
        else:
            tries -= 1
            print("Number of tries left:", tries)
        if tries == 0:
            print("The program has failed to guess the correct number.")
            return


guess_random_num_linear(5, 0, 10)


def guess_random_num_binary(tries, start, stop):
    random_number = random.randrange(start, stop)
    print("Random number to find:", random_number)

    lower_bound = start
    upper_bound = stop

    while tries != 0:
        pivot = (lower_bound + upper_bound) // 2

        if pivot == random_number:
            print("Found it!", random_number)
            return
        elif pivot > random_number:
            print("Guessing higher!")
            upper_bound = pivot - 1
            tries -= 1
        else:
            print("Guessing lower!")
            lower_bound = pivot + 1
            tries -= 1
        if tries == 0:
            print("Your program failed to find the number.")


guess_random_num_binary(5, 0, 100)
