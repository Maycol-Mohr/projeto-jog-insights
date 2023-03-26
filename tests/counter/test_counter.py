from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch

mock_string = 'TesTe'


def test_counter():
    with patch("builtins.open", mock_open(read_data=mock_string)):
        assert count_ocurrences('path', 'tEStE') == 1
