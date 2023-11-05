"""
CP1404 Prac 6 - Guitar Class
Estimated time: 15m  (includes testing and reading)
Actual time: 18m
"""
import datetime


class Guitar:
    def __init__(self, name='', year=0, cost=0.0):
        """Initialise a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        """Represent a Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Return how old the guitar is in years"""
        return (datetime.date.today()).year - self.year

    def is_vintage(self):
        """Return True if the guitar is >= 50 years old"""
        return self.get_age() >= 50
