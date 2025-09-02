cant_numeros = 5
sumatoria = 0
promedio = 0

for cont in range(1, cant_numeros + 1):
    print("Ingrese número", cont)
    num = int(input())
    sumatoria += num

promedio = sumatoria / cant_numeros

print(f"La suma de todos los números es {sumatoria}")
print(f"El promedio es {promedio}")