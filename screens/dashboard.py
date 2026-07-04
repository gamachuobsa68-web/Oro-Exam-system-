from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        layout.add_widget(Button(text="Start Exam"))
        layout.add_widget(Button(text="My Results"))
        layout.add_widget(Button(text="Leaderboard"))
        layout.add_widget(Button(text="Logout"))

        self.add_widget(layout)