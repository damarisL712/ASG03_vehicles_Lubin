from vehicle import Vehicle
from manufacturer import Manufacturer
from auto_model import AutoModel


class Sedan(Vehicle):
    'Sedan class inherits vehicle class properties'
    def __init__(self, manufacturer: Manufacturer, model: AutoModel, mpg: float):
        super().__init__(manufacturer, model, mpg)

    def number_of_wheels(self) -> int:
        return 4




