def safety_scenario(speed, obstacle_distance):
    """
    Evaluate driving safety scenario.
    """
    if speed > 60 and obstacle_distance < 5:
        return "HIGH RISK"
    elif speed < 40:
        return "SAFE"
    else:
        return "MODERATE"


if __name__ == "__main__":
    print(safety_scenario(70, 3))
