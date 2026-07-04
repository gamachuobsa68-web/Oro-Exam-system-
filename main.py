from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.teacher import TeacherScreen
from screens.admin import AdminScreen


class AppMain(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(TeacherScreen(name="teacher"))
        sm.add_widget(AdminScreen(name="admin"))

        sm.current = "login"

        return sm


if __name__ == "__main__":
    AppMain().run()