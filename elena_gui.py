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
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import os

# for opengl error
os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

Config.set("graphics", "resizable", True)


class Elena(App):
    def build(self):

        return Label(
            text="Hello i Am Elena!!",
            color=[0.41, 0.42, 0.74, 1],
            font_size="60sp",
            font_name="fonts/Roboto-Regular.ttf",
        )

    def build(self):
        return Image(source="elena.jpg")


if __name__ == "__main__":
    Elena().run()
