import rsa

(publicKey, privateKey) = rsa.newkeys(512)

message = input("Ingrese un mensaje: ")
message = message.encode('utf-8')

cryto_message = rsa.encrypt(message, publicKey)
print(cryto_message)

decrypted_message = rsa.decrypt(cryto_message, privateKey)
print(decrypted_message.decode('utf-8'))
