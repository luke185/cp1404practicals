"""
CP1404 Prac 07 - myguitars.py
Estimated time: 15m
Actual time:
"""
import csv
from guitar import Guitar


def main():
    guitars = []

    with open('guitars.csv', 'r') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))

    display_guitars(guitars)

    print("Add new guitars. Leave blank to finish.")
    name = input('Name: ')
    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        guitars.append(Guitar(name, year, cost))
        name = input('Name: ')

    display_guitars(guitars)

    with open('guitars.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    guitars.sort()
    print('These are my guitars:')
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} "
              f"{'(vintage)' if guitar.is_vintage() else ''}")


main()
