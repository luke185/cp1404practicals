from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATIO = 1.6


class ConvertMilesToKM(App):
    """Convert Miles to KM from user input"""
    output = StringProperty()

    def build(self):
        """Build the app"""
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output = '54.71756'
        return self.root

    def handle_convert(self):
        """Convert user inputted Miles to KM"""
        try:
            self.output = str(float(self.root.ids.miles_input.text) * CONVERSION_RATIO)
        except ValueError:
            self.output = '0.0'

    def handle_increment(self, increment):
        """Change input field by given increment"""
        try:
            self.root.ids.miles_input.text = str(float(self.root.ids.miles_input.text) + increment)
        except ValueError:
            self.root.ids.miles_input.text = str(0 + increment)


ConvertMilesToKM().run()
