# Ejercicio 2
print ("Ingrese un numero mayor a 1")
numero= int(input())

es_primo = True 
for b in range(2, numero):
    if numero % b == 0:
        es_primo = False
        break
if es_primo:
    print(numero, "es un numero primo")
else: 
    print(numero, "no es un numero primo")

#Ejercicio 3
numero = int(input("Ingrese un número entero "))
suma_total = 0
for b in range(1, numero + 1):
    suma_total += b
print("La suma desde 1 hasta", numero, "es:", suma_total)