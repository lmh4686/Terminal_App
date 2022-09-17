from random import randint, randrange, choice

fruit, grain, home, off = "Go to Fruit farm", "Go to Grain farm", "Go to Home", "Quit the game"
decision_temp = "Enter a represented number to make a decision."
fruit_arv_msg = "You are at the Fruit farm"
grain_arv_msg = "You are at the Grain farm"
home_arv_msg = "You are in home"
err_msg = "Invalid input. Type a number only."
fruit_obj = ("Plum", "Apple", "Orange")
grain_obj = ("Wheat", "Oat", "Corn")
bag = {"Plum": 0, "Apple": 0, "Orange": 0, "Wheat": 0, "Oat": 0, "Corn": 0}
bag_limit = 30


class InputError(Exception):
    def __init__(self, user_input):
        super().__init__(f"You entered '{user_input}'. Please enter provided number only.")


def bag_add(item, amount):
    bag[item] += amount
    print(f"You obtained {amount} {item}(s).\nBag : {bag}\nYou have {bag_limit - sum(bag.values())} storage left.")
    joint_prompt()
    if sum(bag.values()) == bag_limit:
        pass


def bag_full(item):
    bag[item] = bag[item] + (bag_limit - sum(bag.values()))
    print(f"You obtained {bag_limit - sum(bag.values())} {item}(s). Directing to home to empty the bag.")
    joint_prompt()


def quit_game():
    print("Thank you for playing!")
    exit()


def keyboard_int_msg(exit_num):
    print(f"\nIf you wish to quit the game, please type {exit_num}.")


def farm_choice():
    while True:
        try:
            decision = input(f"{decision_temp}\n1.{fruit}\n2.{grain}\n3.{off}\n")
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
    print(fruit_arv_msg)
    joint_prompt()
    while True:
        harvested_amount = randrange(1, 3)
        item = fruit_obj[randrange(0, len(fruit_obj))]
        while True:
            try:
                decision = input(f"You found '{item}'(s)!!!\n{decision_temp}"
                                 f"\n(1)Harvest (2)Skip (3){grain} (4){home} (5){off}\n")
                if decision == '1' and sum(bag.values()) + harvested_amount <= bag_limit:
                    bag_add(item, harvested_amount)
                    break
                elif decision == '1' and sum(bag.values()) + harvested_amount > bag_limit:
                    bag_full(item)
                    print("Bag full")
                elif decision == '2':
                    break
                elif decision == '3':
                    return grain_farm()
                elif decision == '4':
                    pass
                elif decision == '5':
                    return quit_game()
                else:
                    raise InputError(decision)
            except InputError:
                print(InputError(decision))
            except KeyboardInterrupt:
                keyboard_int_msg(5)


def grain_farm():
    print(grain_arv_msg)
    joint_prompt()
    while True:
        harvested_amount = randrange(1, 3)
        item = grain_obj[randrange(0, len(fruit_obj))]
        while True:
            try:
                decision = input(f"You found '{item}'(s)!!!\n{decision_temp}"
                                 f"\n(1)Harvest (2)Skip (3){fruit} (4){home} (5){off}\n")
                if decision == '1' and sum(bag.values()) + harvested_amount <= bag_limit:
                    bag_add(item, harvested_amount)
                    break
                elif decision == '1' and sum(bag.values()) + harvested_amount > bag_limit:
                    bag_full(item)
                    print("Bag full")
                elif decision == '2':
                    break
                elif decision == '3':
                    return fruit_farm()
                elif decision == '4':
                    pass
                elif decision == '5':
                    quit_game()
                else:
                    raise InputError(decision)
            except InputError:
                print(InputError(decision))
            except KeyboardInterrupt:
                keyboard_int_msg(5)

farm_choice()

