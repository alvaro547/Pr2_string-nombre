print(" ")
print("Alvaro Campechano 3W")
print(" ")
def saludo(nombre):
    """
    Función que recibe un nombre y despliega un saludo.

    Parámetros:
    nombre (str): El nombre de la persona a saludar.

    Retorna:
    None: Imprime el saludo en la consola.
    """
    print(f"¡Hola {nombre}!")

# Ejemplo de uso
if __name__ == "__main__":
    nombre_usuario = input("Introduce tu nombre: ")
    saludo(nombre_usuario)
