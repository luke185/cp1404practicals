"""CP1404 Prac 6 - ProgrammingLangauge class"""


class ProgrammingLanguage:
    """Represent a programming langauge"""

    def __init__(self, name='', typing='', reflection=True, year=0):
        """Initialise a programming langauge instance"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Represent a Programming Language as a string"""
        return f"{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """return if the programming langauge is dynamically typed or not"""
        return self.typing == 'Dynamic'
