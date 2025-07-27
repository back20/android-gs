
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from app.screens.main_screen import MainScreen
from app.screens.record_screen import RecordScreen

class WorktimeApp(MDApp):
    def build(self):
        self.title = "工时表格生成器"
        Window.softinput_mode = 'below_target'
        self.theme_cls.primary_palette = "Blue"
        Builder.load_file("app/ui/main_screen.kv")
        Builder.load_file("app/ui/record_screen.kv")
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(RecordScreen(name="record"))
        return sm

if __name__ == '__main__':
    WorktimeApp().run()
