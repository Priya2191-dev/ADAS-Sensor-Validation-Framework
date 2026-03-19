def collision_warning(distance, safe_distance=4):
    """
    Check if collision warning should trigger.
    """
    if distance < safe_distance:
        return True
    else:
        return False


if __name__ == "__main__":
    print(collision_warning(3))
