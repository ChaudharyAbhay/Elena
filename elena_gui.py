from cProfile import label
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

import os

os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class Elena(App):
    def build(self):
        return Label(
            text="Hello i Am Elena!!",
            color=[0.41, 0.42, 0.74, 1],
            font_size="60sp",
        )

    # def build(self):
    #     btn = Button(
    #         text="this is a button",
    #         font_size="20sp",
    #         background_color=(0, 0, 0, 0),
    #         color=(1, 1, 1, 1),
    #         size=(32, 32),
    #         size_hint=(0.2, 0.2),
    #         pos_hint={"x": 0.5, "y": 0.5},
    #     )
    #     btn.bind(on_press=)
    #     return btn


class Elena_Login(App):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)

    def datas(self):
        email: email
        pwd: pwd
        label(text="Email: " + email, pos_hint={"x": 0.25, "top": 0.9})
        pass


def elena_main_screen():
    label = Elena()
    label.run()


def elena_login_screen():
    label = Elena_Login()
    label.run()


# elena_main_screen()

if __name__ == "__main__":
    elena_main_screen.run()
