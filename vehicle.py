from abc import ABC, abstractmethod
# Import total_ordering to automatically provide additional comparison methods.
from functools import total_ordering
from manufacturer import Manufacturer
from auto_model import AutoModel

class Vehicle(ABC):
    'Abstract base class for all types of vehicles'
    def __init__(self, manufacturer: Manufacturer, model: AutoModel, mpg: float):
        self._manufacturer = manufacturer
        self._model = model
        self._mpg = mpg

    @property
    def manufacturer(self) -> Manufacturer:
        return self._manufacturer
        
    @property
    def model(self) -> AutoModel:
        return self._model
        
    @property
    def mpg(self) -> float:
        return self._mpg
    
    @property
    # using inheritance in the way of getting the first year from auto model
    def release_year(self) -> int:
        return self._model.first_year

    # Concrete method
    def how_far_with(self, num_of_gallons: int) -> float:
        return self._mpg * num_of_gallons

    # abstract method
    @abstractmethod
    def number_of_wheels(self) -> int: 
        ...
    
    # --- Comprable using @functools.total_ordering

    # Check if two vehicles have the same release year.

    def __eq__(self, other) -> bool:
        return self.release_year == other.release_year
    
    # Check if this vehicle was released before another vehicle.
    def __lt__(self, other):
        return self.release_year < other.release_year

