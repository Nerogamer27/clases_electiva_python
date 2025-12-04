Q=0
while Q==0:
        a=int(input("Ingrese el primer número: "))
        b=int(input("Ingrese el segundo número: "))
        o=int(input("¿Qué tipo de operación desea realizar?\n1.+\n2.-\n3.*\n4./\n5. Salir\n"))
        if o==1:
                c=a+b
                print("El resultado de la operacion es: ",c)
        elif o==2:
                c=a-b
                print("El resultado de la operacion es: ",c)
        elif 0==3:
                c=a*b
                print("El resultado de la operacion es: ",c)
        elif o==4:
                c=a/b
                print("El resultado de la operacion es: ",c)
        elif o==5:
                Q=1
        else:
                print("Opcion no valida")
print("Gracias por usarnos :)")