"""
elGamal.py
Implementacion del algoritmo de cifrado de ElGamal
"""
from random import randint
import random
from math import pow
#limites de numeros a generar
min = pow(10, 5)
max = pow(10, 6)

#Funcion para comprobar si un numero es primo
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True
#devuelve un numero primo aleatorio
def randomPrime(min, max):
    rand = random.randint(min, max)
    while (not isPrime(rand)):
        rand = random.randint(min, max)
    return rand
#calcula el gcd entre dos numeros
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)
#Funcion que genera la llave
def gen_key(primo):
    key = random.randint(min, primo)
    while gcd(primo, key) != 1:
        key = random.randint(min, primo)
    return key
#Funcion que cifra
def encrypt(msg, primo, A, g):
    en_msg = []
    b = gen_key(primo)
    B = (g ** b) % primo
    s = (A ** b) % primo
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
    return en_msg, B

#Funcion que descifra
def decrypt(en_msg, B, a, primo):
    dr_msg = []
    secreto = (B ** a) % primo
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / secreto)))
    return dr_msg