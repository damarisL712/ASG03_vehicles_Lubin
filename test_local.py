"""
Local tests 

Author: Damaris Lubin 

Run with: 
    pytest -v test_local.py
"""

import pytest
from manufacturer import Manufacturer
from auto_model import AutoModel

class TestManufacturer: 
    # tests that the constructor sotres the name and country correctly
    def test_manufacturer_init(self):
        # creates manufacturer object
        manu = Manufacturer("Ford", "USA")
        # checks that the name was stored correctly
        assert manu._name == "Ford"
        # checks that the country was stored correctly 
        assert manu._country == "USA"

    def test_manufacturer_getter_name(self):
        manu = Manufacturer("Honda", "Japan")
        assert manu.name == "Honda"
    

    def test_manufacturer_getter_country(self):
        manu = Manufacturer("BMW", "Germany")
        assert manu.country == "Germany"


class TestAutoModel:
    # Test that the constructor and getters work correctly.
    def test_constructor_and_getters(self):
        am = AutoModel("Civic", False, [1996, 1997, 1998])

        assert am.name == "Civic"
        assert am.in_production is False
        assert am.years == [1996, 1997, 1998]

    # Test that the first year is returned correctly.
    def test_first_year(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])

        assert am.first_year == 2020

    # Test that the string is formatted correctly.
    def test_str(self):
        am = AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018])

        assert str(am) == "M3 Limited in production = False, release year: 2015"

    # Test that an empty years list raises a ValueError.
    def test_empty_years_raises(self):
        with pytest.raises(ValueError):
            AutoModel("Ghost", False, [])

    # Test that changing the original list does not change the model.
    def test_years_defensive_copy(self):
        years = [2000, 2001]

        am = AutoModel("Test", True, years)

        years.append(2002)

        assert am.years == [2000, 2001]

    # Test that changing the returned list does not change the model.
    def test_years_getter_returns_copy(self):
        am = AutoModel("Test", True, [2000, 2001])

        returned_years = am.years

        returned_years.append(2002)

        assert am.years == [2000, 2001]
