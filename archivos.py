#Escritura inicial de un archivo

print("1- Escribiendo archivo")
archivo_producto = open("productos.txt", "w")
archivo_producto.write("Lapicera\n")
archivo_producto.write("Cuaderno\n")
archivo_producto.close()

#Lectura de un archivo

print("2. Leyendo archivo y mostrando contenido")
archivo_producto = open("productos.txt", "r")
contenido = archivo_producto.read()
print(contenido)
archivo_producto.close()

#Insertar registros al final

print("3. Agregando contenido al final del archivo")
archivo_producto = open("productos.txt", "a")
archivo_producto.write("Goma de borrar\n")
archivo_producto.close()

#Lectura con nuevo registro

print("4. Leyendo archivo y mostrando contenido")
archivo_producto = open("productos.txt", "r")
contenido = archivo_producto.read()
print(contenido)
archivo_producto.close()

#Sobreescribiendo contenido en modo W

print("5. Escribiendo y pisando registros de archivo")
archivo_producto = open("productos.txt", "w")
archivo_producto.write("Regla\n")
archivo_producto.close()

#Nueva lectura de archivo

print("6. Leyendo archivo y mostrando contenido")
archivo_producto = open("productos.txt", "r")
contenido = archivo_producto.read()
print(contenido)
archivo_producto.close()

#Lectura segura con with y modo r

print("Leyendo archivo con with")
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#Agregar contenido con with y modo a

print("Agregando nueva linea con with")
with open("productos.txt", "a") as archivo:
    archivo.write("Cartuchera\n")

#Lectura final

print("Leyendo archivo con with")
with open("productos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)