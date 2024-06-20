import flet as ft

from helpers.database import ConnectDB


def actions():
    return ft.Container(content=ft.Column(controls=[
        ft.TextField(label="Buscar"),
        ft.TextButton(text="Agregar Producto")
    ]))


def list_data(db: ConnectDB):
    # Se realiza la conección a la bas de datos sqlite3
    db = ConnectDB()

    # Se ejecuta el comando SQL, para obtener la lista de productos
    products = db.execute("SELECT * FROM producto;")

    list_view = ft.ListView(expand=1, spacing=30, padding=10, auto_scroll=True)

    # Se renderiza cada uno de los productos
    for product in products:
        unit = product[5] + '(es)' if product[5] == 'unidad' else product[5]
        stock = f"Stock: {product[3]} {unit}"
        list_view.controls.append(
            ft.Container(ft.Column(controls=[
                ft.Text(product[1], size=20),
                ft.Text(f"Precio: S/. {product[2]}"),
                ft.Text(stock),
                ft.Text(f"Descripción: {product[4]}")
            ]),
                border=ft.border.all(1, '#333333'))
        )

    return list_view


def inventory_view(page: ft.Page):
    return [
        actions(),
        list_data()
    ]
