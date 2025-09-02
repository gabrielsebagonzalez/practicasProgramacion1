for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("---------")

num = int(input("Ingrese un número: "))

for i in range(num):
    for j in range(num):
        print("*", end=" ")
    print()

num = int(input("Ingrese un número: "))
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()

num = int(input("Ingrese un número: "))
for i in range(num):
    for j in range(num):
        if i == 0 or i == num -1 or j == 0 or j == num - 1:
            print(1, end=" ")
        else:
            print(0, end=" ")
            
    print()