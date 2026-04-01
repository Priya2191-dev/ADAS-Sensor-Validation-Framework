import logging
from typing import List, Union

# Configure logging
logging.basicConfig(level=logging.INFO)

Number = Union[int, float]

def detect_obstacles(sensor_data: List[Number], threshold: Number = 5) -> List[Number]:
    """
    Detect obstacles closer than the given threshold.

    :param sensor_data: List of distance values from sensors
    :param threshold: Distance threshold
    :return: List of detected obstacles
    """

    # Input validation
    if not isinstance(sensor_data, list):
        raise TypeError("sensor_data must be a list")

    if not all(isinstance(d, (int, float)) for d in sensor_data):
        raise ValueError("All sensor values must be numeric")

    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold must be numeric")

    # Core logic (Pythonic)
    obstacles = [d for d in sensor_data if d < threshold]

    logging.info(f"Input: {sensor_data}, Threshold: {threshold}, Obstacles: {obstacles}")

    return obstacles
