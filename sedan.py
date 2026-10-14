from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel


class Sedan(Vehicle):
    'Sedan class inherits vehicle class properties'
    def __init__(self, manufacturer: Manufacturer, model: AutoModel, mpg: float):
        super().__init__(manufacturer, model, mpg)

    def number_of_wheels(self) -> int:
        return 4

    def __str__(self):
        # format: (<manufacturer>) <model>, mpg: <mpg formatted to 2 decimal places>
        # Example: (Honda, Japan) Civic in production = False, release year: 1996, mpg: 28.00

        return f"({self._manufacturer}) {self._model}, mpg: {self._mpg:.2f}"




