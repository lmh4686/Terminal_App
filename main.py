from random import randint, randrange, choice
from prettytable import PrettyTable
import json
import csv
t = PrettyTable()
fruit, grain, off = "Go to Fruit farm", "Go to Grain farm", "Quit the game"
decision_temp = "Enter a represented number to make a decision."
fruit_arv_msg = "You are at the Fruit farm"
grain_arv_msg = "You are at the Grain farm"
base_arv_msg = "You are in home"
key_itr_msg = "You can't quit the game in this stage."
fruit_obj = ("Plum", "Apple", "Orange")
grain_obj = ("Wheat", "Oat", "Corn")
bag = {"Plum": 0, "Apple": 0, "Orange": 0, "Wheat": 0, "Oat": 0, "Corn": 0}
bag_limit = 30
storage = {"Plum": 0, "Apple": 0, "Orange": 0, "Wheat": 0, "Oat": 0, "Corn": 0}
recipes = (
    {"Apple porridge": {"Apple": 7, "Wheat": 5, "Oat": 3, "Corn": 3}},
    {"Plum porridge": {"Plum": 5, "Wheat": 4, "Oat": 2, "Corn": 1}},
    {"Orange porridge": {"Orange": 8, "Wheat": 3, "Oat": 6, "Corn": 4}},
    {"Mixed porridge": {"Apple": 4, "Plum": 2, "Orange": 3, "Wheat": 2, "Oat": 3, "Corn": 1}}
)
available_dish = {"Apple porridge": 0, "Plum porridge": 0, "Orange porridge": 0, "Mixed porridge": 0}
grocery_quotients = []
printed_dish = {}


class InputError(Exception):
    def __init__(self, user_input):
        super().__init__(f"You entered '{user_input}'. Please enter provided number only.")


class RangeError(Exception):
    pass


class ExcessError(Exception):
    pass


def keyboard_itr_msg(exit_num):
    print(f"\nIf you wish to quit the game, please type {exit_num}.")


def get_user_choice(prompt, options):
    user_input = input(prompt)
    if type(options) is list and user_input not in options:
        raise InputError(user_input)
    elif type(options) is range and user_input not in options:
        if int(user_input) > max(options):
            raise ExcessError
        elif int(user_input) <= 0:
            raise RangeError
    return user_input


def joint_prompt():
    while True:
        try:
            joint_msg = input("Hit enter to continue")
        except KeyboardInterrupt:
            print(key_itr_msg)
        else:
            if joint_msg == "":
                break
            else:
                print("Please hit only enter")


def obj_discover_msg(discovered_item):
    return f"You found '{discovered_item}'(s)!!!\n{decision_temp}"


def check_space(storage_type):
    t.field_names = ["ITEM", "AMOUNT"]
    for grocery, amount in storage_type.items():
        if amount > 0:
            t.add_row([grocery, amount])
    print(t)
    t.clear()
    joint_prompt()


def check_recipe():
    t.field_names = ["DISH NAME", "RECIPE"]
    for item in recipes:
        for dish_name, recipe in item.items():
            t.add_row([dish_name, recipe])
    print(t)
    t.clear()
    joint_prompt()


def bag_add(item, amount):
    bag[item] += amount
    print(f"You obtained {amount} {item}(s). You have {bag_space()} storage left.")
    joint_prompt()


def bag_full(item):
    print(f"You obtained {bag_space()} {item}(s).\n"
          f"Your bag is full! Directing home to empty the bag.")
    bag[item] += bag_space()
    joint_prompt()
    return home()


def bag_space():
    available_space = bag_limit - sum(bag.values())
    return available_space


def quit_game():
    print("Thank you for playing!")
    exit()


def farm_choice():
    while True:
        try:
            decision = get_user_choice(f"{decision_temp}\n(1).{fruit}\n(2).{grain}\n(3).{off}\n", ['1', '2', '3'])
        except KeyboardInterrupt:
            keyboard_itr_msg(3)
        except InputError as err:
            print(err)
        else:
            if decision == '1':
                return fruit_farm()
            elif decision == '2':
                return grain_farm()
            elif decision == '3':
                quit_game()


