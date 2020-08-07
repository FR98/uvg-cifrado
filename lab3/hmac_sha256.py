import hashlib
import hmac
from base64 import b64encode

def hmacSha256(msg, key):
    # Python 2
    message = bytes(msg).encode('utf-8')
    secret = bytes(key).encode('utf-8')

    # Python 3
    # message = bytes(msg, 'utf-8')
    # secret = bytes(key, 'utf-8')
    
    return b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())

print(hmacSha256('Cifrado de informacion seccion 10', 'CC3078'))
print(hmacSha256('La implementacion de este ejercicio fue sencilla', 'MAC'))


# Implementacion del timing attack extraida de
# https://github.com/sqreen/DevelopersSecurityBestPractices/tree/master/_practices/timing-attack/_python

# To run
# pip install -r requirements.txt
# gunicorn -w 1 app:app
# python hack.py
