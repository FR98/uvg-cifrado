from os import urandom
from hashlib import sha1
from random import shuffle, choice

puzzle_size = 2 ** 16

def merkles_puzzle():
    secrets = [None] * puzzle_size
    puzzles = [None] * puzzle_size
    
    for i in range(puzzle_size):
        # Generar secreto
        secrets[i] = urandom(16)
        # pair = secret|index
        pair = secrets[i] + int.to_bytes(i, 4, 'big')
        # plaintext = pair|sha1(pair)
        plaintext = pair + sha1(pair).digest()
        # cipthertext = ENCRYPT(plaintext, key)
        key = urandom(10)
        noise = sha1(key).digest()
        noise += sha1(noise).digest()
        ciphertext = bytes(i ^ j for i, j in zip(plaintext, noise))
        # puzzle = ciphertext|key
        puzzles[i] = ciphertext + key[2:]
    # Orden random
    shuffle(puzzles)
    return secrets, puzzles
    
def solve_puzzle(puzzle):
    ciphertext = puzzle[:40]
    key = puzzle[40:]
    
    for i in range(puzzle_size):
        noise = sha1(int.to_bytes(i, 2, 'big') + key).digest()
        noise += sha1(noise).digest()
        # plaintext := DECRYPT(ciphertext, key)
        plaintext = bytes(i ^ j for i, j in zip(ciphertext, noise))
        # pair|digest := key|index|sha1(pair)
        pair = plaintext[:20]
        digest = plaintext[20:]
        if sha1(pair).digest() == digest:
            return i, pair[:16], int.from_bytes(pair[16:], 'big')

alice_secrets, public_puzzles = merkles_puzzle()

bob_time, bob_secret, public_index = solve_puzzle(choice(public_puzzles))
    
print('Bob: ')
print('\tKey: ', bob_secret)
print('\tIndex: ', public_index)
print('\tSteps executed: ', bob_time)

print('Alice: ')
print('\tkey: ', alice_secrets[public_index])

total_time, total_puzzles = 0, 0

for puzzle in public_puzzles:
    time, key, index = solve_puzzle(puzzle)
    total_time += time
    total_puzzles += 1
    
    if index == public_index:
        print('\nEl adversario encontro el secreto: ', key)
        break
    
    if total_time > bob_time * 100:
        print('\nEl adversario no pudo encontrar el secreto')
        break
    
print('Puzzles: {} pasos ejecutados {}'.format(total_puzzles, total_time))
