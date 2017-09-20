from kivy.app import App
from kivy.lang  import  Builder
from kivy.uix.label import Label

class ListNames(App):
    def build(self):
        self.title = "List Names"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.list_names()
        return self.root

    def list_names(self):
        names = ["where", "is", "my", "dad"]
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)


ListNames().run()
