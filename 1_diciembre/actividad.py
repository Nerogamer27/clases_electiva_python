def agenda(nombre,numero,direccion):
    return f"Contacto guardado: {nombre}, Teléfono: {numero}, Dirección: {direccion}"
    for i in range(2):
        nombre=input("Ingrese el nombre del contacto: ")
        numero=input("Ingrese el número de teléfono: ")
        direccion=input("Ingrese la dirección: ")
        print("Contacto guardado exitosamente.")
        mensaje=agenda(nombre,numero,direccion)
        print(mensaje)
        print("-----------------------------")
print("Agenda de Contactos")
for i in range(2):
    nombre=input("Ingrese el nombre del contacto: ")
    numero=input("Ingrese el número de teléfono: ")
    direccion=input("Ingrese la dirección: ")
    print("Contacto guardado exitosamente.")
    mensaje=agenda(nombre,numero,direccion)
    print(mensaje)
    print("-----------------------------")