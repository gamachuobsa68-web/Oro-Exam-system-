from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label


class AdminScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            Label(text="Admin Dashboard")
        )