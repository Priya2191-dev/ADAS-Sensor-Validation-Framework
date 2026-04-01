from typing import List, Union

Number = Union[int, float]

def validate_sensor_data(data: List[Number]) -> bool:
    """
    Validate sensor data:
    - No negative values
    - All values must be numeric
    """

    # Input validation
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All sensor values must be numeric")

    # Core logic
    return all(value >= 0 for value in data)


if __name__ == "__main__":
    print(validate_sensor_data([10, 5, 3]))
