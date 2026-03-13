from validation.time_to_collision import TimeToCollision


def test_ttc_calculation():

    ttc_system = TimeToCollision()

    distance = 40
    speed = 20

    ttc = ttc_system.calculate_ttc(distance, speed)

    assert ttc == 2


def test_ttc_risk_level():

    ttc_system = TimeToCollision()

    result = ttc_system.evaluate_risk(1.5)

    assert result == "CRITICAL"
