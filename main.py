from random import randint, randrange
fruit, vegi, home, off = "Go to Fruit farm", "Go to Vegetable farm", "Go to Home", "Quit the game"
decision_temp = "Enter a represented number to make a decision."
fruit_arv = "You are at the Fruit farm"
vegi_arv = "You are at the Vegetable farm"
home_arv = "You are at the home"
err_msg = "Invalid input. Type a number only."


class InputError(Exception):
    def __init__(self, user_input):
        super().__init__(f"You entered '{user_input}'. Please enter provided number only.")



def farm_choice():
    while True:
        try:
            decision = input(f"{decision_temp}\n1. {fruit}     2.{vegi}\n")
            if decision == '1':
                print(fruit_arv)
                break
            elif decision == '2':
                print(vegi_arv)
                break
            elif decision not in ['1', '2']:
                raise InputError(decision)
        except InputError:
            print(InputError(decision))


def fruit_farm():





