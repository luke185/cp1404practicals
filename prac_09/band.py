class Band:
    """Represent a Band object"""

    def __init__(self, name: str):
        """Construct a Band"""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Display a Band"""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a new musician to the Band list"""
        self.musicians.append(musician)

    def play(self):
        """Make each musician in the Band list play"""
        play_string = [musician.play() for musician in self.musicians]
        return '\n'.join(play_string)
