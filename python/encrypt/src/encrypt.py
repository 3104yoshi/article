from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(cipher.nonce)
print(tag)
print(ciphertext)

cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)