from typing import Union

Number = Union[int, float]

def collision_warning(distance: Number, safe_distance: Number = 4) -> bool:
    """
    Determine if a collision warning should be triggered.

    :param distance: Current distance to obstacle
    :param safe_distance: Minimum safe distance threshold
    :return: True if warning should trigger, else False
    """

    # Input validation
    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric")

    if not isinstance(safe_distance, (int, float)):
        raise TypeError("safe_distance must be numeric")

    if distance < 0:
        raise ValueError("distance cannot be negative")

    return distance < safe_distance


if __name__ == "__main__":
    print(collision_warning(3))
