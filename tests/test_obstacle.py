from src.obstacle_detection import detect_obstacles

def test_obstacle():
    assert detect_obstacles([10,2,3],5) == [2,3]
