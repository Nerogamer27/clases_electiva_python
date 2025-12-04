## Guardar nombres de estudiantes en un archivo y luego leerlos
with open("agenda_antonio.txt", "w") as ejemplo:
    for i in range(6):
        nombre = input("Ingrese el nombre del estudiante: ")
        ejemplo.write(nombre + "\n")
        telefono = input("Ingrese el telefono del estudiante: ")
        ejemplo.write("Telefono:" +telefono+ "\n")
        direccion = input("Ingrese la direccion del estudiante: ")
        ejemplo.write("Direccion:" +direccion+"\n")
        print("----------------------------------------")
## Leer y mostrar el contenido del archivo 
    with open("estudiantes.txt", "r") as ejemplo:
        contenido = ejemplo.read()
        print("Lista de estudiantes guardados.")