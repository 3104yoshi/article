

## テストの前後処理を定義する方法
### fixture を使用する
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
 その場合は、以下のように戻り値を yield で返せばよい  
 (request-context オブジェクトであれば 「addfinalizer に事後処理となるメソッドを渡す」という方法がより安全であるそうだが、ここでは割愛する)  

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

 - その場合は後述の confest.py に fixture を定義すると、scope が正しく機能する

```
  root
  ├─ src
  │   └─ app.py
  └─ tests
      ├─ conftest.py
      ├─ test_app.py
      └─ test_app2.py
```

### confest.py について
 - fixture を conftest.py で定義することで、同じディレクトリにある複数のテストモジュールで fixture が使用できるようになる
 - また、上位のディレクトリにある conftest 内で定義された fixture は使用できるが、下位のものは使用できない。

 以下の例であれば、test_app3.py からは tests/conftest.py を使用できる。  
 一方、test_app.py からは test_dir2/conftest.py は使用できない。

ディレクトリ構成
```
 root
  └─ tests
      ├─ conftest.py
      ├─ test_app.py
      └─ test_dir2
           ├─ conftest.py
           └─ test_app2.py
```
サンプルコード
```python:tests/conftest.py
# tests/conftest.py
import pytest

@pytest.fixture(scope="function")
def hoge():
    print("start")
    message = "ほげ"

    yield message

    print("done")
```
```python:tests/test_app.py
# tests/conftest.py
class TestApp:
    def test_sample(self, hoge):
        print(hoge)

    def test_sample2(self, hoge):
        print(hoge)

class TestApp1_2:
    def test_sample(self, hoge):
        print(hoge)
```
```python:test_dir2/conftest.py
import pytest

@pytest.fixture(scope="function")
def hoge2():
    # setup
    print("start2")
    message = "ほげ2"

    yield message

    print("done2")
```
```python:test_dir2/test_app2.py
class TestApp2:
    # 上位ディレクトリの conftest.py に定義された fixture は使用可能
    def test_sample(self, hoge):
        print(hoge)

    def test_sample2(self, hoge2):
        print(hoge2)
```
以下の実行結果から、test_app2.py で上位にある fixture を呼び出せている
``` shell
# command in root/tests/
pytest -s

# 出力結果
test_app.py start
ほげ
.done
start
ほげ
.done
start
ほげ
.done

test_dir2\test_app2.py start
ほげ
.done
start2
ほげ2
.done2
```