from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from core.auth import login_user


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.title = Label(
            text="🎓 ORO EXAM LOGIN",
            font_size=26,
            size_hint=(1, 0.2)
        )

        self.role = Spinner(
            text="student",
            values=("student", "teacher", "admin")
        )

        self.username = TextInput(
            hint_text="Username",
            multiline=False
        )

        self.password = TextInput(
            hint_text="Password",
            password=True,
            multiline=False
        )

        self.message = Label(text="")

        btn = Button(
            text="LOGIN",
            size_hint=(1, 0.2)
        )

        btn.bind(on_press=self.check_login)

        layout.add_widget(self.title)
        layout.add_widget(self.role)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(btn)
        layout.add_widget(self.message)

        self.add_widget(layout)

    def check_login(self, instance):

        ok = login_user(
            self.role.text,
            self.username.text,
            self.password.text
        )

        if ok:

            self.message.text = "Login Successful ✔"

            if self.role.text == "student":
                self.manager.current = "dashboard"

            elif self.role.text == "teacher":
                self.manager.current = "teacher"

            elif self.role.text == "admin":
                self.manager.current = "admin"

        else:
            self.message.text = "Invalid username or password ❌"