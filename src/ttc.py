def time_to_collision(distance, speed):
    if speed == 0:
        return float('inf')
    return distance / speed
