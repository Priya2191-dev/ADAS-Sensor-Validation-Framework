import pytest
from ttc import time_to_collision


def test_ttc_basic():
    assert time_to_collision(100, 20) == 5.0

def test_ttc_zero_speed():
    assert time_to_collision(100, 0) == float('inf')

def test_ttc_zero_distance():
    assert time_to_collision(0, 20) == 0.0

def test_ttc_float_values():
    assert round(time_to_collision(50, 3), 2) == 16.67

@pytest.mark.parametrize("distance, speed, expected", [
    (100, 20, 5.0),
    (0, 20, 0.0),
    (50, 5, 10.0),
])
def test_multiple_cases(distance, speed, expected):
    assert time_to_collision(distance, speed) == expected

def test_invalid_distance():
    with pytest.raises(TypeError):
        time_to_collision("100", 20)

def test_invalid_speed():
    with pytest.raises(TypeError):
        time_to_collision(100, "fast")

def test_negative_distance():
    with pytest.raises(ValueError):
        time_to_collision(-10, 20)

def test_negative_speed():
    with pytest.raises(ValueError):
        time_to_collision(100, -5)
