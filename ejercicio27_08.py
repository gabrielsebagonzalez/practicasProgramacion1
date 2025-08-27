num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

print("***OPCIONES***")
print("1 Sumar")
print("2 Restar")
print("3 Multiplicar")
print("4 Dividir")

opcion = int(input("Ingrese la opción deseada: "))

if opcion == 1:
    operacion = num1 + num2
elif opcion == 2:
    operacion = num1 - num2
elif opcion == 3:
    operacion = num1 * num2
elif opcion == 4:
    operacion = num1 / num2
else:
    print("opción inválida")
    exit()

print(f"El resultado de la operación es: {operacion}")

#TERNARIO
nota = 6
resultado = "Aprobado" if nota >= 6 else "Desaprobado"
nota2 = 4

if nota > 0 and nota <= 10:
    if nota >= 6:
        print("Aprobada")
    else:
        print("Desaprobado") 
else:
    print("Nota inválida")

#Pedir un número y verificar si es positivo , y en caso de serlo comprobar si es par

num = int(input("Ingrese un número: "))

if num > 0:
    paridad = "Par" if num % 2 == 0 else "Impar"
    print(paridad)
else:
    print("Número inválido")
     