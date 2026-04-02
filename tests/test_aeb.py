import pytest
from aeb import apply_brakes


def test_brake_applied():
    assert apply_brakes(2, 3) is True

def test_brake_not_applied():
    assert apply_brakes(5, 3) is False

def test_brake_boundary():
    assert apply_brakes(3, 3) is False

def test_brake_zero_ttc():
    assert apply_brakes(0, 3) is True

@pytest.mark.parametrize("ttc, threshold, expected", [
    (2, 3, True),
    (5, 3, False),
    (3, 3, False),
    (0, 3, True),
])
def test_multiple_cases(ttc, threshold, expected):
    assert apply_brakes(ttc, threshold) == expected

def test_invalid_ttc():
    with pytest.raises(TypeError):
        apply_brakes("2.5", 3)

def test_negative_ttc():
    with pytest.raises(ValueError):
        apply_brakes(-1, 3)
