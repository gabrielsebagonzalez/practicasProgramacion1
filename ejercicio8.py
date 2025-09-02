"""Desarrollar un algoritmo que permita ingresar un número entero entre 1 y 10 (inclusive). La
computadora debe mostrar la tabla de multiplicar del número ingresado."""

num = int(input("Ingresar un número entero entre 1 y 10: "))
if num >= 1 and num <= 10:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Debe ser un número entre 1 y 10")