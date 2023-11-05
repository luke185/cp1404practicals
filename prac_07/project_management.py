"""
CP1404 Prac 07 - project_management.py
Estimated time: 60m
Actual time:
"""
import datetime
from project import Project

MENU = '- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n' \
       '- (A)dd new project\n- (U)pdate project\n- (Q)uit'


def main():
    projects = load_projects('projects.txt')
    print(MENU)
    choice = input('> ').upper()
    while choice != 'Q':
        if choice == 'L':
            pass
        if choice == 'S':
            pass
        if choice == 'D':
            pass
        if choice == 'F':
            pass
        if choice == 'A':
            pass
        if choice == 'U':
            pass
        else:
            print('Invalid Input')
        choice = input('> ').upper()
    print('Thanks : )')


def load_projects(filename):
    projects = []
    return projects


main()
