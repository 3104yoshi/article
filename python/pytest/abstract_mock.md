## 【pytest】 pytest において mock を生成する方法
### 概要
mock の生成方法が複数存在し、複雑だったので整理した。


### mockとは
mock を知らない人のために簡単に説明を。

- テストにおける mock とは、テストに必要なオブジェクトを代替するもの。  
- mock を使用することで、オブジェクトの属性や戻り値を自由に設定できる
- DB から値を取得する必要のあるメソッドをテストしたい時などに重宝する

### mock を生成する方法
1.  unittest.mocker.patch を使用する
    - 以下のいずれかの方法で指定したオブジェクトを mock 化できる
        - @patch() アノテーションを使用する
        - patch() メソッドを使用する
            - with 文で生成可能
            
    - 以下の例では os.getcwd() メソッドの戻り値を固定している

    ```python
    import os
    from unittest.mock import patch
    class TestApp:
        @patch('os.getcwd')
        def test_with_mock_patch(self, mock_getcwd):
            mock_getcwd.return_value = 'mocked'
            print(f"cwd={os.getcwd()}")

        def test_with(self):
            with patch('os.getcwd') as mock:
                mock.return_value = 'mocked-with'
                print(f"with={os.getcwd()}")

    # 実行結果
    # cwd=mocked
    # .with=mocked-with
    ```
    - 以下のように、patch() 内で戻り値を定義することもできる
    
    ```python
    import os
    from unittest.mock import patch
    class TestApp:
        @patch('os.getcwd', return_value = 'mocked')
        def test_with_mock_patch(self, mock_getcwd):
            print(f"cwd={os.getcwd()}")

        def test_with(self):
            with patch('os.getcwd', return_value = 'mocked-with') as mock:
                print(f"with={os.getcwd()}")

    # 実行結果
    # cwd=mocked
    # .with=mocked-with
    ```

1. pytest-mock
    - @pytest.fixture を付与したメソッドに mocker を渡す
    - fixture を用いて mock を定義しているので、テスト後に自動でモックが破棄される

    ```python
    import os
    import pytest

    @pytest.fixture()
    def fixture_pytest_mocker(mocker):
        return mocker.patch(
            'os.getcwd', return_value='mocked'
        )

    def test_pytest_mock(fixture_pytest_mocker):
        print(f"pytest_mocker={os.getcwd()}")

    # 実行結果
    # pytest_mocker=mocked
    ```

### 各方法のメリットとデメリットについて
1. unittest.mocker.patch
    - メリット
        - Python 標準ライブラリの機能であるため、追加でライブラリをインポートする必要がない
    - デメリット
        - pytest-mock と比較して冗長なコードになりがち  

1. pytest-mock
    - メリット
        - fixture で mock を簡単に管理でき、コードが簡潔になる
    - デメリット
        - pytest を追加でインポートする必要がある

### まとめ
pytest を使える環境なら、2 の pytest-mock を使用する方がコードが簡潔になって良さそう