# https://github.com/RyanRiddle/elgamal

import sys
import elgamal


message = input("Ingrese el mensaje que desea cifrar con ElGamal: \n")

# Por defecto genera llaves de 256 bits
keys = elgamal.generate_keys()
publicKey = keys['publicKey']
print("Prirmo: ", publicKey.p)
print("Public: ", publicKey.h)
privateKey = keys['privateKey']
print("Generador: ", privateKey.g)
print("Private: ", privateKey.x)

cipher = elgamal.encrypt(publicKey, message)
print(cipher, "\n")

plaintext = elgamal.decrypt(privateKey, cipher)
print(plaintext)