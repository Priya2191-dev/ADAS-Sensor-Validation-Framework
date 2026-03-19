from src.aeb import apply_brakes

def test_brake_applied():
    assert apply_brakes(2, 3) is True

def test_brake_not_applied():
    assert apply_brakes(5, 3) is False

def test_brake_boundary():
    assert apply_brakes(3, 3) is False

def test_brake_zero_ttc():
    assert apply_brakes(0, 3) is True
