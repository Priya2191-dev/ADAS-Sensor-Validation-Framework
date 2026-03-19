from obstacle_detection import detect_obstacles

def test_detect_obstacles_basic():
    assert detect_obstacles([10, 2, 3, 7], 5) == [2, 3]

def test_detect_obstacles_no_obstacle():
    assert detect_obstacles([10, 8, 6], 5) == []

def test_detect_obstacles_all_obstacles():
    assert detect_obstacles([1, 2, 3], 5) == [1, 2, 3]

def test_detect_obstacles_empty():
    assert detect_obstacles([], 5) == []
