import math

# def imprimir_hola_mundo():
#     print("Hola mundo")

# imprimir_hola_mundo()

# def calcular_area_circulo(radio):
#     return 2 * math.pi * (radio ** 2)

# def calcular_perimetro(radio):
#     return 2 * math.pi * radio

# radio = float(input("Ingrese el radio del círculo: "))

# resultado_area = calcular_area_circulo(radio)
# resultado_perimetro = calcular_perimetro(radio)

# def segundos_a_horas(segundos):
#     return segundos/3600

# seg = int(input("Ingrese la cantidad de segundos: "))
# horas = segundos_a_horas(seg)

# print(f"{seg} segundos son equivalentes a {round(horas, 2)} horas")

# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(f"{numero} x {i} = { numero * i}")

# num = int(input("Ingrese un número: "))
# tabla_multiplicar(num)

# def obtener_resto(num1, num2):
#     return num1 % num2

# def es_multiplo(x, y):
#     return obtener_resto(x, y) == 0

# n1 = int(input("Número 1: "))
# n2 = int(input("Número 2: "))

# resto = obtener_resto(n1, n2)

# print(f"El resto entre {n1} y {n2} es {resto}")
# if es_multiplo(n1, n2):
#     print(f"{n1} es multiplo de {n2}")


#Composición de funciones

def siguiente(num):
    return num + 1

def doble(num):
    return num * 2

print(doble(siguiente(4)))
