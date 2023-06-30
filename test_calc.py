import flet
from flet import (Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius,colors, TextField)
from datetime import timedelta


class CalculatorApp(UserControl):



    def build(self):
        # self.reset()
        self.result = Text(value='0', color=colors.WHITE, size=20)


        return Container(
            width=500,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(10),
            padding=20,
            content=Column(
                controls=[
                    Row(controls=[self.result],alignment='end'),
                    Row(
                        controls=[
                            ElevatedButton(
                                text='min_press',
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='min_press',
                            ),
                            ElevatedButton(
                                text='hours',
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='hours',
                            ),
                            ElevatedButton(
                                text='minutes',
                                color=colors.BLACK,
                                expand=1,
                                on_click=self.button_clicked,
                                data='minutes'
                            )
                        ]
                    )

                ]
            )
        )

    def button_clicked(self):
        data = e.control.data
        if data in "min_press":
            self.press_min = self.result.value = self.calculator()
        if data in 'hours':
            self.result.value = self.calculator()
        if data in 'minutes':
            self.result.value = self.calculator()



    def calculator(self):
        press_min = int(input('Введите минимальное давление при включении:'))
        time_now = timedelta(hours=int(input('час: ')), minutes=(int(input('минуты: '))))
        max_press_drop = round(press_min / 3)
        press_ctrl_exit = press_min - max_press_drop
        delta_time = timedelta(minutes=(round(max_press_drop * 6.8 / 45)))
        total_time = timedelta(minutes=(round(press_min * 6.8 / 45)))
        time_on_exit = time_now + delta_time
        comeback_time = time_now + total_time
        return f' Pmax.пад = {max_press_drop}, Рк.вых =  {press_ctrl_exit}, Дельта Т = {delta_time}, Тобщ = {total_time}, Т вых = {time_on_exit}, Т возвр = {comeback_time}'

def main(page: Page):
    page.title = 'Calc App'

    calc = CalculatorApp()

    page.add(calc)

flet.app(target=main)