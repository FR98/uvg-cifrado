from random import randint

import random  
from math import pow
  

min = pow(10,2)
max = pow(10,6)

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
        return b; 
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
    print('')
    en_msg = [] 
    print('B está cifrando mensaje a A')
    b = gen_key(primo)
    print('Secreto de B: ',b)
    s = (A** b)% primo
    print('Secreto entre A y B: ',s)
    B = (g** b)% primo
    print('Público de B: ',B)
    for i in range(0, len(msg)): 
        en_msg.append(msg[i])
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i])
    return en_msg, B 
  
def decrypt(en_msg, B, a, primo): 
    print('')
    print('A está descifrando mensaje de B')
    dr_msg = [] 
    secreto = (B** a)%primo
    print('Secreto entre A y B: ',secreto)
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/secreto)))          
    return dr_msg

a = random.randint(min, max)

msg = 'encryption'
print("Original Message :", msg) 

primo = randomPrime(min, max) 
print('Primo: ',primo)
g = random.randint(2, primo) 
print('Generador: ',g)

a = gen_key(primo)# Llave privada de A 
print('Secreto de A: ',a)

A = (g**a)%primo
print('Público de A: ',A)

en_msg, B = encrypt(msg, primo, A, g) 
dr_msg = decrypt(en_msg, B, a, primo) 
dmsg = ''.join(dr_msg) 
print("Decrypted Message :", dmsg)
