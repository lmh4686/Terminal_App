import pytest
import main

str_inputs = iter(['1', '2', '3', '4', 'a', '!'])
num_inputs = iter([1, 0, 5, 1.1, 'a'])


def fake_str_input(prompt):
    return next(str_inputs)


def fake_num_input(prompt):
    return next(num_inputs)

#Testing for get_user_choice(prompt, option) that takes input message and option as arguments. 
#When option is list, input reamins to be string. If option is range, input gets converted to int.
class TestGetUserChoice:
    #Test for correct input that in option. This should pass
    def test_str_valid_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_str_input)
        assert main.get_user_choice('a', ['1', '2', '3'])
        assert main.get_user_choice('a', ['1', '2', '3'])
        assert main.get_user_choice('a', ['1', '2', '3'])
        
    #Check if InputError gets raised for invalid input that is not in option. This should pass.
    def test_str_invalid_input(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_str_input)
        with pytest.raises(main.InputError): 
            main.get_user_choice('a', ['1', '2', '3'])
            main.get_user_choice('a', ['1', '2', '3'])
            main.get_user_choice('a', ['1', '2', '3'])

    #Test for correct input that are in options. This should pass.
    def test_num_valid_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        assert main.get_user_choice('a', range(1, 5, 1))
        # assert main.get_user_choice('a', range(1, 5, 1))
      
    #Check if RangeError gets rasied for a integer input that are smaller than option's max value. This should pass.
    def test_num_smaller_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        with pytest.raises(main.RangeError):
            assert main.get_user_choice('a', range(1, 5, 1))
 
    #Check if ExcessError gets rasied for an positve integer input that are bigger than option's max value. This should pass.
    def test_num_excess_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        with pytest.raises(main.ExcessError): 
            assert main.get_user_choice('a', range(1, 5, 1))

    #Check if ValueError gets raised for a none integer input. This should pass.
    def test_num_not_int_input(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_num_input)
        with pytest.raises(ValueError):
            assert main.get_user_choice('a', range(1, 5, 1))
            assert main.get_user_choice('a', range(1, 5, 1))
            

class TestCook:
    def test_ff(self):
        assert main.printed_dish == {'1': 'Apple Porridge', '2': 'Orange Porridge', '3': 'Plum Porridge'}
        assert main.storage == {'Apple': 20, 'Orange': 10, 'Plum': 10, 'Wheat': 20, 'Oat': 20, 'Corn': 20}
        assert main.cook('1', 2) == {'Apple': 6, 'Orange': 10, 'Plum': 10, 'Wheat': 10, 'Oat': 14, 'Corn': 14}

#bag_add(item, amount) takes 2 arguments one is obtained item name and amount.
#Bag is a dictionary stores item by its name and amount.
class TestBagAdd:
    #Test if bag adds the value correctly by item. This should pass
    def test_adding(self):
        assert main.bag_add('Wheat', 4) == 4 
        assert main.bag_add('Wheat', 4) == 8
        assert main.bag_add('Plum', 3) == 3



