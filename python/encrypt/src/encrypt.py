import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'secret data'

data4 = b'\xac\xb3\xb3\x92\xed?\xd6-E\xa4\x0f\xec\xedGY`'

with open('keyfile', 'wb') as f:
    f.write(data4)

with open('keyfile', 'rb') as f:    
    print(f'data4={data4}')
    data5 = f.read()
    print(f'data5={data5}')
# print(data4.hex())
# raw = os.environ.get('CRYPTO_KEY')
# print(f'raw={raw}')
# print(f'raw={type(raw)}')
# # print("jkafk\ed\xajfk")
# bytes_raw = bytes.fromhex(raw)
# print(f'bytes_raw={bytes_raw}')


# print(bytes.fromhex(bytes(os.environ.get('CRYPTO_KEY'), 'utf-8').decode()))
# print(type(bytes.fromhex(bytes(os.environ.get('CRYPTO_KEY'), 'utf-8').decode())))


# print(bytes(os.environ.get('CRYPTO_KEY').fromhex()))
# print(type(os.environ.get('CRYPTO_KEY')))
# print(len(os.environ.get('CRYPTO_KEY')))
# data2 = os.environ.get('CRYPTO_KEY').encode()
# # data3 = bytes(data2, 'utf-8')
# print(data2)
# print(len(data2))
# print(type(data2))
# print(data3)

key = get_random_bytes(16)
# print(f"key={key.decode()}")
# print(f'key={key.decode()}')
print(f"key={key}")
print(f"key length={len(key)}")
print(f"key type={type(key)}")
print(f"key hex={key.hex()}")
print(f"key hex length={len(key.hex())}")
print(f"key from hex={bytes.fromhex(key.hex())}")
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(cipher.nonce)
print(tag)
print(ciphertext)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(cipher.nonce)
print(tag)
print(ciphertext)

cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print(data)