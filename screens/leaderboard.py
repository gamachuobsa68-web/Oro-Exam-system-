from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

try:
    from core.db import get_results
except:
    def get_results():
        return [
            ("Student 1", 95),
            ("Student 2", 90),
            ("Student 3", 85),
        ]


class LeaderboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.title = Label(
            text="🏆 LEADERBOARD",
            font_size=28,
            size_hint=(1, 0.15)
        )

        self.layout.add_widget(self.title)

        self.score_box = BoxLayout(
            orientation="vertical"
        )

        self.layout.add_widget(self.score_box)

        self.back = Button(
            text="Back",
            size_hint=(1, 0.15)
        )

        self.back.bind(on_press=self.go_back)

        self.layout.add_widget(self.back)

        self.add_widget(self.layout)

    def on_enter(self):
        self.score_box.clear_widgets()

        results = get_results()

        rank = 1

        for student, score in results:

            lbl = Label(
                text=f"{rank}. {student}   ----   {score}",
                font_size=20
            )

            self.score_box.add_widget(lbl)

            rank += 1

    def go_back(self, instance):
        self.manager.current = "dashboard"