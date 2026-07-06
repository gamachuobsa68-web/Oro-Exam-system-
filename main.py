import os
import sys
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder

# Caasaa folder kee irraa dubbisuuf path dabaluu
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.db import connect_db
from data.questions import EXAM_QUESTIONS

class LoginScreen(Screen):
    def login_user(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()
        
        if not username or not password:
            self.ids.error_msg.text = "Maaloo falanqa hunda guuti!"
            return
            
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            role = user[0]
            self.ids.error_msg.text = ""
            App.get_running_app().current_user = username
            if role == 'student':
                self.manager.current = 'student_dashboard'
            elif role == 'teacher':
                self.manager.current = 'teacher_dashboard'
        else:
            self.ids.error_msg.text = "Maqaa ykn Jecha Icchitii dogoggora!"

class StudentDashboard(Screen):
    pass

class ExamScreen(Screen):
    def on_pre_enter(self):
        self.questions = EXAM_QUESTIONS.get("Afaan Oromoo", [])
        self.current_index = 0
        self.score = 0
        self.selected_answer = None
        self.ids.action_btn.text = "Ewugi"
        self.ids.action_btn.disabled = True
        self.load_question()

    def load_question(self):
        if self.current_index < len(self.questions):
            q_data = self.questions[self.current_index]
            self.ids.question_text.text = f"Gaaffii {self.current_index + 1}: {q_data['q']}"
            self.ids.options_box.clear_widgets()
            self.selected_answer = None
            self.ids.action_btn.disabled = True
            
            for option in q_data["o"]:
                btn = Button(text=option, size_hint_y=None, height=50)
                btn.bind(on_press=self.select_option)
                self.ids.options_box.add_widget(btn)
        else:
            self.save_score()
            self.ids.question_text.text = f"Qormaata xumurteetta!\nQabxiin kee: {self.score} / {len(self.questions)}"
            self.ids.options_box.clear_widgets()
            self.ids.action_btn.text = "Gara Idoo Jalqabaa"
            self.ids.action_btn.disabled = False

    def select_option(self, instance):
        for child in self.ids.options_box.children:
            child.background_color = [1, 1, 1, 1]
        instance.background_color = [0.2, 0.6, 1, 1]
        self.selected_answer = instance.text
        self.ids.action_btn.disabled = False

    def next_question(self):
        if self.current_index < len(self.questions):
            correct = self.questions[self.current_index]["a"]
            if self.selected_answer == correct:
                self.score += 1
            self.current_index += 1
            self.load_question()
        else:
            self.manager.current = 'student_dashboard'

    def save_score(self):
        username = App.get_running_app().current_user
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (username, subject, score, total) VALUES (?, ?, ?, ?)",
                       (username, "Afaan Oromoo", self.score, len(self.questions)))
        conn.commit()
        conn.close()

class TeacherDashboard(Screen):
    def on_enter(self):
        self.load_scores()

    def load_scores(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT username, subject, score, total FROM scores")
        rows = cursor.fetchall()
        conn.close()
        
        if rows:
            display_text = ""
            for row in rows:
                display_text += f"Barataa: {row[0]} | Akaakuu: {row[1]} | Qabxii: {row[2]}/{row[3]}\n"
            self.ids.scores_list.text = display_text
        else:
            self.ids.scores_list.text = "Qabxiin galmeeffame hin jiru."

class ExamApp(App):
    current_user = ""
    def build(self):
        self.title = "Oro Exam System"
        # main.kv akka ofiin dubbisu gochuuf
        Builder.load_file('main.kv')
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(StudentDashboard(name='student_dashboard'))
        sm.add_widget(ExamScreen(name='exam'))
        sm.add_widget(TeacherDashboard(name='teacher_dashboard'))
        return sm

if __name__ == '__main__':
    ExamApp().run()