from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


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
        self.output = str(float(self.root.ids.miles_input.text) * 1.6)

    def handle_increment(self, increment):
        self.root.ids.miles_input.text = str(float(self.root.ids.miles_input.text) + increment)


ConvertMilesToKM().run()
