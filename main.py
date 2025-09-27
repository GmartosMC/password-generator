# Generador de contraseñas seguras

import secrets
import string
import flet as ft

# Caja que guarda la Password
password_field = ft.TextField(
    read_only=True,
    width=1000,
    text_align=ft.TextAlign.LEFT,
    text_style=ft.TextStyle(
        size=17,
        weight=ft.FontWeight.BOLD,
        font_family="serif"
    )
)

def password_generation(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for i in range(length))

def main(page: ft.Page):
    page.title = "Password Generator"

    title = ft.Text("Password Generator", size=30, weight=ft.FontWeight.BOLD)

    # Slider
    slider = ft.Slider(
        min=8,
        max=64,
        divisions=56,
        label="{value}",
        value=12
    )

    # Handler para cambios del slider
    def on_slider_change(e):
        password_field.value = password_generation(int(e.control.value))
        page.update()

    # Handler para el botón
    def on_generate_click(e):
        password_field.value = password_generation(int(slider.value))
        page.update()

    # Handler para copiar al portapapeles
    def on_copy_click(e):
        # copiar
        page.set_clipboard(password_field.value)
        snack_bar = ft.SnackBar(ft.Text("Password Copied to the Clipboard"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    # Asignamos handlers
    slider.on_change = on_slider_change
    button = ft.ElevatedButton("Generate Password", on_click=on_generate_click)
    copy_button = ft.ElevatedButton(
        "Copy to Clipboard",
        on_click=on_copy_click,
        icon=ft.Icons.COPY
    )

    # Password de inicio
    password_field.value = password_generation(int(slider.value))

    # Añadimos todo a la interfaz
    page.add(
        title,
        password_field,
        ft.Text("Password Length:", size=20, weight=ft.FontWeight.BOLD),
        slider,
        button,
        copy_button
    )

ft.app(target=main)
