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


def elena_main_screen():
    label = Elena()
    label.run()

elena_main_screen()