from typing import Union

Number = Union[int, float]

def apply_brakes(ttc: Number, threshold: Number = 3) -> bool:
    """
    Decide whether to apply brakes based on Time To Collision (TTC).

    :param ttc: Time to collision
    :param threshold: Safety threshold
    :return: True if brakes should be applied
    """

    # Input validation
    if not isinstance(ttc, (int, float)):
        raise TypeError("ttc must be numeric")

    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold must be numeric")

    if ttc < 0:
        raise ValueError("ttc cannot be negative")

    if threshold < 0:
        raise ValueError("threshold cannot be negative")

    # Core logic
    return ttc < threshold


if __name__ == "__main__":
    print(apply_brakes(2.5))
