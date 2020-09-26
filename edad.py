#Edad
'''Mostrar nombre y edad de un usuario'''

#INPUTS
anoactual=2020
nombre=0
anonacimiento=0
edad=0

#PROCESS
print ("ingrese su nombre: ")
nombre= input()
print ("ingrese su año de nacimiento: ")
anonacimiento= int(input())
edad= anoactual-anonacimiento
print ("su nombre es: ",nombre , "y su edad es: ",edad)
