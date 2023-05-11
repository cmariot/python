import random


def str_to_integer(string: str):
    """
    Takes a string and returns an integer if it's a valid integer
    """
    try:
        return int(string)
    except ValueError:
        return None


def guess():
    instructions = """This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n"""
    print(instructions)
    try_number = 1
    random_number = random.randint(1, 99)
    while (1):
        try:
            choice = input("What's your guess between 1 and 99?\n>> ")
            if (choice == 'exit'):
                return
            choice = str_to_integer(choice)
            if (choice is None):
                print("That's not a number")
            elif (choice > random_number):
                print("Too high!")
            elif (choice < random_number):
                print("Too low!")
            else:
                if (choice == 42):
                    print("The answer to the ultimate question of life,",
                          end="")
                    print("the universe and everything is 42.")
                if (try_number == 1):
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you've got it!")
                    print("You won in", try_number, "attempts!")
                return
            try_number += 1
        except EOFError:
            print()
            continue
        except KeyboardInterrupt:
            print()
            continue


if __name__ == "__main__":
    guess()
