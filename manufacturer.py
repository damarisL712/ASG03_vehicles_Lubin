class Manufacturer:
    """Represents a vehicle manufacturer."""
    # constructor that initializes the manufacturer's name and country
    def __init__(self, name: str, country: str):
        # store the manufacturer's name
        self._name = name
        self._country = country
    
    # getter for the manufacturer's name
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def country(self) -> str:
        return self._country


    def __str__(self):
        return f"{self._name}, {self._country}"
