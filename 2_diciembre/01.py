class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad
        
def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
    
persona1 = Persona ("Laura",20)
persona2 = Persona ("Andres",25)
    
persona1.saludar()
persona2.saludar()