from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch
# from unittest.mock import mock_open, patch
# import pytest


def test_counter():
    with patch("builtins.open", mock_open(read_data="file")):
        assert count_ocurrences('path', 'FILE') == 1
