import pytest
import os
from housing_ui import validate_input

class TestUIOfHousing:
    """Class for grouping tests"""
    def test_UI_should_validate_input_if_valid(self):
        """ To check if user submitted input is among valid commands"""
        assert validate_input("1")
        assert validate_input("2")
        assert validate_input("3")
        assert validate_input("4")
        assert validate_input("5")
        assert validate_input("6")
    
    def test_UI_should_raise_error_if_input_is_invalid(self):
        """ To check if user submitted input is among valid commands"""
        with pytest.raises(ValueError):
            validate_input("invalid")

        with pytest.raises(ValueError):
            validate_input("7")

