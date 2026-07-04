from core.db import init_db


class AppMain(App):

    def build(self):

        init_db()   # 🔥 IMPORTANT

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(TeacherScreen(name="teacher"))
        sm.add_widget(AdminScreen(name="admin"))
        sm.add_widget(ExamScreen(name="exam"))
        sm.add_widget(LeaderboardScreen(name="leaderboard"))

        sm.current = "login"

        return sm