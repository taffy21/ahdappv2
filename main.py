from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, ListProperty, NumericProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.button import Button
from kivy.clock import Clock
import qns

class SelectableButton(RecycleDataViewBehavior, Button):
    index = None
    data = ObjectProperty()

    def refresh_view_attrs(self, rv, index, data):
        self.index = index
        self.data = data
        return super().refresh_view_attrs(rv, index, data)
    def on_touch_down(self, touch):

        if super().on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

class MyRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class WindowManager(ScreenManager):
    pass


class Loading(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.switch_screen, 2)

    def switch_screen(self, dt):
        self.manager.current = "login"

class Login(Screen):
    pass

class Register(Screen):
    pass
class Contents(Screen):
    """insert functions """
    pass

class MyQuiz(Screen):
    quiz_number = NumericProperty()
    next_question = StringProperty()
    quiz = qns.Quizzes

class FinalScore(Screen):
    score = NumericProperty(0)


class Completed(Screen):
    pass



class AdvancedHIVApp(App):
    pass


if __name__ == "__main__":
    AdvancedHIVApp().run()
