## Guardar nombres de estudiantes en un archivo y luego leerlos
with open("estudiantes.txt", "w") as ejemplo:
    for i in range(3):
        nombre = input("Ingrese el nombre del estudiante: ")
        ejemplo.write(nombre + "\n")
## Leer y mostrar el contenido del archivo 
    with open("estudiantes.txt", "r") as ejemplo:
        contenido = ejemplo.read()
        print("Lista de estudiantes guardados.")
        print(contenido)