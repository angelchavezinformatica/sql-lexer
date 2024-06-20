import flet as ft

# from .views.inventory import inventory_view
from .views.add_product import add_product_view


def main(page: ft.Page):
    page.title = "Inventory Manager"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.ARROW_BACK),
        leading_width=40,
        title=ft.Text("Agregar Producto", size=25, weight=ft.FontWeight.BOLD),
        bgcolor='#98A124'
    )

    page.add(
        ft.SafeArea(content=ft.Column(controls=[
            # *inventory_view(page),
            *add_product_view(page)
        ]))
    )
