import sys
import numpy as np
clave = np.array([[2, 3],
                  [4, 5]])

mensaje_a_encriptar = sys.argv[1]

#Cifrado
#1) Convertir cada letra del mensaje a su analogo ASCII
numeros = []
for letra in mensaje_a_encriptar:
    numeros.append(ord(letra))

#2) Crear una matriz de 2xN a partir de la lista de numeros creado en la parte 1
if len(mensaje_a_encriptar)%2 == 0:
    matriz = np.array(numeros).reshape((2,int(len(numeros)/2)))
else:
    numeros.append(0)
    matriz = np.array(numeros).reshape((2,int(len(numeros)/2)))

#3) Multiplicar la clave por la matriz mensajef
matriz_cifrada = np.dot(clave, matriz)

#4) Transformar la matriz a vector
numeros_cifrados = matriz_cifrada.flatten()

#4) Convertir cada numero a su caracter correspondiente
texto_cifrado = ""
for numero in numeros_cifrados:
    texto_cifrado += chr(numero)

#Hallando el mensaje descifrado
inv = np.linalg.inv(clave)
matriz_descifrada = np.dot(inv, matriz_cifrada).astype(int)
numeros_descifrados = matriz_descifrada.flatten()
texto_descifrado = ""
for numero in numeros_descifrados:
    texto_descifrado += chr(numero)

print("Mensaje original: ", mensaje_a_encriptar)
print("Mensaje cifrado: ", texto_cifrado)
print("Mensaje descifrado: ", texto_descifrado)
 