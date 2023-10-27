import pytest
import os
#from housing_ui import classmethod

class TestUIOfHousing:
    """Class for grouping tests"""
    def test_UI_should_validate_input_if_valid(self):
        """ To check if user submitted input is among valid commands"""
        assert validate_input("valid")
    
    def test_UI_should_raise_error_if_input_is_invalid(self):
        """ To check if user submitted input is among valid commands"""
        with pytest.raises(ValueError):
            validate_input("invalid")

