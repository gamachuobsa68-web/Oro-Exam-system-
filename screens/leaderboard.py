from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from core.db import get_results


class LeaderboardScreen(Screen):
    def on_enter(self):
        self.clear_widgets()

        data = get_results()

        text = "🏆 LEADERBOARD\n\n"

        for d in data:
            text += f"{d[0]} - {d[1]}\n"

        self.add_widget(Label(text=text))