import pytest

from src.utils.app_info import get_app_version


def test_get_app_version():
    version = get_app_version()

    assert version is not None
    assert isinstance(version, str)
    assert version == "0.1.0"