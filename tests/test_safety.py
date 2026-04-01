import pytest
from safety_scenario import safety_scenario


def test_high_risk():
    assert safety_scenario(70, 3) == "HIGH RISK"

def test_safe_low_speed():
    assert safety_scenario(30, 10) == "SAFE"

def test_moderate_case():
    assert safety_scenario(50, 6) == "MODERATE"

def test_edge_case():
    assert safety_scenario(60, 5) == "MODERATE"

def test_invalid_speed():
    with pytest.raises(TypeError):
        safety_scenario("fast", 3)

def test_invalid_distance():
    with pytest.raises(TypeError):
        safety_scenario(70, "near")
