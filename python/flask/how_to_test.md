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

## テストの前処理を定義する方法
### fixture を使用する方法
 - @pytest.fixture() を付与した関数内の処理を呼び出すことができる
 - 以下の例では、test_sample() に hoge() を渡すことで、test_sample() の前に hoge() が呼び出される。

```python:test.py
import pytest

@pytest.fixture()
def hoge():
    print("setup")
    message = "hoge"
    return message

class TestApp:
    def test_sample(self, hoge):
        print(hoge)
```

 事前処理として "setup" が出力されている

``` shell
# command
pytest test.py -s

# 出力
test.py setup
hoge
.
```

 事前処理だけでなく、事後処理を定義することもできる
 また、戻り値を yield で返すことにより、各テスト関数の事後処理も記述できる  
 (request-context オブジェクトであれば 「addfinalizer に事後処理となるメソッドを渡す」という方法がより安全であるが、ここでは割愛する)  

```python
import pytest

@pytest.fixture()
def hoge():
    print("setup")
    message = "hoge"
    yield message
    print("teardown")

class TestApp:
    def test_sample(self, hoge):
        print(hoge)
```

 テスト関数が終了した後に、hoge() で定義した事後処理が実行されている

``` shell
# command
pytest test.py -s

# 出力
test.py setup
hoge
.teardown
```

 関数単位ではなく、クラス単位やモジュール単位で事前処理を行いたい場合は scope を設定するとよい  

```python
import pytest

@pytest.fixture(scope='class')
def hoge():
    print("setup")
    message = "hoge"
    yield message
    print("teardown")

class TestApp:
    def test_sample(self):
        print(hoge)

    def test_sample2(self):
        print(hoge)
```

 各テスト関数毎ではなく、クラス単位で fixture が呼び出されている

``` shell
# command
pytest test.py -s

# 出力結果
test.py setup
hoge
.hoge
.teardown
```

### scope について
 scope を定義することで fixture が呼び出されるタイミングと、事後処理が呼び出されるタイミングを定義できる  
 以下の 5 つのいずれかを定義できる (デフォルトは function)  
 1. function
 1. class
 1. module
 1. package
 1. session

 指定した単位で fixture で定義された事前処理と事後処理が呼び出される

#### session を扱う際の注意点
 - テストモジュール内で fixture を定義した上で複数のモジュールを実行すると、1度のテスト実行でモジュールの数だけ fixture が呼び出されてしまう。
 - 以下の構成で test_app.py に fixture を定義し、tests/ 以下のテストを実行すると、fixture が 2 回呼び出されてしまう

```
  root
  ├─ src
  │   └─ app.py
  └─ tests
      ├─ test_app.py
      └─ test_app2.py
```

 - その場合は confest.py に fixture を定義すると、scope が正しく機能する

```
  root
  ├─ src
  │   └─ app.py
  └─ tests
      ├─ conftest.py
      ├─ test_app.py
      └─ test_app2.py
```

### confest.py を使用する方法
 - 
