from enum import Enum


@unique
class Ship(Enum):
    AIRCRAFT_CARRIER = 1
    BATTLESHIP = 2
    SUBMARINE = 3
    DESTROYER = 4
