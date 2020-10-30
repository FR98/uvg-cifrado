
"""
scrypt.py
Implementacion de scrypt para derivación de contraseñas
Inspirado y obtenido de https://passlib.readthedocs.io/en/stable/lib/passlib.hash.scrypt.html
"""
from passlib.hash import scrypt
import datetime

password = "password"
h = scrypt.using(
  salt = b'saltsaltsalt',
  salt_size = 64, # Tamano de los salt generados automaticamente dentro de la funcion
  rounds = 8, #Numero de rondas a usar
  block_size = 32, # Parametro r
  parallelism = 1, # Nivel de paralelismo a usar (parametro p). Pruebas muestran que a mayor paralelismo, mayor tiempo de procesamiento
  relaxed = True # Para que corrija automaticamente posibles errores en valores de rondas, salt, etc.
  ).hash(password)
print('Contrasena original: {}'.format(password))
print('Contrasena derivada: {}'.format(h))
print('Verificada: {}'.format(scrypt.verify(password, h)))
