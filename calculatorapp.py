import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# class Screen(BoxLayout):
#     fontsize = 40
#
#     def __init__(self, **kwargs):
#         super(Screen, self).__init__(**kwargs)

class CalcApp(App):
    def build(self):

        user_input = TextInput(font_size=40, text='', multiline=False, size_hint=(1, None), pos_hint={'center_y': .7})

        over_all_layout = BoxLayout(orientation='vertical')
        over_all_layout.add_widget(user_input)
        user_input.bind(on_text_validate=self.on_enter)

        buttons_layout = GridLayout(cols=4, row_force_default=True, row_default_height=50,
                                    pos_hint={'center_x':.5}, size_hint=(1, 1))


        list1 = ['7', '8', '9', 'Del', '4', '5', '6', '/', '1', '2', '3', '-', '0', '.', '+', '=']

        for x in list1:
            buttons_layout.add_widget(Button(text=str(x), font_size=40))


        over_all_layout.add_widget(buttons_layout)

        return over_all_layout



    def on_enter(self, value):
        pass


    def longpressed(self,button):
        pass


    def edit_func(self, object):
        pass


    def remove_func(self, object):
        pass


CalcApp().run()


# class MyApp(App):
#
#     def build(self):
#         return Screen()
#
#
# if __name__ == '__main__':
#     MyApp().run()
