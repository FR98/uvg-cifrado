from random import randint

# Variables iniciales
primo = 23
generador = randint(0, 100)
print("\nVariables Publicas: ")
print("\tPrimo: {}".format(primo))
print("\tGenerador: {}".format(generador))

a, b = randint(0, 100), randint(0, 100)

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
