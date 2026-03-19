from src.sensor_fusion import sensor_fusion

def test_fusion():
    assert sensor_fusion([10],[20]) == [15]
