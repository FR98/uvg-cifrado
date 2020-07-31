## IMPORTANTE: Ejecutar con python 2
"""
m = multiplicador
c = incremento
n = modulo
states_number = cantidad de estados
"""

import random

def lcg(m, c, n, seed, states_number):
    list_states = []
    state = seed
    for i in range(states_number):
        state = (state * m + c) % n
        list_states.append(state)
    return list_states

m = 1584654197449762
c = 429335945204311
n = 583521704611601
seed = 123
states_number = 3

print("Multiplicador =", m)
print("Incremento =", c)
print("Modulo =", n)
print("Semilla =", seed)
print("Cantidad de estados =", states_number)

list_states = lcg(m, c, n, seed, states_number)
for index, state in enumerate(list_states, start=1):
    print("s"+str(index)+":", state)

print("////////////////////////////////")

m = 915451635481687
c = 5886893188886454
n = 6108133789056532
seed = 123
states_number = 4

print("Multiplicador =", m)
print("Incremento =", c)
print("Modulo =", n)
print("Semilla =", seed)
print("Cantidad de estados =", states_number)

print ("\n\nA:\n")
list_states = lcg(m, c, n, seed, states_number)
for index, state in enumerate(list_states, start=1):
    print("s"+str(index)+":", state)

print("\n\nB:\n")
x2 = 1251340539300040
x1 = 1526203935246140
m = 7544713835650436
n = 3059121001727213
#(x2/m) + mx1 + c = 0
resultado = (x2 - x1*m) % n
x3 = (x2*m+ resultado) % n
print ( "Incremento: {}\n".format((x2 - x1*m) % n ))
print("s3={}".format(x3))

def mcd(a, b):
    resto = 0
    while (b>0):
        resto = b
        b = a%b
        a = resto
    return a
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

print("\n\nC:\n")

x1 = 1617562532769340
x2 = 2688456964915964
x3 = 2557694464258732
n  = 3173287219423490

print( "MCD="+str(mcd((x1/2-x2/2), n/2 ) ))

print("\n")
inverso = MMI((x1/2-x2/2) , n/2)
# inverso = 93727606880267
print("Inverso multiplicativo es " + str(inverso))

print((inverso * (x1-x2) )%n/2)

m0 = (inverso * (x2-x3))%n/2
m1 = m0 + n/mcd(x1-x2 , n)
print (m0)
print(m1)
print ("CON M1")
print ((x2 - m0*x1) % n)
print((x3 - m0*x2) % n)

print ("CON M2")
print((x2-m1*x1) % n)
print((x3-m1*x2) % n)

#Como son el mismp:
c = (x3-m1*x2) % n

s4 = (m0*x3 + c)%n
print("s4="+str(s4))
