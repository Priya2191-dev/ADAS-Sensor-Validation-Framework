from src.ttc import time_to_collision

def test_ttc_basic():
    assert time_to_collision(100, 20) == 5

def test_ttc_zero_speed():
    assert time_to_collision(100, 0) == float('inf')

def test_ttc_zero_distance():
    assert time_to_collision(0, 20) == 0

def test_ttc_float_values():
    assert round(time_to_collision(50, 3), 2) == round(16.6667, 2)
