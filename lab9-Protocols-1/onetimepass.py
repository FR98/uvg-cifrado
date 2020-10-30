import pyotp
#https://github.com/pyauth/pyotp/blob/develop/src/pyotp/totp.py
#pip install pytop

#Genera llave de 32 bits
rn = pyotp.random_base32()
print('Resultado de secret-generator-base-32: ',rn,'\n')

totp = pyotp.TOTP(rn) # Time-Based One Time Path
num = totp.now() # => 'PIN'
print('PIN!\nEl pin es:',num,'\n\nPor favor ingrese el pin que se le ha mandado:\n')
trynum = input()

#Verifica si es o no
if(totp.verify(trynum)):
    print('El pin es el correcto!')
else:
    print('El pin es incorrecto!')

