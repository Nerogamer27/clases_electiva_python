class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas =notas
    
    def calcular_promedio(self):
        promedio = sum(self.notas) / len(self.notas)
        return promedio
    
    def mostrar_info(self):
        promedio = self.calcular_promedio()
        if promedio>=3.0:
            estado="Aprobado"
        else:
            estado="Reprobado"
        print(f"Estudiante: {self.nombre} es:{promedio: .2f}, por esto esta ({estado})")
        
lista_estudiantes=[]
cantidad = int(input("Ingrese la cantidad de estudiantes: "))
for i in range(cantidad):
    print(f"\n Estudiante Número {i+1}")
    nombre = input("Ingrese el nombre del estudiante: ")
    notas = []
        
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1}: "))
        notas.append(nota)
        
    estudiante = Estudiante (nombre,notas)
    lista_estudiantes.append(estudiante)
        
aprobados=0
        
for est in lista_estudiantes:
    est.mostrar_info()
    if est.calcular_promedio()>=3.0:
        aprobados +=1
print(f"\nEntonces de los {cantidad} estudiantes,")
print(f"\n{aprobados} Aprobaron")
print(f"\n{cantidad - aprobados} Reprobaron")