def shared_farm_options(user_input, harvested_item, harvested_amount, other_farm):
    if user_input == '1' and sum(bag.values()) + harvested_amount < bag_limit:
        bag_add(harvested_item, harvested_amount)
    elif user_input == '1' and sum(bag.values()) + harvested_amount >= bag_limit:
        bag_full(harvested_item)
    elif user_input == '2':
        pass
    elif user_input == '3':
        check_space(bag)
    elif user_input == '4':
        check_recipe()
    elif user_input == '5':
        return grain_farm() if 'Grain' in other_farm else fruit_farm()
    elif user_input == '6':
        return home()
    elif user_input == '7':
        quit_game()


def main_farm(item, amount, other_farm):
    while True:
        try:
            decision = get_user_choice(f"{obj_discover_msg(item)}"
                                       f"\n(1)Harvest (2)Skip (3)Check bag (4)Check recipes\n"
                                       f"(5){other_farm} (6)Go to home (7){off}\n",
                                       ['1', '2', '3', '4', '5', '6', '7'])
        except InputError as err:
            print(err)
        except KeyboardInterrupt:
            keyboard_itr_msg(7)
        else:
            shared_farm_options(decision, item, amount, other_farm)
            if decision == '1' or '2':
                break


def fruit_farm():
    print(fruit_arv_msg)
    joint_prompt()
    while True:
        harvested_amount = randint(1, 3)
        discovered_item = choice(fruit_obj)
        main_farm(discovered_item, harvested_amount, grain)


def grain_farm():
    print(grain_arv_msg)
    joint_prompt()
    while True:
        harvested_amount = randrange(1, 3)
        discovered_item = choice(grain_obj)
        main_farm(discovered_item, harvested_amount, fruit)


def get_available_dish():
    for item in recipes:
        for name, recipe in item.items():
            for grocery, amount in recipe.items():
                if storage[grocery] < amount:
                    available_dish[name] = 0
                    break
            else:
                for grocery, amount in recipe.items():
                    grocery_quotients.append(storage[grocery] // amount)
                available_dish[name] = min(grocery_quotients)
                grocery_quotients.clear()


def cook(food_num, amount):
    for item in recipes:
        for name in item.keys():
            if name != printed_dish[food_num]:
                break
        else:
            for grocery, number in item[name].items():
                storage[grocery] -= (number * amount)
    get_available_dish()
    print(f"Congrats!! You cooked {amount} {printed_dish[food_num]}!\nNow your storage has :\n"
          f"{storage}")
    joint_prompt()


def home():
    print(base_arv_msg)
    for grocery, amount in bag.items():
        storage[grocery] += amount
        bag[grocery] = 0
    print("All your items in the bag have been transferred to the storage\nStorage : ")
    check_space(storage)
    get_available_dish()
    while sum(available_dish.values()) >= 1:
        print("You can cook :")
        for name, amount in available_dish.items():
            if amount >= 1:
                print(f"{amount} of {name}")
        joint_prompt()
        try:
            decision = get_user_choice(f"{decision_temp}\n"
                                       f"(1)Choose dish to cook  (2)Cook later go to farm to harvest (3){off}\n",
                                       ['1', '2', '3'])
        except KeyboardInterrupt:
            keyboard_itr_msg(3)
        except InputError as err:
            print(err)
        else:
            if decision == '1':
                while True:
                    print(decision_temp)
                    order = 0
                    for dish_name, dish_amount in available_dish.items():
                        if dish_amount > 0:
                            order += 1
                            print(f"({order})Cook {dish_name}")
                            printed_dish[str(order)] = dish_name
                    try:
                        food = get_user_choice("", list(printed_dish.keys()))
                    except InputError as err:
                        print(err)
                    except KeyboardInterrupt:
                        print(key_itr_msg)
                    else:
                        break
                while True:
                    max_dish_num = available_dish[printed_dish[food]]
                    try:
                        food_amount = int(get_user_choice(f"How many {printed_dish[food]} do you want to cook? "
                                                          f"Max: {max_dish_num}\n", range(1, max_dish_num + 1, 1)))
                    except (ValueError, RangeError):
                        print("Please enter a positive integer bigger than zero.")
                    except KeyboardInterrupt:
                        print(key_itr_msg)
                    except ExcessError:
                        print(f"The maximum available amount for this dish is {max_dish_num}.")
                    else:
                        cook(food, food_amount)
                        break
            elif decision == '2':
                return farm_choice()
            elif decision == '4':
                quit_game()
            else:
                raise InputError(decision)
    else:
        print("You don't have enough ingredients to cook. Go back to farm and harvest more ingredients.")
        return farm_choice()


farm_choice()

