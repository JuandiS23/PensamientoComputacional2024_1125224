# Problema 1 
lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "tipo Equilátero"
    elif a == b or a == c or b == c:
        return "tipo Isósceles"
    else:
        return "tipo Escaleno"


if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Error: Los lados del triángulo deben ser mayores que cero.")
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Error: Los lados no forman un triángulo válido.")
else:
    print("El triángulo es", tipo_triangulo(lado1, lado2, lado3))

#Ejercicio 2 
import math

def ObtenerPerimetro(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

def ObtenerArea(radio):
    area = math.pi * radio**2
    return area

def ObtenerVolumen(radio):
    volumen = (4/3) * math.pi * radio**3
    return volumen

radio = float(input("Ingrese el radio del círculo: "))

perimetro = ObtenerPerimetro(radio)
area = ObtenerArea(radio)
volumen = ObtenerVolumen(radio)

print(f"El perímetro del círculo es: {perimetro:.2f}")
print(f"El área del círculo es: {area:.2f}")
print(f"El volumen de la esfera es: {volumen:.2f}")

#Ejercicio 3 
def imprimir_mes(numero):
    if numero == 1:
        print("Enero")
    elif numero == 2:
        print("Febrero")
    elif numero == 3:
        print("Marzo")
    elif numero == 4:
        print("Abril")
    elif numero == 5:
        print("Mayo")
    elif numero == 6:
        print("Junio")
    elif numero == 7:
        print("Julio")
    elif numero == 8:
        print("Agosto")
    elif numero == 9:
        print("Septiembre")
    elif numero == 10:
        print("Octubre")
    elif numero == 11:
        print("Noviembre")
    elif numero == 12:
        print("Diciembre")
    else:
        print("Error: El número ingresado no es válido.")

numero = int(input("Ingrese un número del 1 al 12: "))

imprimir_mes(numero)