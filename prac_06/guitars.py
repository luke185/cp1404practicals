"""
CP1404 Prac 06 - guitars.py
Estimated time: 15m
Actual time: 17m
"""
from guitar import Guitar


def main():
    """Add a user's guitars to a list"""
    guitars = []
    print('My guitars!')
    name = input('Name: ')
    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        guitars.append(Guitar(name, year, cost))
        name = input('Name: ')
    print('These are my guitars:')
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} "
              f"{'(vintage)' if guitar.is_vintage() else ''}")


main()
