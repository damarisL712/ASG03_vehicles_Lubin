from abc import ABC, abstractmethod

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

    def how_far_with(self, num_of_gallons: int) -> float:
        return self._mpg * num_of_gallons

    # abstract method
    @abstractmethod
    def number_of_wheels(self) -> int: 
        ...
