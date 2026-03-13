from validation.aeb_system import AEBSystem


def test_braking_trigger():

    aeb = AEBSystem()

    result = aeb.check_braking(1.5)

    assert result == "BRAKE"


def test_no_braking():

    aeb = AEBSystem()

    result = aeb.check_braking(4)

    assert result == "NO_BRAKE"
