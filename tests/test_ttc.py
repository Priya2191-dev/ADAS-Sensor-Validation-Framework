from src.ttc import time_to_collision

def test_ttc():
    assert time_to_collision(100,20) == 5
