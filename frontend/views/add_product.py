import flet as ft

from helpers.database import ConnectDB


def add_product_view(page: ft.Page):
    def add(e):
        with ConnectDB() as db:
            db.execute(
                f"""INSERT INTO producto (nombre, precio, stock, descripcion, medida) VALUES (?, ?, ?, ?, ?);""",
                (name.value, int(stock.value), float(price.value), description.value, unit.value))

        name.value = ""
        stock.value = ""
        price.value = ""
        description.value = ""
        unit.value = ""
        page.update()

    name = ft.TextField(label='Nombre')
    stock = ft.TextField(label='Stock')
    price = ft.TextField(label='Precio')
    description = ft.TextField(label='Descripción')
    unit = ft.TextField(label='Medida')

    return [
        name,
        stock,
        price,
        description,
        unit,
        ft.ElevatedButton(text='Agregar', on_click=add, style=ft.ButtonStyle(
            bgcolor='#98A124',
            color='#000000'
        ))
    ]
