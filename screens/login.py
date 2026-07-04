from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from core.auth import login


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        self.role = Spinner(
            text="student",
            values=("student", "teacher", "admin")
        )

        self.username = TextInput(
            hint_text="Username"
        )

        self.password = TextInput(
            hint_text="Password",
            password=True
        )

        btn = Button(text="Login")
        btn.bind(on_press=self.check_login)

        layout.add_widget(self.role)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(btn)

        self.add_widget(layout)

    def check_login(self, instance):

        ok = login(
            self.role.text,
            self.username.text,
            self.password.text
        )

        if ok:

            if self.role.text == "student":
                self.manager.current = "dashboard"

            elif self.role.text == "teacher":
                self.manager.current = "teacher"

            else:
                self.manager.current = "admin"