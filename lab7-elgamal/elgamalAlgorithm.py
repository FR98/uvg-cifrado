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

# # Variables iniciales
# primo = 23
# generador = randint(1, primo)

# a, b = randint(1, primo-1), randint(1, primo-1)

# A = (generador ** a) % primo
# B = (generador ** b) % primo

# aliceSecreto = (B ** a) % primo
# bobSecreto = (A ** b) % primo





#Python program to illustrate ElGamal encryption 
  
import random  
from math import pow
  
a = random.randint(2, 10) 
  
def gcd(a, b): 
    if a < b: 
        return gcd(b, a) 
    elif a % b == 0: 
        return b; 
    else: 
        return gcd(b, a % b) 
  
# Generating large random numbers 
def gen_key(primo): 
  
    key = random.randint(pow(10, 20), primo) 
    while gcd(primo, key) != 1: 
        key = random.randint(pow(10, 20), primo) 
  
    return key 

  
# Asymmetric encryption 
def encrypt(msg, primo, A, g): 
    en_msg = [] 
    b = gen_key(primo)
    s = (A** b)% primo
    B = (g** b)% primo
    for i in range(0, len(msg)): 
        en_msg.append(msg[i])
    print("g**b used : ", B) 
    print("g**ab used : ", s) 
    for i in range(0, len(en_msg)): 
        en_msg[i] = s * ord(en_msg[i])
    return en_msg, B 
  
def decrypt(en_msg, B, a, primo): 
    dr_msg = [] 
    secreto = (B** a)%primo
    for i in range(0, len(en_msg)): 
        dr_msg.append(chr(int(en_msg[i]/secreto)))          
    return dr_msg 

msg = 'encryption'
print("Original Message :", msg) 

primo = random.randint(pow(10, 20), pow(10, 50)) 
g = random.randint(2, primo) 

a = gen_key(primo)# Private key for receiver 
A = (g**a)%primo
print("g used : ", g) 
print("g^a used : ", A) 

en_msg, B = encrypt(msg, primo, A, g) 
dr_msg = decrypt(en_msg, B, a, primo) 
dmsg = ''.join(dr_msg) 
print("Decrypted Message :", dmsg)
