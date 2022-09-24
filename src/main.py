from random import randint, randrange, choice
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style
import ascii_magic

# Package functions t= table, c= color, b= background, s= style, r= reset
t, c, b, s, r = PrettyTable(), Fore, Back, Style, Style.RESET_ALL
init()

# ASCii settings by locations
landing = ascii_magic.from_image_file(
    '../docs/landing.jpg',
    columns=70,
    back=ascii_magic.Back.BLACK)
fruit_landing = ascii_magic.from_image_file(
    '../docs/fruit_farm.jpg',
    columns=70,
    back=ascii_magic.Back.BLACK)
grain_landing = ascii_magic.from_image_file(
    '../docs/grain_farm.jpg',
    columns=50,
    back=ascii_magic.Back.BLACK)
home_landing = ascii_magic.from_image_file(
    '../docs/home.jpg', columns=60, back=ascii_magic.Back.BLACK)

# Commonly used templates
fruit, grain, off = "Go to Fruit farm", "Go to Grain farm", "Quit the game"
decision_temp = f"Enter a {c.RED}represented number{r} "\
                f"to make a {c.GREEN}decision{r}."
fruit_arv_msg = f"{b.LIGHTYELLOW_EX}{c.BLACK}{s.DIM}"\
                f"You are at the Fruit farm{r}"
grain_arv_msg = f"{b.LIGHTYELLOW_EX}{c.BLACK}{s.DIM}"\
                f"You are at the Grain farm{r}"
base_arv_msg = f"{b.LIGHTYELLOW_EX}{s.DIM}{c.BLACK}You are in home{r}"

# Error message for KeyboardInterrupt
key_itr_msg = f"\n{b.RED}{c.WHITE}You can't quit the game in this stage.{r}"

# Harvestable objects
fruit_obj = ("Plum", "Apple", "Orange")
grain_obj = ("Wheat", "Oat", "Corn")

# Storages
bag = {"Plum": 0, "Apple": 0, "Orange": 0, "Wheat": 0, "Oat": 0, "Corn": 0}
bag_limit = 30
storage = {"Plum": 0, "Apple": 0, "Orange": 0, "Wheat": 0, "Oat": 0, "Corn": 0}

# Variables for cook()
recipes = (
    {"Apple porridge": {
        "Apple": 7, "Wheat": 5, "Oat": 3, "Corn": 3}},
    {"Plum porridge": {
        "Plum": 5, "Wheat": 4, "Oat": 2, "Corn": 1}},
    {"Orange porridge": {
        "Orange": 8, "Wheat": 3, "Oat": 6, "Corn": 4}},
    {"Mixed porridge": {
        "Apple": 4, "Plum": 2, "Orange": 3, "Wheat": 2, "Oat": 3, "Corn": 1}}
)
available_dish = {
    "Apple porridge": 0,
    "Plum porridge": 0,
    "Orange porridge": 0,
    "Mixed porridge": 0}
grocery_quotients = []
printed_dish = {}


# Errors
class InputError(Exception):
    def __init__(self, user_input):
        super().__init__(f"You entered '{user_input}'."
                         f" Please enter {c.RED}provided number{r} only.")


class RangeError(Exception):
    pass


class ExcessError(Exception):
    pass


def keyboard_itr_msg(exit_num):
    print(f"\nIf you wish to {s.BRIGHT}{c.RED}quit{r} the game, "
          f"please type {c.RED}{exit_num}{r}.")


# Most used functions
def get_user_choice(prompt, options):
    user_input = input(prompt)
    if isinstance(options, list) and user_input not in options:
        raise InputError(user_input)
    elif isinstance(options, range) and user_input not in options:
        if int(user_input) > max(options):
            raise ExcessError
        elif int(user_input) <= 0:
            raise RangeError
    return user_input


def joint_prompt():
    while True:
        try:
            joint_msg = input(f"Hit {c.RED}enter{r} to continue")
        except KeyboardInterrupt:
            print(key_itr_msg)
        else:
            if joint_msg == "":
                break
            else:
                print(f"Please hit {c.RED}only enter{r}")


def quit_game():
    print(f"{b.LIGHTYELLOW_EX}{c.BLACK}{s.DIM}Thank you for playing!{r}")
    exit()


# Functions for farm
def obj_discover_msg(discovered_item):
    return f"You found {c.CYAN}{discovered_item}(s){r}!!!\n{decision_temp}"


def check_space(storage_type):
    t.field_names = [f"{c.GREEN}ITEM{r}", f"{c.CYAN}AMOUNT{r}"]
    for grocery, amount in storage_type.items():
        if amount > 0:
            t.add_row([grocery, amount])
    print(t)
    t.clear()
    joint_prompt()


def check_recipe():
    t.field_names = [f"{c.GREEN}DISH NAME{r}", f"{c.CYAN}RECIPE{r}"]
    for recipe in recipes:
        for dish_name, food_list in recipe.items():
            t.add_row([dish_name, food_list])
    print(t)
    t.clear()
    joint_prompt()


def bag_add(item, amount):
    bag[item] += amount
    if __name__ == '__main__':
        print(f"You obtained {c.CYAN}{amount} {item}(s){r}. "
              f"You have {c.GREEN}{bag_space()}{r} space left.")
        joint_prompt()
    else:
        return bag[item]


def bag_full(item):
    print(f"You obtained {c.CYAN}{bag_space()} {item}(s){r}.\n"
          f"Your {c.RED}bag is full{r}! "
          f"{c.GREEN}Directing home{r} to empty the bag.")
    bag[item] += bag_space()
    joint_prompt()
    return home()


