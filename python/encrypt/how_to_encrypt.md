 # 暗号化に用いる python ライブラリ
 ### ライブラリ
 - PyCryptodome
  - https://pycryptodome.readthedocs.io/en/latest/src/introduction.html 
  - 以下のコードで暗号化ができる

```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# encrypt
data = b'secret data'

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

data = cipher.decrypt_and_verify(ciphertext, tag)
# decrypt

```
 
 - 疑問点
  - じゃあこの鍵はどこに保存すればよいのか？環境変数でよいのか？
 - pyca/cryptography
  - https://cryptography.io/en/latest/