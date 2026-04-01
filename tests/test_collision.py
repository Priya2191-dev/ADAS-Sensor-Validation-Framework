import pytest
from collision_warning import collision_warning


def test_collision_true():
    assert collision_warning(3, 4) is True

def test_collision_false():
    assert collision_warning(6, 4) is False

def test_collision_equal_boundary():
    assert collision_warning(4, 4) is False

def test_collision_zero_distance():
    assert collision_warning(0, 4) is True

@pytest.mark.parametrize("distance, safe_distance, expected", [
    (3, 4, True),
    (6, 4, False),
    (4, 4, False),
    (0, 4, True),
])
def test_collision_cases(distance, safe_distance, expected):
    assert collision_warning(distance, safe_distance) == expected

def test_invalid_distance_type():
    with pytest.raises(TypeError):
        collision_warning("3", 4)

def test_invalid_safe_distance_type():
    with pytest.raises(TypeError):
        collision_warning(3, "4")

def test_negative_distance():
    with pytest.raises(ValueError):
        collision_warning(-1, 4)
