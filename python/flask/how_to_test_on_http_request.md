# flask アプリケーションにおいて、HTTP リクエストを送信した時のテスト方法
## サンプルコードの構成
 root
  ├─ src
  │   └─ app.py
  └─ tests
      └─ test_app.py

 - テスト対象のコード

 ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def sample():
        return "Hello World!"

    if __name__ == '__main__':
        app.run(debug=True)
 ```

## HTTP クライアントの作成
 - Flask クラスに定義された test_client() を使用する
 - HTTP クライアントを以下のように生成し、実際にサーバーを立ち上げることなくメソッドをテストできる

 ``` python
 import app from app

 client = app.test_client()
 ```

 - テスト用のクライアントは各テストで使用するため、毎回定義する必要がある

 - fixture や confest.py を使用すると、各テスト関数内で定義する必要がなくなる