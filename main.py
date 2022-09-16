from random import randint, randrange, choice
fruit, vegi, home, off = "Go to Fruit farm", "Go to Vegetable farm", "Go to Home", "Quit the game"
decision_temp = "Enter a represented number to make a decision."
fruit_arv = "You are at the Fruit farm"
vegi_arv = "You are at the Vegetable farm"
home_arv = "You are at the home"
err_msg = "Invalid input. Type a number only."
harvested_amount = randrange(1, 5)
fruit_obj = choice([{"Grapes": harvested_amount}, {"Apple": harvested_amount}, {"Orange": harvested_amount}])
bag = {"Grapes": 0, "Apple": 0, "Orange": 0}


class InputError(Exception):
    def __init__(self, user_input):
        super().__init__(f"You entered '{user_input}'. Please enter provided number only.")


def quit_game():
    raise ValueError


def farm_choice():
    while True:
        try:
            decision = input(f"{decision_temp}\n1.{fruit}\n2.{vegi}\n3.{off}\n")
            if decision == '1' or decision == '2':
                break
            elif decision == '3':
                quit_game()
            else:
                raise InputError(decision)
        except InputError:
            print(InputError(decision))
        except ValueError:
            print("Thank you for playing!")
            break
    if decision == '1':
        fruit_farm()


def joint_prompt():
    while True:
        joint_msg = input("Hit enter to continue")
        if joint_msg == "":
            break
        else:
            print("Please hit only enter")


def fruit_farm():
    print(fruit_arv)
    joint_prompt()
    for k, v in fruit_obj.items():
        decision = input(f"You found {k}(s)!!!\n{decision_temp}\n(1)Harvest (2)Skip (3){vegi} (4){off} (5){home}\n")
        if decision == '1':
            bag[k] += v
            print(f"You obtained {v} {k}.")







farm_choice()
