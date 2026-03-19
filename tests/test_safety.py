from src.safety_scenario import safety_scenario

def test_safety():
    assert safety_scenario(70,3) == "HIGH RISK"
