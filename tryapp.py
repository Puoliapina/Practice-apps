import kivy
import appwebscraping
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.boxlayout import BoxLayout
from functools import partial

class TestApp(App):
    def build(self):
        def callback(instance, city):
            print('The button <%s> is being pressed' % instance.text)
            instance.text = appwebscraping.country_weather(city).replace("\t", "      ")

        # return a Button() as a root widget
        layout = BoxLayout(orientation='vertical')
        butn1 = Button(text='Helsinki', font_size=30)
        butn2 = Button(text='Osaka', font_size=30)
        butn3 = Button(text='Sultanpur', font_size=30)
        butn4 = Button(text='Mumbai', font_size=30)

        layout.add_widget(butn1)
        layout.add_widget(butn2)
        layout.add_widget(butn3)
        layout.add_widget(butn4)

        butn1.bind(on_press=partial(callback, city='Helsinki'))
        butn2.bind(on_press=partial(callback, city='Osaka'))
        butn3.bind(on_press=partial(callback, city='Sultanpur'))
        butn4.bind(on_press=partial(callback, city='Mumbai'))
        return layout


if __name__ == '__main__':
    TestApp().run()

# Button(text= webscraping.r1.replace("\t", "      "), font_size=30)