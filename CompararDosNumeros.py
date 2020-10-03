#CompararDosNumeros#

'''
Se requiere de un programa que solicite dos números al usuario por consola, y determine cuál de los dos es 
el MAYOR en el caso que los dos números sean diferentes. SI los números ingresados son IGUALES, 
el programa debe escribir por pantalla un mensaje indicando que dichos valores son iguales, y por lo tanto 
NO habrá un número mayor.
Validaciones adicionales:
El programa SOLO debe aceptar números enteros positivos.

'''
import os
os.system 
a=0
b=0
print ("Ingrese el primer numero")
a=int(input())
print ("Ingrese el segundo numero")
b=int(input())
if a>0 and b>0:  
    if a==b :
        print("Los numeros ingresados son iguales")
    else:
        if a>b:
            print ("El numero mayo es:", a)
        else:
            print ("El numero mayor es:", b)
else:
    print ("Los valores ingresados deben ser positivos")
