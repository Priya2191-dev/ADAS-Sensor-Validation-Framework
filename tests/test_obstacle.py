import pytest
from obstacle_detection import detect_obstacles


def test_detect_obstacles_basic():
    assert detect_obstacles([10, 2, 3, 7], 5) == [2, 3]

def test_detect_obstacles_no_obstacle():
    assert detect_obstacles([10, 8, 6], 5) == []

def test_detect_obstacles_all_obstacles():
    assert detect_obstacles([1, 2, 3], 5) == [1, 2, 3]

def test_detect_obstacles_empty():
    assert detect_obstacles([], 5) == []

def test_threshold_edge_case():
    assert detect_obstacles([5, 4.9], 5) == [4.9]

def test_invalid_sensor_data_type():
    with pytest.raises(TypeError):
        detect_obstacles("invalid_input", 5)

def test_non_numeric_values():
    with pytest.raises(ValueError):
        detect_obstacles([1, "a", 3], 5)

def test_invalid_threshold_type():
    with pytest.raises(TypeError):
        detect_obstacles([1, 2, 3], "5")
