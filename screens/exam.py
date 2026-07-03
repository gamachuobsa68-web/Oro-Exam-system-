from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from data.questions import QUESTIONS
from core.db import init_db, save_result


class ExamScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        init_db()

        self.index = 0
        self.score = 0

        self.layout = BoxLayout(orientation="vertical", padding=20)

        self.q = Label(text="")
        self.layout.add_widget(self.q)

        self.buttons = []

        for i in range(4):
            b = Button()
            b.bind(on_press=self.check)
            self.buttons.append(b)
            self.layout.add_widget(b)

        self.add_widget(self.layout)

        self.load()

    def load(self):
        q = QUESTIONS[self.index]

        self.q.text = q["q"]

        for i, opt in enumerate(q["options"]):
            self.buttons[i].text = opt

    def check(self, instance):
        if instance.text == QUESTIONS[self.index]["answer"]:
            self.score += 1

        self.index += 1

        if self.index < len(QUESTIONS):
            self.load()
        else:
            save_result("student1", self.score, len(QUESTIONS))
            self.manager.current = "leaderboard"