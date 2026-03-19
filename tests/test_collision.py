from src.collision_warning import collision_warning

def test_collision():
    assert collision_warning(3) is True
