def detect_obstacles(sensor_data, threshold=5):
    """
    Detect obstacles closer than threshold.
    """
    obstacles = []
    for distance in sensor_data:
        if distance < threshold:
            obstacles.append(distance)

    return obstacles


if __name__ == "__main__":
    print(detect_obstacles([10, 2, 3, 7], 5))
