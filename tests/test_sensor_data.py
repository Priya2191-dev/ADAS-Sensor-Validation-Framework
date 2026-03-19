from sensor_data import validate_sensor_data

def test_valid_data():
    assert validate_sensor_data([10, 5, 3]) is True

def test_invalid_data_negative():
    assert validate_sensor_data([10, -1, 3]) is False

def test_empty_data():
    assert validate_sensor_data([]) is True

def test_all_zero_values():
    assert validate_sensor_data([0, 0, 0]) is True
