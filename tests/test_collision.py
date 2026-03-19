from collision_warning import collision_warning

def test_collision_true():
    assert collision_warning(3, 4) is True

def test_collision_false():
    assert collision_warning(6, 4) is False

def test_collision_equal_boundary():
    assert collision_warning(4, 4) is False

def test_collision_zero_distance():
    assert collision_warning(0, 4) is True
