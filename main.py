import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_counter = ft.Text(
        value="0",
        size=100,
        width=200,
        text_align=ft.TextAlign.CENTER,
    )

    def minus_click(e):
        text_counter.value = str(int(text_counter.value) - 1)

    def plus_click(e):
        text_counter.value = str(int(text_counter.value) + 1)

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                text_counter,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
        )
    )
ft.run(main)