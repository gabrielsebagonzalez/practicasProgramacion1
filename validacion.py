"""Pedí al usuario una fila (1 a 3) y una columna (1 a 4). Si cualquiera de las dos está fuera derango, volver a pedir solo ese valor. Repetí hasta que ambas sean válidas."""


# fila = int(input("Ingrese una fila entre 1 y 3: "))
# while fila < 1 or fila > 3:
#     fila = int(input("Fila inválida debe ser entre 1 y 3: "))

# columna = int(input("Ingrese una columna entre 1 y 4: "))
# while columna < 1 or columna > 4:
#     columna = int(input("Columna inválida debe ser entre 1 y 4: "))
# print(f"Coordenada válida ({fila};{columna})")


"""Simulá el lanzamiento de un dado hasta sacar un 6. Luego preguntá si quiere volver a jugar(s/n); si responde "s", repetí todo el proceso."""

import random

jugar_dado = input("Quiere jugar a los dados? debe sacar 6 s/n: ").lower()

while jugar_dado == "s":
    lanzamiento = 0
    intentos = 0

    while lanzamiento != 6:
        lanzamiento = random.randint(1,6)
        intentos += 1
        print(lanzamiento, end=" ")
    print(f"Salió el 6 después de {intentos} intentos")

    jugar_dado = input("Quiere volver a jugar? s/n: ")
print("Gracias por participar")

