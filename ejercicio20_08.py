"""Una colonia de bacterias se duplica exponencialmente: al final de cada hora la cantidad total de bacterias se multiplica por 2.
Pedir la cantidad inicial y la cantidad de horas, y calcular la cantidad de bacterias que abrá en total.
Fórmula B = B_inicial * (2^horas)"""

bacterias_inicial = int(input("Ingrese la cantidad inicial de bacterias: "))
horas = int(input("Ingrese la cantidad de horas: "))

total_bacterias = bacterias_inicial * pow(2, horas)

print(f"La cantidad de total de bacterias después de {horas} horas son: {total_bacterias}")
