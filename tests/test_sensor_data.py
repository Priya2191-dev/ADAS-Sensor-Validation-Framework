from validation.sensor_validator import SensorDataValidator

def test_sensor_data_validation():

    validator = SensorDataValidator()

    result = validator.validate_sensor_data("data/sensor_sample_data.csv")

    assert result == True
