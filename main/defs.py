from datetime import timedelta
import flet as ft


def main(page: ft.Page):
    page.title = 'Flet counter example'
    page.vertical_alignment = 'center'
    result = ft.Text(value="0")

    page.add(
        ft.Row(controls=[result]),
        ft.Row(controls=[
            ft.TextField(label='Enter min press'),
            ft.ElevatedButton(text='Enter')

        ],
            alignment='center'
        ),
        ft.Row(controls=[
            ft.TextField(label='Enter Hours'),
            ft.ElevatedButton(text='Enter')

        ],
            alignment='center'
        ),
        ft.Row(controls=[
            ft.TextField(label='Enter minutes'),
            ft.ElevatedButton(text='Enter')

        ],
            alignment='center'
        )
    )


ft.app(target=main, view=ft.WEB_BROWSER)





def calculator():
    press_min = int(input('Введите минимальное давление при включении:'))
    time_now = timedelta(hours=int(input('час: ')), minutes=(int(input('минуты: '))))
    max_press_drop = round(press_min / 3)
    press_ctrl_exit = press_min - max_press_drop
    delta_time = timedelta(minutes=(round(max_press_drop * 6.8 / 45)))
    total_time = timedelta(minutes=(round(press_min * 6.8 / 45)))
    time_on_exit = time_now + delta_time
    comeback_time = time_now + total_time
    return f' Pmax.пад = {max_press_drop}, Рк.вых =  {press_ctrl_exit}, Дельта Т = {delta_time}, Тобщ = {total_time}, Т вых = {time_on_exit}, Т возвр = {comeback_time}'
print(calculator())

