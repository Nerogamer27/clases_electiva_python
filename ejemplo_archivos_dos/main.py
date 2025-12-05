import funciones

ARCHIVO="archivo_ejemplo.csv"

while True:
    print("MENÚ")
    print("1. Ver Estudiantes")
    print("2. Agregar Estudiantes")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion=="1":
        ests=funciones.leer_estudiantes(ARCHIVO)
        for e in ests:
            print(f"{e["nombre"]} - {e["edad"]} años - {e["direccion"]}")
            
    elif opcion=="2":
        nombre=input("Nombre: ")
        edad= input("Edad: ")
        direccion= input ("Direccion: ")
        
        if not funciones.validar_nombre(nombre):
            print("⚠️Nombre Invalido")
            continue
        if not funciones.validar_direccion(direccion):
            print ("⚠️Direccion invalida")
            continue
        if funciones.validar_edad(edad):
            print ("⚠️Edad invalida")
            continue
        funciones.agregar_estudiante(ARCHIVO,nombre,edad,direccion)
        print("Estudiante agregado con exito")
        
    elif opcion =="3":
        break
    else:
        print("Opcion no valida")