from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy_garden.mapview import MapView

Window.size = (375, 812)


class MainWindow(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.switch_to_home, 5)

    def switch_to_home(self, dt):
        self.manager.current = 'Second'


class SecondWindow(MDScreen):
    pass


class LoginWindow(MDScreen):
    pass


class WelcomeScreen(MDScreen):
    pass


class HomeScreen(MDScreen):
    pass


class WindowManager(MDScreenManager):
    pass


class MyMainApp(MDApp):
    def build(self):
        kv = Builder.load_file("my.kv")
        LabelBase.register(name='DMSans_med', fn_regular='fonts/DMSans-Medium.ttf')
        LabelBase.register(name='DMSans_reg', fn_regular='fonts/DMSans-Regular.ttf')
        return kv


if __name__ == "__main__":
    MyMainApp().run()
