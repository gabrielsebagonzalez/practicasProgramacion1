# Verificar que un número es par

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")

nombre = input("Ingresa tu nombre: ")

print(f"nombre ingresado: {nombre}")
print(f"Nombre en mayúscula: {nombre.upper()}")
print(f"Nombre en minúscula: {nombre.lower()}")
print(f"Nombre Título: {nombre.title()}")

color = input("Ingrese un color del semáforo: ").lower()

if color == "rojo":
    print("No avances")
elif color == "amarillo":
    print("Precaución")
elif color == "verde":
    print("Avance")
else:
    print("Color inválido")

temp = float(input("Ingrese una temperatura: "))

if temp < 10:
    print("Hace frío")
elif temp >= 10 and temp <= 25:
    print("Clima agradable")
else:
    print("Hace calor")




