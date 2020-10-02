from random import randint

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
