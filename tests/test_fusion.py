import pytest
from sensor_fusion import sensor_fusion


def test_basic_fusion():
    assert sensor_fusion([10], [20]) == [15.0]

def test_multiple_values():
    assert sensor_fusion([10, 20], [20, 30]) == [15.0, 25.0]

def test_empty_input():
    assert sensor_fusion([], []) == []

def test_unequal_length():
    assert sensor_fusion([10, 20], [30]) == [20.0]

@pytest.mark.parametrize("camera, radar, expected", [
    ([10], [20], [15.0]),
    ([10, 20], [20, 30], [15.0, 25.0]),
    ([], [], []),
    ([10, 20], [30], [20.0]),
])
def test_fusion_cases(camera, radar, expected):
    assert sensor_fusion(camera, radar) == expected

def test_invalid_type():
    with pytest.raises(TypeError):
        sensor_fusion("invalid", [10])

def test_non_numeric_values():
    with pytest.raises(ValueError):
        sensor_fusion([10, "a"], [20, 30])
