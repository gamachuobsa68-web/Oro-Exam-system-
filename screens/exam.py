from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

import random

from data.questions import QUESTIONS
from core.logic import grade_exam
from core.db import save_result
from utils.pdf import generate_result_pdf


class ExamScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.index = 0
        self.answers = {}

        # shuffle questions (PRO FEATURE)
        self.questions = QUESTIONS.copy()
        random.shuffle(self.questions)

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.question_label = Label(text="", font_size=22)

        self.option_buttons = []

        for i in range(4):
            btn = Button()
            btn.bind(on_press=self.select_answer)
            self.option_buttons.append(btn)

        self.next_btn = Button(text="NEXT ➡")
        self.next_btn.bind(on_press=self.next_question)

        self.layout.add_widget(self.question_label)

        for b in self.option_buttons:
            self.layout.add_widget(b)

        self.layout.add_widget(self.next_btn)

        self.add_widget(self.layout)

    # LOAD QUESTION
    def on_enter(self):
        self.load_question()

    def load_question(self):

        q = self.questions[self.index]

        self.question_label.text = f"{self.index+1}. {q['question']}"

        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].text = opt

    # SELECT ANSWER
    def select_answer(self, instance):

        self.answers[self.index] = instance.text

    # NEXT QUESTION
    def next_question(self, instance):

        if self.index < len(self.questions) - 1:
            self.index += 1
            self.load_question()
        else:
            self.finish_exam()

    # 🔥 FINAL PRO FUNCTION
    def finish_exam(self):

        score, total = grade_exam(self.answers, self.questions)

        student_name = "Student001"  # later we connect login user

        save_result(student_name, score, total)

        generate_result_pdf(student_name, score, total)

        self.manager.current = "dashboard"