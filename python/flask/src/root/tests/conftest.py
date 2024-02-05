import pytest

@pytest.fixture(scope="function")  # fixtureの宣言
def hoge():
    # setup
    print("start")
    message = "ほげ"

    yield message

    print("done")