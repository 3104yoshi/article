import pytest
import os
from unittest.mock import Mock, patch

@pytest.fixture()
def fixture_pytest_mocker(mocker):
    return mocker.patch(
        'os.getcwd', return_value='mocked'
    )

class TestApp:
    @patch('os.getcwd')
    def test_with_mock_patch(self, mock_getcwd):
        mock_getcwd.return_value = 'mocked'
        print(f"cwd={os.getcwd()}")

    def test_pytest_mock(self, fixture_pytest_mocker):
        print(f"pytest_mocker={os.getcwd()}")
    
    def test_directlymock(self):
        my_mock = Mock()
        my_mock.return_value = 'mocked'
        os.getcwd = my_mock
        print(os.getcwd())
    
    def test_with(self):
        with patch('os.getcwd') as mock:
            mock.return_value = 'mocked'
            print(f"with={os.getcwd()}")
    
    def test_raw_getcwd(self):
        print(f"test_raw_getcwd={os.getcwd()}")