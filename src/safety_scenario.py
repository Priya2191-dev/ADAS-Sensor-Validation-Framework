def safety_scenario(speed, obstacle_distance):
    if speed > 60 and obstacle_distance < 5:
        return "HIGH RISK"
    return "SAFE"
