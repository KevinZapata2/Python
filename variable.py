# a = 45 
# b = 1.2
# c= 45 
# d = "hola"
# print(type(d))
# if a==c:
#     print("a y c son iguales")
# else:
#     print("a y b no son")

# #DIVISION
# Division = 20//5
# print(Division)    
# #PONTECIACION
# pontencia = 2**3
# print(pontencia)
# potencia1 =pow(3,3)
# print(potencia1)
# #RESIDUO: % (Modulo)
# resto = 20%8
# print(resto)

#DIVISION CON DATOS SOLICITADOS AL USUARIO
#INPUT(): string
# nombre = input("Ingrese su nombre:").upper()
# print(nombre)
# dividendo = int(input("Ingrese un numero entero positivo:"))
# divisor = int(input("Ingrees un numero entrero positivo"))

# div = dividendo//divisor
# # print("El resultado de la division es", div)
# print(f"La division entre {dividendo} y {divisor} es {div}")

#lover(): cambiar todo el texto a minuscula
#upper(): cambiar el texto a mayuscula
#title(): cambia a mayuscula las primeras letras de cada palabra

# numero = int(input("Ingresa un número entero positivo: "))

# if numero > 0:
#     if numero % 2 == 0:
#         print(f"El número {numero} es par.")
#     else:
#         print(f"El número {numero} es impar.")
# else:
#     print("Por favor, ingresa un número entero positivo.")
    
    
#Solicitar al usuario, nombre, edad, si tiene pasaporte o no. Si el usuario es mayor de edad y tiene pasaporte debe 
# mostar el nombre del usuario puede salir del pais, de lo contrario no puede salir del pais


# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# tiene_pasaporte = input("¿Tienes pasaporte? (Responde 'si' o 'no'): ").title()

# if edad > 18 and tiene_pasaporte == 'Si':
#     print(f"{nombre}, puedes salir del pais.")
# else:
#     print(f"{nombre}, no puedes salir del pais.")


# Por medio de ELIF solicitar al usuario por medio de un menu el area de la figura que quiera calcular. 
# figuras para calcular el area son: circulo, cuadrado, triangulo
import math
print("Calculadora de áreas")
print("1. Círculo")
print("2. Cuadrado")
print("3. Triángulo")

opcion = int(input("Elige la figura para calcular su área (1/2/3): "))

if opcion == 1:
    radio = float(input("Ingresa el radio del círculo: "))
    area_circulo = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area_circulo}")
elif opcion == 2:
    lado = float(input("Ingresa el lado del cuadrado: "))
    area_cuadrado = lado ** 2
    print(f"El área del cuadrado es: {area_cuadrado}")
elif opcion == 3:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    area_triangulo = (base * altura) // 2
    print(f"El área del triángulo es: {area_triangulo}")
else:
    print("Opción inválida. Por favor, elige una opción válida (1/2/3).")