def bag_space():
    available_space = bag_limit - sum(bag.values())
    return available_space


def farm_choice():
    while True:
        try:
            decision = get_user_choice(
                f"{decision_temp}\n(1){fruit}\n(2){grain}\n(3){off}\n",
                ['1', '2', '3'])
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


def main_farm(item, amount, other_farm):
    while True:
        try:
            decision = get_user_choice(
                f"{obj_discover_msg(item)}\n"
                f"(1)Harvest (2)Skip (3)Check bag (4)Check recipes\n"
                f"(5){other_farm} (6)Go to home (7){off}\n",
                ['1', '2', '3', '4', '5', '6', '7'])
        except InputError as err:
            print(err)
        except KeyboardInterrupt:
            keyboard_itr_msg(7)
        else:
            sub_farm_options(decision, item, amount, other_farm)
            if decision == '1' or decision == '2':
                break


def sub_farm_options(
                        user_input,
                        harvested_item,
                        harvested_amount,
                        other_farm):
    if user_input == '1' and sum(bag.values()) \
                     + harvested_amount < bag_limit:
        bag_add(harvested_item, harvested_amount)
    elif user_input == '1' and sum(bag.values()) \
                       + harvested_amount >= bag_limit:
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


def fruit_farm():
    ascii_magic.to_terminal(fruit_landing)
    print(fruit_arv_msg)
    joint_prompt()
    while True:
        harvested_amount = randint(1, 3)
        discovered_item = choice(fruit_obj)
        main_farm(discovered_item, harvested_amount, grain)


def grain_farm():
    ascii_magic.to_terminal(grain_landing)
    print(grain_arv_msg)
    joint_prompt()
    while True:
        harvested_amount = randrange(1, 3)
        discovered_item = choice(grain_obj)
        main_farm(discovered_item, harvested_amount, fruit)


# functions for home
def home_arrival():
    ascii_magic.to_terminal(home_landing)
    print(base_arv_msg)
    for grocery, amount in bag.items():
        storage[grocery] += amount
        bag[grocery] = 0
    print(f"All your {c.GREEN}items{r} in the bag have been "
          f"{c.RED}transferred{r} to the {c.GREEN}storage{r}.\nStorage : ")
    check_space(storage)
    get_available_dish()


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
    for recipe in recipes:
        for name in recipe.keys():
            if name != printed_dish[food_num]:
                break
        else:
            for grocery, number in recipe[name].items():
                storage[grocery] -= (number * amount)
    get_available_dish()
    print(f"Congrats!! You cooked {c.GREEN}{amount} "
          f"{printed_dish[food_num]}{r}!"
          f"\nNow your storage has :\n")
    check_space(storage)


def print_available_dish():
    order_num = 0
    for dish_name, dish_amount in available_dish.items():
        if dish_amount > 0:
            order_num += 1
            print(f"({order_num})Cook {c.GREEN}{dish_name}{r}")
            printed_dish[str(order_num)] = dish_name


def home():
    home_arrival()
    while sum(available_dish.values()) > 0:
        print(f"You can {c.GREEN}cook{r} :")
        for name, amount in available_dish.items():
            if amount > 0:
                print(f"{c.CYAN}{amount}{r} of {c.GREEN}{name}{r}")
        try:
            decision = get_user_choice(
                f"{decision_temp}\n"
                f"(1)Choose dish to cook (2)Cook later go to farm to harvest "
                f"(3){off}\n",
                ['1', '2', '3'])
        except KeyboardInterrupt:
            keyboard_itr_msg(3)
        except InputError as err:
            print(err)
        else:
            if decision == '1':
                while True:
                    print(decision_temp)
                    print_available_dish()
                    try:
                        food_choice = get_user_choice(
                            "", list(printed_dish.keys()))
                    except InputError as err:
                        print(err)
                    except KeyboardInterrupt:
                        print(key_itr_msg)
                    else:
                        break
                while True:
                    max_dish_num = available_dish[printed_dish[food_choice]]
                    try:
                        food_amount = int(
                            get_user_choice(
                                f"How many {c.GREEN}"
                                f"{printed_dish[food_choice]}{r} "
                                f"do you want to {c.GREEN}cook{r}? "
                                f"Max: {c.RED}{max_dish_num}{r}\n",
                                range(1, max_dish_num + 1, 1)))
                    except (ValueError, RangeError):
                        print(f"{b.RED}{c.WHITE}Please enter a positive "
                              f"integer bigger than zero.{r}")
                    except KeyboardInterrupt:
                        print(key_itr_msg)
                    except ExcessError:
                        print(f"{b.RED}{c.WHITE}The maximum available amount "
                              f"for this dish is {max_dish_num}.{r}")
                    else:
                        cook(food_choice, food_amount)
                        break
            elif decision == '2':
                return farm_choice()
            elif decision == '3':
                quit_game()
            else:
                raise InputError(decision)
    print(f"You {c.RED}don't have enough ingredients{r} to cook.\n"
          f"{c.GREEN}Go back to farm{r} and "
          f"{c.CYAN}harvest more{r} ingredients.")
    return farm_choice()


if __name__ == "__main__":
    ascii_magic.to_terminal(landing)
    print(f"{b.LIGHTYELLOW_EX}{c.BLACK}{s.DIM}Welcome to farming game!{r}\n"
          f"{c.GREEN}Harvest ingredients from 2 different "
          f"farms and cook them at home!{r}")
    joint_prompt()
    farm_choice()
