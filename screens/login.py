from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.user = TextInput(hint_text="Student ID")
        btn = Button(text="Login")

        btn.bind(on_press=self.go)

        layout.add_widget(self.user)
        layout.add_widget(btn)

        self.add_widget(layout)

    def go(self, instance):
        self.manager.current = "dashboard"