from random import randint

"""
Proceso:
- Se fija un numero primo p largo (600 digitos o 2000 bits)
- Se fija un entero g que esta entre {1, ...., p}
- Alice elige aleatoriamente un numero a entre {1, ...., p-1}
- Alice calcula A = g^a (mod p) y se lo envia a Bob
- Bob calcula B = g^b (mod p) y se lo envia a Alice
- * Entonces se creo la llave Kab = g^ab (mod p)
- Alice y Bob pueden calcular Kab
    - Alice obtiene Kab asi:
        Kab = B^a (mod p) = (g^b)^a
    - Bob obtiene Kab asi:
        Kab = A^b (mod p) = (g^a)^b

Importante:
    - p y g son publicos
    - a y b no son publicos

Los atacantes ven los valores de:
    p, g, A, B

Este protocolo es indefenso a man-in-the-middle, si un atacante intercepta A y B y los reemplaza por A' y B', este atacante controla la comunicacion
"""

# Variables iniciales
primo = 23
generador = randint(1, primo)
print("\nVariables Publicas: ")
print("\tPrimo: {}".format(primo))
print("\tGenerador: {}".format(generador))

a, b = randint(1, p-1), randint(1, p-1)

# Alice envia a Bob A = g^a mod p
# Bob envia a Alice B = g^b mod p
print("\nPublico: ")
A = (generador ** a) % primo
B = (generador ** b) % primo
print("\tAlice publica: {}".format(A))
print("\tBob publica: {}".format(B))

print("\nCalcular secreto: ")
# Alice: s = B^a mod p
# Bob: s = A^b mod p
aliceSecreto = (B ** a) % primo
print("\tAlice secreto: {}".format(aliceSecreto))
bobSecreto = (A ** b) % primo
print("\tBob secreto: {}".format(bobSecreto))
