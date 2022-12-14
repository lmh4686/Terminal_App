import pytest
import main
# Inputs that reamin as string
str_inputs = iter(['1', '2', '3', '4', 'a', '!'])
# Inputs that converted to integer
num_inputs = iter([1, 0, 5, 1.1, 'a'])


# For monkeypatch purposes
def fake_str_input(prompt):
    return next(str_inputs)


def fake_num_input(prompt):
    return next(num_inputs)


# --Outline--
# Testing for get_user_choice(prompt, option)
# Takes input message and option as arguments.
# If option is list, input remains to be string.
# If option is range, input gets converted to int.


class TestGetUserChoice:
    # ----When input reamins as string----
    # Test for correct input that in option.
    # All test should pass
    def test_str_valid_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_str_input)
        assert main.get_user_choice('a', ['1', '2', '3'])  # When input is '1'
        assert main.get_user_choice('a', ['1', '2', '3'])  # When input is '2'
        assert main.get_user_choice('a', ['1', '2', '3'])  # When input is '3'


    # Check if InputError gets raised for invalid input that is not in option.
    # All test should pass.
    def test_str_invalid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_str_input)
        with pytest.raises(main.InputError):
            main.get_user_choice('a', ['1', '2', '3'])  # When input is '4'
            main.get_user_choice('a', ['1', '2', '3'])  # When input is 'a'
            main.get_user_choice('a', ['1', '2', '3'])  # When input is '!'


    # ----When input get converted to int ----
    # Test for correct input that are in options.
    # All test should pass.
    def test_num_valid_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        assert main.get_user_choice('a', range(1, 5, 1))  # When input is 1


    # Check if RangeError raised.
    # Integer input case less than option's max value.
    # All test should pass.
    def test_num_smaller_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        with pytest.raises(main.RangeError):
            assert main.get_user_choice('a', range(1, 5, 1))  # When input is 0


    # Check if ExcessError raised
    # Positive integer input case bigger than option's max value.
    # All test should pass.
    def test_num_excess_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        with pytest.raises(main.ExcessError):
            assert main.get_user_choice('a', range(1, 5, 1))  # When input is 5


    # Check if ValueError raised for a none integer input.
    #  All test should pass.
    def test_num_not_int_input(self, monkeypatch):  # int input test
        monkeypatch.setattr("builtins.input", fake_num_input)
        with pytest.raises(ValueError):
            assert main.get_user_choice(
                'a', range(1, 5, 1))  # When input is 1.1
            assert main.get_user_choice(
                'a', range(1, 5, 1))  # When input is 'a'


# --Outline--
# Testing for bag_add(item, amount)
# Takes 2 arguments, obtained item's name and amount.
# Bag is a dictionary stores item by its name and amount.
class TestBagAdd:
    # Test if bag adds the value correctly to its respective key.
    # All test should pass.
    def test_adding(self):
        assert main.bag_add('Wheat', 4) == 4  # Add 4 Wheat
        assert main.bag_add('Wheat', 4) == 8  # Add 4 more Wheat
        assert main.bag_add('Plum', 3) == 3  # Add 3 plum


# All tests have been passed as expected.
