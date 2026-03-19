def validate_sensor_data(data):
    """
    Validate sensor data (no negative values).
    """
    for value in data:
        if value < 0:
            return False

    return True


if __name__ == "__main__":
    print(validate_sensor_data([10, 5, 3]))
