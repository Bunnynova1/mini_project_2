import random


def roll_dice():
    return random.randint(1, 6)


def main():
    print("Hi. Welcome to the Dice Game!😺")
    start_game = input("Do you want to play? (yes/no): ")

    if start_game.lower() == "no":
        print("Alright, see you next time!")
    else:
        print("Great. Let's start rolling the dice!")

        while True:
            input("|Press Enter to roll the dice| ")

            dice1 = roll_dice()
            dice2 = roll_dice()
            total = dice1 + dice2

            print(f"\nYou rolled: {dice1} + {dice2} = {total}")

            if total == 7 or total == 11:
                print("Congratulations! You win!🎉")
                break
            elif total == 2 or total == 3 or total == 12:
                print("Sorry, the casino wins. Better luck next time!😹")
                break
            else:
                goal = total
                print(f"Your goal is {goal}. Keep rolling 🎲!")

                while True:
                    input("|Press Enter to roll again| ")
                    dice1 = roll_dice()
                    dice2 = roll_dice()
                    total = dice1 + dice2

                    print(f"\nYou rolled: {dice1} + {dice2} = {total}")

                    if total == 7:
                        print("Oh no! You rolled a 7. You lose. Better luck next time!😹")
                        break
                    elif total == goal:
                        print("Congratulations! You matched your goal. You win!🎉")
                        break
            play_again = input("\nDo you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                print("\nThanks for playing! See you next time.😺")
                break


if __name__ == "__main__":
    main()
