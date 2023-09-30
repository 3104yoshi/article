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

# 同じ key を使用しても cipher が異なる場合、元のデータがおなしでも暗号化後のデータは異なる
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

# decrypt
data = cipher.decrypt_and_verify(ciphertext, tag)

```

- pyca/cryptography
- https://cryptography.io/en/latest/

- bytes 型の key の保存方法
- ファイルに保存
  - バイナリモードでファイルを開閉する
- 環境変数に保存
  - 読み込むときにバイト列が文字列として読み込まれてしまうので、16進数、あるいは文字列に変換する必要がある
  - 文字列として保存 (非推奨)
    - ランダムな bytes 列だと文字列にエンコードできない場合がある。
    - 文字列で保存したい場合は ランダムな文字列を生成してそれをデコードする、みたいなことをしないといけないので面倒
  - 16 進数として保存 (推奨)
    - バイト列を機械的に変換したものを保存し、使用するときはそれをデコードするば良い

- AES mode
- GCM
  - パフォーマンス、セキュリティなど様々な観点から優れているが、実装が複雑になる
  - 他人が実装してくれるなら GCM は最高
  - 特許なし
- OCB
  - パフォーマンス良い
  - https://www.cs.ucdavis.edu/~rogaway/ocb/ が特許保持
    - そのため、GPL ライセンス (フリーライセンス) なら問題ないが、商用利用するなら課金の必要あり
- EAX
  - デメリット : GCM, OCB と比較するとパフォーマンスに劣る
  - メリット
    - 特許なし
    - 実装しやすい
- 参考 https://blog.cryptographyengineering.com/2012/05/19/how-to-choose-authenticated-encryption/
