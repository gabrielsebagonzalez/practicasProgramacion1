cant_numeros = 4
print("Ingrese número 1")
num = int(input())

max_num = num
min_num = num
pos_max = 1
pos_min = 1

for cont in range(2, cant_numeros + 1):
    print("Ingrese número", cont)
    num = int(input())
    if num > max_num:
        max_num = num
        pos_max = cont
    elif num < min_num:
        min_num = num
        pos_min = cont

print(f"El mayor número es {max_num} y salió en la posición {pos_max}")
print(f"El menor número es {min_num} y salió en la posición {pos_min}")