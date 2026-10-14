"""
Local tests 

Author: Damaris Lubin 

Run with: 
    pytest -v test_local.py
"""

import pytest
from manufacturer import Manufacturer
from auto_model import AutoModel
from vehicle import Vehicle
from sedan import Sedan
from truck import Truck

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

class TestVehicle:
    # Test that Vehicle cannot be created directly because it is abstract.
    def test_vehicle_is_abstract(self):
        manufacturer = Manufacturer("Ford", "USA")
        model = AutoModel("F150", True, [2020, 2021, 2022])

        with pytest.raises(TypeError):
            Vehicle(manufacturer, model, 20.0)


class TestSedan:
    # Test that the Sedan constructor and inherited getters work correctly.
    def test_sedan_constructor_and_getters(self):
        sedan = Sedan(Manufacturer("Honda", "Japan"), AutoModel("Civic", False, [1996, 1997, 1998]), 28.0)
        assert sedan.manufacturer.name == "Honda"
        assert sedan.manufacturer.country == "Japan"
        assert sedan.model.name == "Civic"
        assert sedan.mpg == 28.0

    # Test that a sedan always has four wheels.
    def test_number_of_wheels(self):
        sedan = Sedan(Manufacturer("Honda", "Japan"), AutoModel("Civic", False, [1996, 1997, 1998]), 28.0)
        assert sedan.number_of_wheels() == 4

    # Test that the release year comes from the AutoModel.
    def test_release_year(self):
        sedan = Sedan(Manufacturer("BMW", "Germany"), AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018]), 30.0)
        assert sedan.release_year == 2015

    # Test how far the sedan can travel with a given number of gallons.
    def test_how_far_with(self):
        sedan = Sedan(Manufacturer("Honda", "Japan"), AutoModel("Civic", False, [1996, 1997, 1998]), 28.0)
        assert sedan.how_far_with(10) == 280.0

    # Test that the Sedan string is formatted correctly.
    def test_sedan_str(self):
        sedan = Sedan(Manufacturer("Honda", "Japan"), AutoModel("Civic", False, [1996, 1997, 1998]), 28.0)
        assert str(sedan) == "(Honda, Japan) Civic in production = False, release year: 1996, mpg: 28.00"

class TestTruck:
    # Test that a truck is not dually by default.
    def test_default_not_dually(self):
        truck = Truck(Manufacturer("Ford", "USA"), AutoModel("F150", True, [2020, 2021, 2022]), 20.0)
        assert truck.is_dually is False

    # Test that a non-dually truck has four wheels.
    def test_non_dually_wheels(self):
        truck = Truck(Manufacturer("Ford", "USA"), AutoModel("F150", True, [2020, 2021, 2022]), 20.0)
        assert truck.number_of_wheels() == 4

    # Test that a dually truck has six wheels.
    def test_dually_wheels(self):
        truck = Truck(Manufacturer("Toyota", "Japan"), AutoModel("Tundra", False, [1987, 1988]), 30.0, True)
        assert truck.number_of_wheels() == 6

    # Test that the dually property returns True when set.
    def test_is_dually_true(self):
        truck = Truck(Manufacturer("Toyota", "Japan"), AutoModel("Tundra", False, [1987, 1988]), 30.0, True)
        assert truck.is_dually is True

    # Test that the release year comes from AutoModel.
    def test_release_year(self):
        truck = Truck(Manufacturer("Toyota", "Japan"), AutoModel("Tundra", False, [1987, 1988]), 30.0, True)
        assert truck.release_year == 1987

    # Test how far the truck can travel with a given number of gallons.
    def test_how_far_with(self):
        truck = Truck(Manufacturer("Toyota", "Japan"), AutoModel("Tundra", False, [1987, 1988]), 30.0, True)
        assert truck.how_far_with(5) == 150.0

    # Test that the Truck string is formatted correctly.
    def test_truck_str(self):
        truck = Truck(Manufacturer("Toyota", "Japan"), AutoModel("Tundra", False, [1987, 1988]), 30.0, True)
        assert str(truck) == "(Toyota, Japan) Tundra in production = False, release year: 1987, mpg: 30.00 is dually truck: True"
