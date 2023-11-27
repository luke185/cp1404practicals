"""
CP1404 Prac 6 - Languages.py
Estimated time: 10m
Actual time: 15m
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    languages = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
                 ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                 ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

    display_dynamic(languages)


def display_dynamic(languages):
    """Display all the dynamically typed languages"""
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
