# -------------------------------------------------------
# Cifrado RSA
# -------------------------------------------------------
# Andy castillo
# Marco Fuentes
# Jose Block
# Gian Luca Rivera
# Francisco Rosal
# -------------------------------------------------------

import random
import base64

def menu():
    print("""
----------------------------
  Sistema de Criptografia RSA
    1. Generar llaves
    2. Encriptar
    3. Desencriptar
    4. Salir
----------------------------
    """)

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

def mcd(a, b):
    if a < b:
        a, b = b, a

    res = a % b
    if (res == 0):
        return b
    return mcd(b, res)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return False
    else:
        return x % m

def generarLlaves():
    min = 100
    max = 1000
    p = 0
    q = 0

    while (p == q):
        p = randomPrime(min, max)
        q = randomPrime(min, max)
    # n = modulo
    n = p * q
    print("p = {p}, q = {q}".format(p=p, q=q))
    print("n = {n}".format(n=n))

    # Funcion phi de Euler phi(n)
    phiN = (p - 1) * (q - 1)
    print("phi(n) = {phiN}".format(phiN = phiN))

    d = False
    while (not d):
        e = random.randint(0, phiN-1)
        while (mcd(e, phiN) != 1 or e > 1000000): # 1,000,000 para evitar numeros muy grandes y que tarde mucho
            e = random.randint(0, phiN-1)

        # d es el inverso de e mod phiN
        d = modinv(e, phiN)
    print("e = {e}".format(e=e))
    print("d = {d}".format(d=d))
    # print((e*d) % phiN)
    publicKey = str(n) + '.' + str(e)
    privateKey = str(n) + '.' + str(d)

    publicKey_bytes = publicKey.encode('ascii')
    publicKey_b64_bytes = base64.b64encode(publicKey_bytes)
    publicKey_encoded = publicKey_b64_bytes.decode('ascii')

    privateKey_bytes = privateKey.encode('ascii')
    privateKey_b64_bytes = base64.b64encode(privateKey_bytes)
    privateKey_encoded = privateKey_b64_bytes.decode('ascii')

    return publicKey_encoded, privateKey_encoded

def encriptar(message, publicKey_encoded):
    m = message

    publicKey_base64_bytes = publicKey_encoded.encode('ascii')
    publicKey_bytes = base64.b64decode(publicKey_base64_bytes)
    publicKey = publicKey_bytes.decode('ascii')

    n, e = publicKey.split('.')
    n, e = int(n), int(e)
    cifrado = pow((m % n), (e % n)) % n
    return cifrado

def desencriptar(cifrado, privateKey_encoded):
    privateKey_base64_bytes = privateKey_encoded.encode('ascii')
    privateKey_bytes = base64.b64decode(privateKey_base64_bytes)
    privateKey = privateKey_bytes.decode('ascii')

    n, d = privateKey.split('.')
    n, d = int(n), int(d)
    m = pow((cifrado % n), (d % n)) % n
    return m

# ----------------------------------------------------------------------------------------------------------------------------------------- #

opcion = "0"
while (opcion != "4"):
    menu()
    opcion = input("Seleccione un numero: ")

    if (opcion == "1"):
        # Generar Llaves
        publicK, privateK = generarLlaves()
        print("Llave Publica: ", publicK)
        print("Llave Privada: ", privateK)

    elif (opcion == "2"):
        # Cifrado
        message = input("Ingrese su mensaje:\n\t")
        publicKey = input("Ingrese la llave publica:\n\t")
        print(">> Encriptando mensaje...")
        encriptadototal = ""
        for letra_index in range(len(message)):
            messageB = message[letra_index].encode()
            messageNumber = int.from_bytes(messageB, "big")
            encriptadoLetra = encriptar(messageNumber, publicKey)
            encriptadototal += str(encriptadoLetra)
            if (letra_index + 2 <= len(message)):
                encriptadototal += "."

        encriptado_bytes = encriptadototal.encode('ascii')
        encriptado_base64_bytes = base64.b64encode(encriptado_bytes)
        print("Mensaje encriptado:\n" +  encriptado_base64_bytes.decode('ascii'))

    elif (opcion == "3"):
        # Decifrado
        encriptado_base64 = input("Ingrese el mensaje encriptado:\n\t")
        encriptado_base64_bytes = encriptado_base64.encode('ascii')
        encriptado_bytes = base64.b64decode(encriptado_base64_bytes)
        encriptado = encriptado_bytes.decode('ascii')

        privateKey = input("Ingrese la llave privada:\n\t")
        print(">> Desencriptando mensaje...")
        finalDecrypt = ""
        encriptadoPartes = encriptado.split(".")
        for e in range(len(encriptadoPartes)):
            if (e == len(encriptadoPartes) // 4):
                print(">> Desencriptando mensaje... 25%")
            elif (e == len(encriptadoPartes) // 2):
                print(">> Desencriptando mensaje... 50%")
            elif (e == (len(encriptadoPartes) // 2 + len(encriptadoPartes) // 4)):
                print(">> Desencriptando mensaje... 75%")
            m = desencriptar(int(encriptadoPartes[e]), privateKey)
            # print(m)
            try:
                finalDecrypt += (m.to_bytes(1, "big").decode())
            except:
                print("LLave incorrecta!")
                break
        print("Mensaje original:\n\t" + finalDecrypt)

    elif (opcion == "4"):
        print("Gracias por utilizar el programa.")
    else:
        print("Opcion no valida")
