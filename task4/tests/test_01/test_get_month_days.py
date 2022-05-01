from simple_library_01.functions import get_month_days
import pytest


def test_get_month_days():
    assert 30 == get_month_days(1930, 12)
    assert 29 == get_month_days(2000, 2)
    assert 28 == get_month_days(2001, 2)
    with pytest.raises(AttributeError):
        get_month_days(2003, 13)
    assert 30 == get_month_days(2011, 4)
    assert 31 == get_month_days(2021, 12)