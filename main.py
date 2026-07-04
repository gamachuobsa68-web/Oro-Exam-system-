from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen

class OroExamSystem(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))

        return sm

if __name__ == "__main__":
    OroExamSystem().run()