"""
Signature.py
Implementacion de firima digital usando el algoritmo de Elgamal
"""
from random import randint
import random
from math import pow
from sha256 import hmacSha256
from elGamal import encrypt, decrypt, randomPrime , gen_key
#limites
min = pow(10, 5)
max = pow(10, 6)

MESSAGE = "Este es un mensaje de prueba"
#Se generan los numeros que seran necesarios para el proceso
primo = randomPrime(min, max)
print('Primo: ', primo)
g = random.randint(2, primo)
print('Generador: ', g)


# Informacion de Alice que enviara a Bob
aSecret = gen_key(primo)
aPublic = (g ** aSecret) % primo

# Enviar informacion a Bob

myHash = hmacSha256( msg = MESSAGE , key = str(aPublic) )
encrypted , bPublic = encrypt(msg = myHash ,primo = primo , A = aPublic , g = g)

# Verificacion de Alice

alicesHash = hmacSha256(msg = MESSAGE , key = str(aPublic) )
decrypted = decrypt(encrypted , bPublic , aSecret , primo)
decrypted=''.join(decrypted)
print('*'*50)
print('FUNCIONO: ' , decrypted== alicesHash)
print('*'*50)
