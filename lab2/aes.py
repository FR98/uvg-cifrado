import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random
import ast

"""
1. 
    i. No tuvimos que utilizar encode, sin embargo si decode porque el algoritmo devuelve bytes, se uso decode sobre el texto encriptado
    ii. Modo OFB, porque ... 
    iii. Se pasaron los parametros: key, iv y el texto encriptado, porque si se cambian, no se podria desencriptar
2.
    i. Modo OFB, porque ... 
    ii. Se pasaron los parametros: key, iv y el texto encriptado, porque si se cambian, no se podria desencripta
    iii. La llave y el vector inicial, son las mas importantes
"""

def convertir_16_bytes(data, is_key=False):
    len_data = len(data)

    # Verificamos si es llave para utilizar solo los primeros 16 bytes de la llave
    if is_key:
        r = len_data % 16
        if r != 0:
            # Si la llave no es congruente a 16 bytes entonces se completa para que sea de 16 bytes
            for i in range(16-r):
                data += '0'
        return data[0:16]

    if len_data / 16 == 1:
        # Si la data es de 16 bytes se conserva como es
        return [data]
    elif len_data % 16 == 0:
        # Si la data es congruente a 16 bytes, pero mayor a 16 bytes, se divide en partes de 16 bytes
        data_list = []
        str_bytes_16 = ""

        for i in data:
            str_bytes_16 += i
            if len(str_bytes_16) == 16:
                data_list.append(str_bytes_16)
                str_bytes_16 = ""
        return data_list
    else:
        # Si la data no es congruente a 16 bytes, se completa
        r = len_data % 16
        for i in range(16-r):
            data += '`'
        return convertir_16_bytes(data)


def menu():
    print(
        """
            Menu:
        1. Encriptar texto
        2. Desencriptar texto
        3. Encriptar archivo
        4. Desencriptar archivo
        5. Salir
        """
    )

continuar = True
iv = get_random_bytes(16)

while continuar:
    menu()
    opcion = input("Ingrese una opcion: \n > ")

    if opcion == '1':
        key = input("Ingrese una llave: \n > ")
        key = convertir_16_bytes(key, is_key=True)
        data = input("Ingrese un texto a encriptar: \n > ")
        data = convertir_16_bytes(data)

        # Se instancia el vector inicial con 16 bytes random
        # Se crea el AES con la llave y el vector inicial
        aes = AES.new(key, AES.MODE_OFB, iv)

        encrypted_list = []
        for d in data:
            encrypted_list.append(aes.encrypt(d))
        print(encrypted_list)

    elif opcion == '2':
        key = input("Para desencriptar el mensaje ingrese la llave: \n > ")
        key = convertir_16_bytes(key, is_key=True)

        # Se crea el AES con la llave y el vector inicial
        aes = AES.new(key, AES.MODE_OFB, iv)

        decrypted_list = []
        for e in encrypted_list:
            try:
                decrypted_list.append(aes.decrypt(e).decode("utf-8"))
            except:
                pass
        decrypted = "".join(decrypted_list).replace('`', '')
        print(">>> ", decrypted)

    elif opcion == '3':
        key = input("Ingrese una llave: \n > ")
        key = convertir_16_bytes(key, is_key=True)
        
        # Se crea el AES con la llave y el vector inicial
        aes = AES.new(key, AES.MODE_OFB, iv)

        with open('./file_prueba.txt', 'r') as doc:
            doc_data = doc.read()
            doc_data = convertir_16_bytes(doc_data)

            encrypted_list = []
            for d in doc_data:
                encrypted_list.append(aes.encrypt(d))
            doc.close()

        with open('./file_encrypted.txt', 'w') as doc:
            doc.write(str(encrypted_list))
            doc.close()

    elif opcion == '4':
        key = input("Para desencriptar el mensaje ingrese la llave: \n > ")
        key = convertir_16_bytes(key, is_key=True)

        # Se crea el AES con la llave y el vector inicial
        aes = AES.new(key, AES.MODE_OFB, iv)
        decrypted = None

        with open('./file_encrypted.txt', 'r') as doc:
            doc_data = doc.read()
            encrypted_list = ast.literal_eval(doc_data)

            decrypted_list = []
            for e in encrypted_list:
                try:
                    decrypted_list.append(aes.decrypt(e).decode("utf-8"))
                except:
                    pass
            decrypted = "".join(decrypted_list).replace('`', '')
            doc.close()

        with open('./file_decrypted.txt', 'w') as doc:
            doc.write(decrypted)
            doc.close()

    elif opcion == '5':
        continuar = False
        print("Bye")
    else:
        print("Opcion invalida")
