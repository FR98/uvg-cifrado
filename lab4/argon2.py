from passlib.hash import argon2

password = input("Ingrese la contraseña: ")
# Generacion de hash
h = argon2.hash(password)
print("Hash: ", h)

# Generacion de hash pero con un numero definido de rondas
roundH = argon2.using(rounds=4).hash(password)
print("Hash with 4 rounds: ", roundH)

ver = argon2.verify(password, h)
print("Verificacion con '{}': ".format(password), ver )

bad = argon2.verify("otrapalabra", h)
print("Vericicación con otra palabra que no es la contraseña ingresada: ", bad)