"""
Local tests 

Author: Damaris Lubin 

Run with: 
    pytest -v test_local.py
"""

import pytest
from manufacturer import Manufacturer

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
        assert manu.get_name == "Honda"
    

    def test_manufacturer_getter_country(self):
        manu = Manufacturer("BMW", "Germany")
        assert manu.get_country == "Germany"
