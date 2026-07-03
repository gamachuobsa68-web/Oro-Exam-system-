from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.admin import AdminScreen
from screens.teacher import TeacherScreen
from screens.student import StudentScreen
from screens.exam import ExamScreen


class ExamApp(App):
    def build(self):
        Builder.load_file("main.kv")

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(TeacherScreen(name="teacher"))
        sm.add_widget(StudentScreen(name="student"))
        sm.add_widget(ExamScreen(name="exam"))

        sm.current = "login"
        return sm


if __name__ == "__main__":
    ExamApp().run()