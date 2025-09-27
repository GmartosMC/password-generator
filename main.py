# Generador de contraseñas seguras

# Importamos las librerías necesarias
import secrets # Para la aleatoriedad
import string # Para los caracteres
import flet as ft # Para la GUI

# La caja que guarda la Password
password_field = ft.TextField(
        read_only=True,
        width=400,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD)
    )

# Función Main
def main(page: ft.Page):
    
    # El título
    page.title = "Password Generator"
    title = ft.Text("Password Generator", size=30, weight=ft.FontWeight.BOLD)

    # Generamos el botón
    button = ft.ElevatedButton("Generate Password", on_click=update_password)

    # Añadimos a la interfaz todo para mostrarlo
    page.add(title, password_field, button)

# Función para actualizar la contraseña
def update_password(e):
    password_field.value = password_generation()
    e.page.update() # Actualizar solo el cambio

# La función para generar la contraseña aleatoria
def password_generation(length = 8):

    # Guardamos en una variable todos los tipos de caracteres que necesitamos
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(secrets.choice(characters) for i in range (length))
    return password

# Llamamos al Main
ft.app(target=main)
