#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
#os.environ['KIVY_TEXT'] = 'sdl2'
import kivy
kivy.require('1.9.1') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from longpress import LongpressButton
from kivy.storage.jsonstore import JsonStore


class Screen(BoxLayout):
    task_count = 5
    orientation = 'vertical'
    fontsize = 40
    todolist = []

    store = JsonStore('todo.json')

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        title=Label(text="I am gonna do...", font_size=30)
        self.add_widget(title)
        for i in range(self.task_count):
            if self.store.exists(str(i)):
                text = self.store.get(str(i))["text"]
                self.add_widget(LongpressButton(text=text,
                                        font_size=self.fontsize,
                                        on_long_press=self.longpressed,
                                        markup=True,
                                        long_press_time=0.3,
                                        id=str(i)
                                        ))
            else:
                user_input = TextInput(multiline=False, font_size=self.fontsize, id=str(i))
                self.add_widget(user_input)
                user_input.bind(on_text_validate=self.on_enter)
                self.todolist.append(user_input)




        edit_remove_layout = BoxLayout(orientation='horizontal')
        edit_button = Button(text="Edit", font_size=self.fontsize)
        remove_button = Button(text="Remove All", font_size=self.fontsize)
        edit_remove_layout.add_widget(edit_button)
        edit_button.bind(on_press=self.edit_func)
        edit_remove_layout.add_widget(remove_button)
        remove_button.bind(on_press=self.remove_func)

        self.add_widget(edit_remove_layout)


    def on_enter(self, value):
        self.remove_widget(value)
        self.add_widget(LongpressButton(text=value.text,
                                        font_size=self.fontsize,
                                        on_long_press=self.longpressed,
                                        markup=True,
                                        long_press_time=0.3,
                                        id=value.id
                                        ),
                        index=(self.task_count-int(value.id)))
        self.store.put(value.id, text=value.text)
        print(value.text)

    def longpressed(self,button):
        if '[s]' not in button.text:
            button.text = '[s][color=#458B00]' + button.text + '[/color][/s]'
        else:
            button.text = button.text[18:-12]
        print("pressed")



    def edit_func(self, object):
        # print(self.children)
        for child in self.children:
            if type(child) == LongpressButton:
                self.remove_widget(child)
                self.add_widget(TextInput(text=child.text,
                                          multiline=False,
                                          font_size=self.fontsize,
                                          id=child.id,
                                          on_text_validate=self.on_enter),
                                index=(self.task_count - int(child.id)))
                print(child.text)


    def remove_func(self, object):
        self.clear_widgets()
        self.store.clear()
        self.__init__()





class MyApp(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    MyApp().run()
