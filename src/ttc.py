from typing import Union

Number = Union[int, float]

def time_to_collision(distance: Number, speed: Number) -> float:
    """
    Calculate Time To Collision (TTC).

    :param distance: Distance to obstacle
    :param speed: Relative speed
    :return: Time to collision (float or inf)
    """

    # Input validation
    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric")

    if not isinstance(speed, (int, float)):
        raise TypeError("speed must be numeric")

    if distance < 0:
        raise ValueError("distance cannot be negative")

    if speed < 0:
        raise ValueError("speed cannot be negative")

    # Core logic
    if speed == 0:
        return float('inf')

    return distance / speed
