from car import Car
from random import randint


class UnreliableCar(Car):
    """Represent a UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        Car also needs to roll a number that is lower than it's reliability to start.
        """
        if randint(0, 100) >= self.reliability:
            distance = 0
            return distance

        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance
