#Calculadora#
import os
os.system 
a=0
b=0
suma=0
resta=0
multiplicar=0
dividir=0
opcion=0
print ("Ingrese el primer numero")
a=int(input())
print ("Ingrese el segundo numero")
b=int(input())
print ("1.Suma")
print ("2.Resta")
print ("3.Multiplicar")
print ("4.Dividir")
print ("Favor ingrese su opcion: ")
opcion=int(input())
if opcion >= 1 and opcion <= 4:
    if opcion==1:
        suma=a+b
        print("El resultado de la suma es: ",suma)
    else:
        if opcion==2:
                resta=a-b
                print("El resultado de la resta es: ", resta)
        else:
            if opcion==3:
                        multiplicar=a*b
                        print("El resultado de la multiplicacion es: ", multiplicar)
            else:
                if opcion==4:
                    dividir=a/b
                    print("El resultado de la division es: ", dividir)
                else:
                    print("Digite una opcion valida")
else:
    print("Digite una opcion valida")



