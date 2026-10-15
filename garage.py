from vehicle import Vehicle

class Garage: 
    """ garage that stores a collection of vehicles."""

    def __init__(self):
        self._vehicles: list[Vehicle] = []
    

    @property
    def vehicles(self) -> list[Vehicle]:
        # defensive copy
        return list(self._vehicles)

    # add_vehicle(vehicle)	Appends a Vehicle to the list. Returns None.
    def add_vehicle(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    # empty_garage()	Clears the list using the list's .clear() method (do not set the list to None). Returns None.
    def empty_garage(self) -> None:
        self._vehicles.clear()

    # sort_by_release_year()	Sorts _vehicles in place (you may simply call self._vehicles.sort()).
    def sort_by_release_year(self) -> None:
        self._vehicles.sort()

    # __str__	Returns each vehicle on its own line.
    def __str__(self):
        # creates empty string and joins each of the vehicles as a string by iterating
        # through each of the vehicles
        return "\n".join(str(v) for v in self._vehicles)