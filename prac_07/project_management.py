"""
CP1404 Prac 07 - project_management.py
Estimated time: 60m
Actual time:
"""
import datetime
from project import Project

MENU = '- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n' \
       '- (A)dd new project\n- (U)pdate project\n- (Q)uit'
DEFAULT_FILE = 'projects.txt'


def main():
    projects = load_projects(DEFAULT_FILE)
    print(MENU)
    choice = input('> ').upper()
    while choice != 'Q':
        if choice == 'L':
            filename = input('Filename: ')
            projects = load_projects(filename)
        elif choice == 'S':
            pass
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            pass
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            projects = update_project(projects)
        else:
            print('Invalid Input')
        choice = input('> ').upper()
    print('Thanks : )')


def load_projects(filename):
    """load a projects file and format it into a list of project objects"""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            line = line.strip().split('\t')
            projects.append(Project(line[0], line[1], int(line[2]), float(line[3]), int(line[4])))
    return projects


def display_projects(projects):
    """display all projects grouped by completion status"""
    projects.sort()
    print('Incomplete projects:  ')
    for project in projects:
        if project.completion_percentage < 100:
            print(project)
    print('Completed projects: ')
    for project in projects:
        if project.completion_percentage == 100:
            print(project)


def add_new_project(projects):
    """add a new project object to the list of projects"""
    name = input('Name: ')
    start = input('Start Date: ')
    priority = int(input('Priority: '))
    cost = float(input('Cost: '))
    percentage = int(input('Percentage: '))
    projects.append(Project(name, start, priority, cost, percentage))


def update_project(projects):
    """update a chosen project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input('Project choice: '))
    print(projects[choice])
    new_percentage = int(input('New percentage: '))
    projects[choice].completion_percentage = new_percentage
    new_priority = int(input('New priority: '))
    projects[choice].priority = new_priority
    return projects


main()
