def validate_sensor_data(data):
    return all(d >= 0 for d in data)
