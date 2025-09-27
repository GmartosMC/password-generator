# Generador de contraseñas seguras

# Importamos las librerías necesarias
import secrets # Para la aleatoriedad
import string # Para los caracteres
import flet as ft # Para la GUI

# Guardamos en una variable todos los tipos de caracteres que necesitamos
characters = string.ascii_letters + string.digits + string.punctuation
print(characters)

