import pytest
from sensor_data import validate_sensor_data


def test_valid_data():
    assert validate_sensor_data([10, 5, 3]) is True

def test_invalid_data_negative():
    assert validate_sensor_data([10, -1, 3]) is False

def test_empty_data():
    assert validate_sensor_data([]) is True

def test_all_zero_values():
    assert validate_sensor_data([0, 0, 0]) is True

@pytest.mark.parametrize("data, expected", [
    ([10, 5, 3], True),
    ([10, -1, 3], False),
    ([], True),
    ([0, 0, 0], True),
])
def test_multiple_cases(data, expected):
    assert validate_sensor_data(data) == expected

def test_invalid_type():
    with pytest.raises(TypeError):
        validate_sensor_data("invalid")

def test_non_numeric_values():
    with pytest.raises(ValueError):
        validate_sensor_data([10, "a", 3])
