from core.db import get_results
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class LeaderboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", padding=20)

        self.title = Label(text="🏆 Leaderboard", font_size=30)

        self.layout.add_widget(self.title)

        self.box = BoxLayout(orientation="vertical")

        self.layout.add_widget(self.box)

        self.add_widget(self.layout)

    def on_enter(self):

        self.box.clear_widgets()

        results = get_results()

        rank = 1

        for student, score, total in results:

            self.box.add_widget(
                Label(text=f"{rank}. {student} - {score}/{total}")
            )

            rank += 1