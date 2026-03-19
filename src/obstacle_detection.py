def detect_obstacles(sensor_data, threshold=5):
    return [d for d in sensor_data if d < threshold]
