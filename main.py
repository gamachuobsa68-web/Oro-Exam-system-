from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from core.db import init_db

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.teacher import TeacherScreen
from screens.admin import AdminScreen
from screens.exam import ExamScreen
from screens.leaderboard import LeaderboardScreen


class AppMain(App):

    def build(self):

        init_db()

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(TeacherScreen(name="teacher"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(ExamScreen(name="exam"))
        sm.add_widget(LeaderboardScreen(name="leaderboard"))

        sm.current = "login"

        return sm


if __name__ == "__main__":
    AppMain().run()
