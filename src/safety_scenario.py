def safety_scenario(speed, obstacle_distance):
    """
    Evaluate driving safety scenario based on speed and obstacle distance.
    """
    
    if not isinstance(speed, (int, float)):
        raise TypeError("speed must be numeric")

    if not isinstance(obstacle_distance, (int, float)):
        raise TypeError("obstacle_distance must be numeric")

    if speed > 60 and obstacle_distance < 5:
        return "HIGH RISK"
    elif speed < 40:
        return "SAFE"
    else:
        return "MODERATE"
