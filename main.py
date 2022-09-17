from random import randint, randrange, choice

fruit, vegi, home, off = "Go to Fruit farm", "Go to Vegetable farm", "Go to Home", "Quit the game"
decision_temp = "Enter a represented number to make a decision."
fruit_msg = "You are at the Fruit farm"
vegi_arv = "You are at the Vegetable farm"
home_arv = "You are at the home"
err_msg = "Invalid input. Type a number only."
fruit_obj = ("Grapes", "Apple", "Orange")
bag = {"Grapes": 0, "Apple": 0, "Orange": 0}


class InputError(Exception):
    def __init__(self, user_input):
        super().__init__(f"You entered '{user_input}'. Please enter provided number only.")


def bag_add(item, amount):
    bag[item] += amount
    print(f"You obtained {amount} {item}(s).\nBag : {bag}\nYou have {20 - sum(bag.values())} storage left.")
    joint_prompt()


def bag_full(item):
    bag[item] = bag[item] + (20 - sum(bag.values()))
    print(f"You obtained {20 - sum(bag.values())} {item}(s). Directing to home to empty the bag.")
    joint_prompt()


def quit_game():
    print("Thank you for playing!")
    exit()


def keyboard_int_msg(exit_num):
    print(f"\nIf you wish to quit the game, please type {exit_num}.")


def farm_choice():
    while True:
        try:
            decision = input(f"{decision_temp}\n1.{fruit}\n2.{vegi}\n3.{off}\n")
            if decision == '1':
                return fruit_farm()
            elif decision == '2':
                pass
            elif decision == '3':
                quit_game()
            else:
                raise InputError(decision)
        except KeyboardInterrupt:
            keyboard_int_msg(3)
        except InputError:
            print(InputError(decision))


def joint_prompt():
    while True:
        try:
            joint_msg = input("Hit enter to continue")
            if joint_msg == "":
                break
            else:
                print("Please hit only enter")
        except KeyboardInterrupt:
            print("\nYou will have option to quit the game after this step.")


def fruit_farm():
    print(fruit_msg)
    joint_prompt()
    while True:
        harvested_amount = randrange(1, 9)
        item = fruit_obj[randrange(0, len(fruit_obj) - 1)]
        try:
            decision = input(f"You found '{item}'(s)!!!\n{decision_temp}"
                             f"\n(1)Harvest (2)Skip (3){vegi} (4){off} (5){home}\n")
            if decision == '1' and sum(bag.values()) + harvested_amount <= 20:
                bag_add(item, harvested_amount)
            elif decision == '1' and sum(bag.values()) + harvested_amount > 20:
                bag_full(item)
                pass
            elif decision == '2':
                pass
            elif decision == '3':
                pass
            elif decision == '4':
                quit_game()
            elif decision == '5':
                pass
            else:
                raise InputError(decision)
        except InputError:
            print(InputError(decision))
        except KeyboardInterrupt:
            keyboard_int_msg(4)


farm_choice()