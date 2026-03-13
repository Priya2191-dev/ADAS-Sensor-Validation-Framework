from validation.collision_warning import CollisionWarningSystem

def test_collision_warning():

    system = CollisionWarningSystem()

    result = system.check_warning(20)

    assert result == "WARNING"
