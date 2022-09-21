import pytest
import main

inputs = iter(['1', '2', '3', 'a', '!'])


def fake_input(prompt):
    return next(inputs)


class TestGetUserChoice:
    def test_valid(self, monkeypatch):
        monkeypatch.setattr("builtins.input", fake_input)
        assert main.get_user_choice('a', ['1', '2', '3']) == '1'
        assert main.get_user_choice('a', ['1', '2', '3']) == '2'
        assert main.get_user_choice('a', ['1', '2', '3']) == '3'
        

    def test_input_err(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        with pytest.raises(main.InputError): #Telling pytest to setup the context manager that expect the RangeError to happen and within that context call get_int() if RangeError happen, test will pass
            main.get_user_choice('a', ['1', '2', '3'])
            main.get_user_choice('a', ['1', '2', '3'])
