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

list_states = lcg(m, c, n, seed, states_number)
for index, state in enumerate(list_states, start=1):
    print("s"+str(index)+":", state)
