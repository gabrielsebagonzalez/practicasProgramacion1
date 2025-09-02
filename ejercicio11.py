"""Desarrollar un algoritmo que permita ingresar el nombre y la edad (por separado) de diferentes personas.La carga termina cuando en el nombre de la próxima persona se ingresa un asterisco(*). La computadora debe mostrar cómo se llama la persona más joven"""

CORTE = "*"
NOMBRE_INVALIDO = "XXXXXXXXXXXXX"
edad_minima = float("inf")
persona_joven = NOMBRE_INVALIDO
EDAD_MAXIMA = 125


nombre = input(f"Ingrese el nombre de la persona o {CORTE} para salir: ")
while nombre != CORTE:
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    while edad < 0 or edad > EDAD_MAXIMA:
        edad = int(input(f"Edad inválida, ingrese nuevamente la edad de {nombre}: "))
    if edad < edad_minima:
        edad_minima = edad
        persona_joven = nombre
    nombre = input(f"Ingrese otro nombre o {CORTE} para salir: ")

if persona_joven == NOMBRE_INVALIDO:
    print("No se ingresaron personas")
else:
    print(f"La persona más joven es {persona_joven} y tiene {edad_minima} años")