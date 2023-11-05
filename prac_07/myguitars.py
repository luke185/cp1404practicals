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
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))

    guitars.sort()

    print('These are my guitars:')
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} "
              f"{'(vintage)' if guitar.is_vintage() else ''}")


main()
