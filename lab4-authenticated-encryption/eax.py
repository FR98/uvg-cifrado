from tomcrypt import cipher

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
        return data_list[0]
    else:
        # Si la data no es congruente a 16 bytes, se completa
        r = len_data % 16
        for i in range(16-r):
            data += '0'
        return convertir_16_bytes(data)


key = input('Ingrese una llave para encriptar: ')
key = convertir_16_bytes(key, is_key=True)
key = bytes(key, 'utf-8')

message = input('Ingrese un mensaje para encriptar: ')
message = convertir_16_bytes(message, is_key=True)
message = bytes(message, 'utf-8')

my_cipher = cipher.aes(key, b'\0' * 16, mode='eax', nonce=b'random', header=b'a header') 
cifrado = my_cipher.encrypt(message)
print(cifrado)
my_cipher.done()

my_cipher = cipher.aes(key, b'\0' * 16, mode='eax', nonce=b'random', header=b'a header') 
print(my_cipher.decrypt(cifrado)) 
my_cipher.done() 
