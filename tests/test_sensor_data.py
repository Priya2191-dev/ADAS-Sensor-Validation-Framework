from src.sensor_data import validate_sensor_data

def test_sensor_data():
    assert validate_sensor_data([1,2,3]) is True
