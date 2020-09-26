import rsa

(publicKey, privateKey) = rsa.newkeys(128)

print(publicKey)
print()
print(privateKey)
