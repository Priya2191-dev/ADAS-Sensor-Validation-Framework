from typing import List, Union

Number = Union[int, float]

def sensor_fusion(camera: List[Number], radar: List[Number]) -> List[float]:
    """
    Fuse camera and radar data by averaging corresponding values.

    :param camera: List of camera sensor values
    :param radar: List of radar sensor values
    :return: List of fused values
    """

    # Input validation
    if not isinstance(camera, list) or not isinstance(radar, list):
        raise TypeError("camera and radar must be lists")

    if not all(isinstance(x, (int, float)) for x in camera + radar):
        raise ValueError("All sensor values must be numeric")

    # Core logic (handles unequal length using zip)
    return [(c + r) / 2 for c, r in zip(camera, radar)]
