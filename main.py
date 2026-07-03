from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.exam import ExamScreen
from screens.leaderboard import LeaderboardScreen


class ExamApp(App):
    def build(self):
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ExamScreen(name="exam"))
        sm.add_widget(LeaderboardScreen(name="leaderboard"))

        return sm


if __name__ == "__main__":
    ExamApp().run()