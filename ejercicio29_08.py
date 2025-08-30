"""Pedir los lados de un triángulo y:
1. Validad que los lados sean positivos
2. Validar que los valores ingresados puedan formar un triángulo (aplicando ladesigualdadtriangular).
3. Clasificarlo como equilátero, isósceles o escaleno.
Un triángulo es válido solo si la suma de dos de sus lados siempre es mayor que el tercero.
Es decir, deben cumplirse estas tres condiciones al mismo tiempo:
a + b > c
a + c > b
b + c > a
Si alguna de estas no se cumple, los lados no forman un triángulo válido."""

lado1 = float(input("Ingrese el lado del triángulo: "))
lado2 = float(input("Ingrese el lado del triángulo: "))
lado3 = float(input("Ingrese el lado del triángulo: "))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados deben ser positivos")
elif lado1 + lado2 <= lado3  or lado2 + lado3 <= lado1 or lado1 + lado3 <= lado2:
    print("Los lados no forman un triángulo")
else:
    if lado1 == lado2 == lado3:
        print("El triágulo es equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es isósceles")
    else:
        print("El trángulo es escaleno")

"""Crear una versión simple del clásico juego “Piedra, Papel o Tijera”.
El programa debe pedir la elección de cada jugador y anunciar quién gana o si hubo empate."""

print("**** Juego Piedra Papel Tijera ****")

jugador1 = input("Ingrese piedra, papel o tijera: ").lower()
jugador2 = input("Ingrese piedra, papel o tijera: ").lower()

if jugador1 == jugador2:
    resultado = "Empataron"

else:
    if (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
        resultado = "Gana jugador 1"
    else:
        resultado = "Gana jugador 2"

print(resultado)

"""Escribir un programa que simule un
cajero automático
con un saldo inicial de
$150000
.
El sistema debe mostrar un menú con 4 opciones:
1.Consultar saldo
2.Retirar dinero (validar que sea mayor a 0 y que no supere el saldo)
3.Depositar dinero (validar que sea mayor a 0)
4.Salir
Según la opción ingresada, mostrar el resultado correspondiente o un mensaje de error si la opción no es válida."""


saldo = 150000
print("***Cajero automático***")
print("1. Consultar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir")
opcion = int(input("Ingrese una opción del menú: "))

if opcion == 1:
    print(f"Su saldo es ${saldo}") 
elif opcion == 2:
    monto = float(input("Ingrese la cantidad a retirar: "))
    if monto <= 0:
        print("Debe ingresar un monto mayor a 0")
    elif saldo < monto:
        print("Saldo insuficiente")
    else:
        saldo -= monto
        print(f"Ud retiró ${monto} su saldo actual es ${saldo}")
elif opcion == 3:
    monto = float(input("Ingrese al monto a depositar: "))
    if monto <= 0:
        print("Debe ingresar un monto mayor a 0")
    else:
        saldo += monto
        print(f"Ud depositó ${monto} su saldo actual es {saldo}")

elif opcion == 4:
    print("Adios!, Gracias por usar nuestro banco")
else:
    print("Opción inválida")

"""Escribir un programa que pida el monto de una compra y el medio de pago(efectivo, débito o crédito).
Reglas: 
Si el monto ingresado es menor o igual a 0, mostrar un mensaje de error.
Si paga en efectivo, aplicar un 20% de descuento. 
Si paga con débito, aplicar un 10% de descuento.
Si paga con crédito, no aplicar descuento.
Si el medio de pago no es válido, mostrar un mensaje de error.
"""

monto = float(input("Ingrese el monto de la compra: "))
if monto <= 0:
    print("Error, debe ser mayor a 0")
    exit()
print("Formas de pago:\n1- Efectivo\n2- Débito\n3- Crédito")
forma_pago = int(input("Elija una opción por favor (númeral): "))

if forma_pago == 1:
    descuento = monto * 0.20
    monto_total = monto - descuento
elif forma_pago == 2:
    descuento = monto * 0.10
    monto_total = monto - descuento
elif forma_pago == 3:
    descuento = 0
    monto_total = monto
else:
    print("Forma de pago inválida")
    exit()

print(f"Su compra tiene un descuento de ${descuento} su saldo a pagar es: ${monto_total}")

"""Escribir un programa que simule un inicio de sesión.
Reglas:
Si el usuario es "admin" :
Pedir la contraseña.
Validar que sea "1234".
Si es correcta → mostrar "Acceso concedido. Bienvenido, administrador."
Si es incorrecta → mostrar "Contraseña incorrecta para admin."
Si el usuario es "invitado":
Pedir la contraseña.
Validar que sea "guest".
Si es correcta → mostrar "Acceso concedido. Bienvenido, invitado."
Si es incorrecta → mostrar "Contraseña incorrecta para invitado."
Si el usuario no coincide con ninguno de los anteriores mostrar "Usuario no reconocido."""

usuario = input("Ingrese el usuario: ").lower()
if usuario == "admin":
    password = input("Ingrese la contraseña: ")
    if password == "1234":
        print("Acceso concedido. Bienvenido, administrador")
    else:
        print("Contraseña incorrecta para admin.")
elif usuario == "invitado":
    password = input("Ingrese la contraseña: ")
    if password == "guest":
        print("Acceso concedido. Bienvenido, invitado.")
    else:
        print("Contraseña incorrecta para invitado.")
else:
    print("Usuario no reconocido.")

