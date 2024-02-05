import pytest

@pytest.fixture(scope="function")
def hoge2():
    # setup
    print("start2")
    message = "ほげ2"

    yield message

    print("done2")