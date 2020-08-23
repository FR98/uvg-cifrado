from Crypto.Cipher import AES
import binascii, os
from base64 import b64encode

def encrypt_AES_GCM(msg, key):
    aesCipher = AES.new(key, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(encryptedMsg, key):
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(key, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

key = os.urandom(32)
print("Key:", binascii.hexlify(key))

msg = input('Ingrese un mensage: ')
msg = bytes(msg, 'utf-8')

encryptedMsg = encrypt_AES_GCM(msg, key)
print('Mensaje encriptado:')
print('\tMensaje cifrado: ', binascii.hexlify(encryptedMsg[0]))
print('\tAES IV: ', binascii.hexlify(encryptedMsg[1]))
print('\tAuth Tag: ', binascii.hexlify(encryptedMsg[2]))

decryptedMsg = decrypt_AES_GCM(encryptedMsg, key)
print("\nMensaje descifrado: ", decryptedMsg)
