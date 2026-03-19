def time_to_collision(distance, speed):
    """
    Calculate Time To Collision.
    """
    if speed == 0:
        return float('inf')

    ttc = distance / speed
    return ttc


if __name__ == "__main__":
    print(time_to_collision(100, 20))
