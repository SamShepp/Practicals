from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesToKm(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_conversion(self):
        result = self.get_validated_miles() * 1.609344
        self.root.ids.display_label.text = "{:.3f}".format(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_increment(self, increment):
        result = self.get_validated_miles() + increment
        self.root.ids.input_number.text = str(result)


ConvertMilesToKm().run()
