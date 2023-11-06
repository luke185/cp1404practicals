"""
CP1404 Prac 07 - project.py
"""
import datetime


class Project:
    def __init__(self, name='', start_date='', priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialise a project"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Represent a project"""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}," \
               f"completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Define how < comparisons should be handled"""
        return self.priority < other.priority

    def is_complete(self):
        """Return if a project is complete"""
        return self.completion_percentage == 100
