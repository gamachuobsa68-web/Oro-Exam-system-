from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        exam_btn = Button(text="Start Exam")
        board_btn = Button(text="Leaderboard")

        exam_btn.bind(on_press=lambda x: self.go("exam"))
        board_btn.bind(on_press=lambda x: self.go("leaderboard"))

        layout.add_widget(exam_btn)
        layout.add_widget(board_btn)

        self.add_widget(layout)

    def go(self, screen):
        self.manager.current = screen