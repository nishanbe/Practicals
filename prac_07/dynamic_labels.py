from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Main app."""
        super().__init__(**kwargs)
        self.names = ["Adam", "Sam", "Ben", "Victor"]

    def build(self):
        self.root = Builder.load_file("dynamic_labels.kv")
        self.title = "Dynamic Labels"
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries.add_widget(temp_label)


DynamicLabelsApp().run()
