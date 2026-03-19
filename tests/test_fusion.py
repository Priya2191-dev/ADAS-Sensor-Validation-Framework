from sensor_fusion import sensor_fusion

def test_basic_fusion():
    assert sensor_fusion([10], [20]) == [15]

def test_multiple_values():
    assert sensor_fusion([10, 20], [20, 30]) == [15, 25]

def test_empty_input():
    assert sensor_fusion([], []) == []

def test_unequal_length():
    assert sensor_fusion([10, 20], [30]) == [20]
