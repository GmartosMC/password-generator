# Generador de contraseñas seguras

# Importamos las librerías necesarias

import secrets # Para la aleatoriedad con un algoritmo seguro
import string # Para los caracteres
import flet as ft # Para la GUI

# Caja que guarda la Password
password_field = ft.TextField(
    read_only=True,
    width=1000,
    text_align=ft.TextAlign.LEFT,
    text_style=ft.TextStyle(
        size=20,
        weight=ft.FontWeight.BOLD,
        font_family="serif"
    )
)

# Función para generar la contraseña
def password_generation(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase

    if use_uppercase == True:
        characters += string.ascii_uppercase
    if use_numbers == True:
        characters += string.digits
    if use_symbols == True:
        characters += string.punctuation

    return "".join(secrets.choice(characters) for i in range(length))

def main(page: ft.Page):
    page.title = "Password Generator"

    title = ft.Text("Password Generator", size=30, weight=ft.FontWeight.BOLD)

    # Switches
    switch_upper = ft.Switch(label="Uppercase", value=True)
    switch_numbers = ft.Switch(label="Numbers", value=True)
    switch_symbols = ft.Switch(label="Symbols", value=True)

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
        password_field.value = password_generation(
        int(e.control.value),
        switch_upper.value,
        switch_numbers.value,
        switch_symbols.value
        )
        page.update()

    # Handler para el botón
    def on_generate_click(e):
        password_field.value = password_generation(
        int(slider.value),
        switch_upper.value,
        switch_numbers.value,
        switch_symbols.value
        )
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

    switch_upper.on_change = lambda e: on_generate_click(e)
    switch_numbers.on_change = lambda e: on_generate_click(e)
    switch_symbols.on_change = lambda e: on_generate_click(e)
    
    button = ft.ElevatedButton(
        "Regenerate",
        on_click = on_generate_click,
        icon = ft.Icons.RESTART_ALT 
        )

    copy_button = ft.ElevatedButton(
        "Copy to Clipboard",
        on_click = on_copy_click,
        icon = ft.Icons.COPY
    )

    # Password de inicio
    password_field.value = password_generation(
    int(slider.value),
    switch_upper.value,
    switch_numbers.value,
    switch_symbols.value
    )

    # Añadimos todo a la interfaz
    page.add(
        title,
        password_field,
        ft.Text("Password Length:", size=20, weight=ft.FontWeight.BOLD),
        slider,
        ft.Row([switch_upper, switch_numbers, switch_symbols]),

        button,
        copy_button
    )

ft.app(target=main)
