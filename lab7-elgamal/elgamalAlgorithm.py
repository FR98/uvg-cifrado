from random import randint
import random
from math import pow

min = pow(10, 5)
max = pow(10, 6)

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
    while f <= r: # verifica si n es divisible por el resto de numeros
        # print ('\t',f)
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def randomPrime(min, max):
    rand = random.randint(min, max)
    while (not isPrime(rand)):
        rand = random.randint(min, max)
    return rand

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Generando números grandes aleatorios
def gen_key(primo):
    key = random.randint(min, primo)
    while gcd(primo, key) != 1:
        key = random.randint(min, primo)
    return key

# Cifrado asimétrico
def encrypt(msg, primo, A, g):
    print()
    print('=' * 50)
    print('B está cifrando mensaje a A')
    print('-' * 50)
    en_msg = []
    b = gen_key(primo)
    print('Secreto de B: ', b)
    B = (g ** b) % primo
    print('Público de B: ', B)
    s = (A ** b) % primo
    print('Secreto entre A y B: ', s)
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
    print('=' * 50)
    print()
    return en_msg, B

def decrypt(en_msg, B, a, primo):
    print()
    print('=' * 50)
    print('A está descifrando mensaje de B')
    print('-' * 50)
    dr_msg = []
    secreto = (B ** a) % primo
    print('Secreto entre A y B: ', secreto)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / secreto)))
    print('=' * 50)
    print()
    return dr_msg



primo = randomPrime(min, max)
print('Primo: ', primo)
g = random.randint(2, primo)
print('Generador: ', g)

print()
print('=' * 50)
print("A calcula sus llaves")
print('-' * 50)
# Llave privada de A
a = gen_key(primo)
print('Secreto de A: ', a)
A = (g ** a) % primo
print('Público de A: ', A)
print('=' * 50)
print()


msg = input('Ingrese un mensaje: ')
print("Mensaje de B a A:", msg)

en_msg, B = encrypt(msg, primo, A, g)
dr_msg = decrypt(en_msg, B, a, primo)
dmsg = ''.join(dr_msg)
print("Mensaje decifrado :", dmsg)
