# [r, s1, s2, s3] = function(s1, s2, s3) is
# // s1, s2, s3 should be random from 1 to 30,000. Use clock if available.
# s1 := mod(171 * s1, 30269)
#     s2 := mod(172 * s2, 30307)
#     s3 := mod(170 * s3, 30323)

#     r := mod(s1/30269.0 + s2/30307.0 + s3/30323.0, 1)

import random

def wichmann_hill(seed=30000):
    s1 = random.randrange(1, seed)
    s2 = random.randrange(1, seed)
    s3 = random.randrange(1, seed)

    x = (171 * s1) % 30269
    y = (172 * s2) % 30307
    z = (170 * s3) % 30323

    return (x/30269.0 + y/30307.0 + z/30323.0) % 1

for r in range(0, 25):
    print(wichmann_hill())