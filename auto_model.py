"""
Represents an automodel class

Will store the model name, whether the model is still in production, and the years the model was produced
"""
class AutoModel: 
    'represents an automodel class' 
     
    # Constructor that initializes the model information.
    def __init__(self, name: str, in_production: bool, years: list[int]):
        # Defensive check to make sure the years list is not empty.
        if not years:
            raise ValueError("The years list must not be empty")

        # Store the model name.
        self._name = name

        # Store whether the model is still in production.
        self._in_production = in_production

        # Store a copy of the years list.
        self._years = years.copy()

    # Getter for the model name.
    @property
    def name(self) -> str:
        return self._name

    # Getter for whether the model is still in production.
    @property
    def in_production(self) -> bool:
        return self._in_production

    # Getter for the production years.
    # Return a copy so the internal list cannot be changed directly.
    @property
    def years(self) -> list[int]:
        return self._years.copy()

    # Getter for the first year the model was produced.
    @property
    def first_year(self) -> int:
        return self._years[0]

# Return the model information as a formatted string.
    def __str__(self) -> str:
        return f"{self._name} in production = {self._in_production}, release year: {self.first_year}"