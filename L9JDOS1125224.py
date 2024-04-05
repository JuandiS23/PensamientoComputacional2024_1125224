# Ejercicio 1 
print("Ingrese su edad")
edad= int(input())
if edad >= 18:
    print("Usted ya es mayor de edad, debe tramitar su DPI")
else:
    print("Usted es menor de edad, disfrute")

#Ejercicio 2 
print("Ingrese un numero")
numero= int(input())
if numero >= 0:
    print("El numero ingresado es positivo")
else:
    print("El numero ingresado es negativo")

#Ejercicio 3 
print("ingresar un numero del 1 al 5")
numero = int(input())
numero == 1
match numero: 
    case 1: 
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case 4:
        print("Cuatro")
    case 5:
        print("Cinco")
    case _:
        print("numero no definido")

# Ejercico 4 
print("Te voy a enseñar la tabla del numero 2")
contador = 0 
while contador <= 5:
    b= contador*2
    print(b)
    contador= contador+1