import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random


class Screen(BoxLayout):
    orientation = 'vertical'
    font_size = 30
    totaldigits = 0
    max_digits = ''

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        line1 = Label(text="Max digits", font_size=self.font_size)
        self.add_widget(line1)
        user_input1 = TextInput(multiline=False, font_size=self.font_size)
        self.add_widget(user_input1)
        user_input1.bind(on_text_validate=self.callback1)
        line2 = Label(text="Total numbers", font_size=self.font_size)
        self.add_widget(line2)
        user_input2 = TextInput(multiline=False, font_size=self.font_size)
        self.add_widget(user_input2)
        user_input2.bind(on_text_validate=self.callback2)
        line3 = Label(text="1 for +, 2 for +&-", font_size=self.font_size)
        self.add_widget(line3)
        user_input3 = TextInput(multiline=False, font_size=self.font_size)
        self.add_widget(user_input3)
        user_input3.bind(on_text_validate=self.callback3)

    def callback1(self, user_input1):

        temp = ''


        for x in range(1, int(user_input1.text) + 1):
            temp += '9'
        self.max_digits = int(temp)

        print(self.max_digits)

    def callback2(self, user_input2):
        self.totaldigits = int(user_input2.text)
        print(self.totaldigits)

    def callback3(self, user_input3):


        signs = []

        if user_input3.text == "1":
            signs.append("+")
        elif user_input3.text == "2":
            signs.append("+")
            signs.append("-")
        print(signs)

        list_of_numbers = []
        for x in range(self.totaldigits+1):
            list_of_numbers.append(f'{random.choice(signs)}{random.randint(1, self.max_digits)}')
        print(list_of_numbers)
        str_list_of_numbers = '\n'.join(list_of_numbers)

        sum = 0
        for num in list_of_numbers:
            sum += int(num)
        print(sum)

        self.clear_widgets()
        line4 = Label(text=str_list_of_numbers, font_size=self.font_size)
        self.add_widget(line4)
        line5 = Label(text=str(sum), font_size=self.font_size)
        self.add_widget(line5)





    def callback(self, instance):
        print('The button %s state is <%s>' % (instance, instance.state))


class MyApp(App):

    def build(self):
        return Screen()


if __name__ == '__main__':
    MyApp().run()
