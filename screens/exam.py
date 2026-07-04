from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from data.questions import QUESTIONS
from core.logic import grade_exam
from core.db import save_result
from utils.pdf import generate_result_pdf


class ExamScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.index = 0
        self.answers = []

        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.question_label = Label(text="", font_size=20)

        self.option_buttons = []

        for i in range(4):
            btn = Button(text="")
            btn.bind(on_press=self.select_answer)
            self.option_buttons.append(btn)

        self.next_btn = Button(text="Next")
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

        q = QUESTIONS[self.index]

        self.question_label.text = f"{self.index+1}. {q['question']}"

        for i, opt in enumerate(q["options"]):
            self.option_buttons[i].text = opt

    # SELECT ANSWER
    def select_answer(self, instance):

        # overwrite answer for current question
        if len(self.answers) > self.index:
            self.answers[self.index] = instance.text
        else:
            self.answers.append(instance.text)

    # NEXT QUESTION
    def next_question(self, instance):

        if self.index < len(QUESTIONS) - 1:
            self.index += 1
            self.load_question()
        else:
            self.finish_exam()

    # ✅ FINAL FUNCTION (YOUR ASKED PART)
    def finish_exam(self):

        score, total = grade_exam(self.answers)

        # SAVE TO DATABASE
        save_result("Student", score, total)

        # GENERATE PDF RESULT
        generate_result_pdf("Student", score, total)

        # GO BACK TO DASHBOARD
        self.manager.current = "dashboard"