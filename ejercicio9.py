"""Desarrollar un algoritmo que permita ingresar una cantidad de personas. La computadora debe
pedir la edad de cada una y finalmente mostrar el porcentaje de personas que es mayor de edad."""
EDAD_MINIMA = 18
EDAD_MAXIMA = 125
mayor_edad = 0
porcentaje = 0

cant_personas = int(input("Ingrese una cantidad de personas: "))
while cant_personas <= 0:
    cant_personas = int(input("Cantidad inválida. Ingrese un número positivo: "))

for persona in range(cant_personas):
    edad = int(input(f"Ingrese la edad N°{persona + 1}: "))
    while edad < 0 or edad > EDAD_MAXIMA:
        edad = int(input(f"Edad inválida, ingrese nuevamente la edad N° {persona + 1}"))
    if edad >= EDAD_MINIMA:
        mayor_edad += 1

porcentaje = (mayor_edad / cant_personas) * 100
print(f"La cantidad de personas mayores de edad son {mayor_edad} y equivalen a un {porcentaje}%")
