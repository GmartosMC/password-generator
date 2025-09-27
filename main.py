# Generador de contraseñas seguras

# Importamos las librerías necesarias
import secrets # Para la aleatoriedad
import string # Para los caracteres
import flet as ft # Para la GUI

def main():

    # Preguntamos al usuario cuantos caracteres quiere
    long = int(input("Type the number of characters. Ej 8: "))
    password = password_generation(long)
    print(f"The password is: {password}")

def password_generation(long):

    # Guardamos en una variable todos los tipos de caracteres que necesitamos
    characters = string.ascii_letters + string.digits + string.punctuation

    password = "".join(secrets.choice(characters) for i in range (long))
    return password

main()