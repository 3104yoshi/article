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

 - AES mode
  - GCM 
    - パフォーマンス、セキュリティなど様々な観点から優れているが、実装が複雑になる
    - 他人が実装してくれるなら GCM は最高
    - 特許なし
  - OCB 
    - パフォーマンス良い
    - https://www.cs.ucdavis.edu/~rogaway/ocb/ が特許保持
      - そのため、GPLライセンス (フリーライセンス) なら問題ないが、商用利用するなら課金の必要あり
  - EAX
    - デメリット : GCM, OCB と比較するとパフォーマンスに劣る
    - メリット
      - 特許なし
      - 実装しやすい
  - 参考 https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/