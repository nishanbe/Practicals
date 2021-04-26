from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Nishan Bedrossian'
KMS_IN_MILE = 1.60934


class ConvertMilesKmApp(App):
    message = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def convert(self):
        """Convert form miles to Kilometres after validating entry"""
        m = self.validate_input()
        result = m * KMS_IN_MILE
        self.message = str(result)

    def validate_input(self):
        """Validate user entry as digits entry otherwise change output to 0"""
        try:
            value = float(self.root.ids.input_text.text)
            # print("Input is an float number. Number = ", value)
            return value
        except ValueError:
            # print("Error")
            return 0

    def handle_change(self, change):
        """Automatically validate and calculate as user types entry"""
        result = self.validate_input() + change
        self.root.ids.input_text.text = str(result)
        self.convert()


ConvertMilesKmApp().run()
