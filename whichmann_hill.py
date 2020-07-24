# [r, s1, s2, s3] = function(s1, s2, s3) is
# // s1, s2, s3 should be random from 1 to 30,000. Use clock if available.
# s1 := mod(171 * s1, 30269)
#     s2 := mod(172 * s2, 30307)
#     s3 := mod(170 * s3, 30323)

#     r := mod(s1/30269.0 + s2/30307.0 + s3/30323.0, 1)

import random

def wichmann_hill(seed=30000):
    s1 = random.randrange(1, seed)
    print("Generando seed aleatoria 1: {}".format(s1))
    s2 = random.randrange(1, seed)
    print("Generando seed aleatoria 2: {}".format(s2))
    s3 = random.randrange(1, seed)
    print("Generando seed aleatoria 3: {}".format(s3))


    x = (171 * s1) % 30269
    print("Operando la semilla 1: {}".format(x))
    y = (172 * s2) % 30307
    print("Operando la semilla 2: {}".format(y))
    z = (170 * s3) % 30323
    print("Operando la semilla 3: {}".format(z))

    return (x/30269.0 + y/30307.0 + z/30323.0) % 1

for r in range(0, 5):
    print("\nIMPLEMENTACION {}\n".format(r+1))
    print("\nRESULTADO: ",wichmann_hill())