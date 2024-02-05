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

# 同じ key を使用しても cipher が異なる場合、元のデータが同じでも暗号化後のデータは異なる
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
    - 文字列として保存してしまうと、読み込み時に \ がエスケープされてしまい、バイト列が書き変わってしまう
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


### どの暗号化の手法を選ぶべきか
#### 復号する必要がないもの
 - ハッシュ関数を使用する
  - チェックサム
  - パスワード保存
 - ライブラリ
  - bcrypt
 - 注意点
  - ハッシュ化されたパスワードが流出した場合に備えて、ソルトの付加は必須
   - ハッシュ値だけだと、「ハッシュ値が同じ = パスワードが同じ」が成り立ってしまう
     - 同じパスワードであることがわかると、簡単なパスワードである可能性が高い
   - 見かけのパスワード長を長くして解読されるまでの時間を稼ぐ
 - tips
  - pepper を適切に使用すると更に安全になる
   　
#### 復号する必要があるもの
  - 共通鍵 : AES
  - 公開鍵 : RSA
