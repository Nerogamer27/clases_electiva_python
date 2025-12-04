numero_secreto=6
intento=int(input("Adivina el número secreto (entre 1 y 10): "))
while intento!=numero_secreto:
    print("Número incorrecto. Inténtalo de nuevo.")
    intento=int(input("Adivina el número secreto (entre 1 y 10): "))
print("¡Felicidades! Has adivinado el número secreto.")