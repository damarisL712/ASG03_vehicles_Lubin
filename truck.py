from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel


class Truck(Vehicle):
    'truck class inherits vehicle class properties'
    def __init__(self, manufacturer: Manufacturer, model: AutoModel, mpg: float, is_dually = False):
        super().__init__(manufacturer, model, mpg)
        self._is_dually = is_dually

    # getter to return false by default
    @property
    def is_dually(self) -> bool:
        return self._is_dually


    def number_of_wheels(self) -> int:
        if self._is_dually == True: 
            return 6
        else:
            return 4

    def __str__(self):
        # format: (<manufacturer>) <model>, mpg: <mpg formatted to 2 decimal places>
        # Example: (Honda, Japan) Civic in production = False, release year: 1996, mpg: 28.00

        return f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f} is dually truck: {self._is_dually} "

