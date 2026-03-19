from behave import given, then
from collision_warning import collision_warning

@given('distance is {distance:d}')
def step_distance(context, distance):
    context.distance = distance

@then('collision warning should be {expected}')
def step_collision(context, expected):
    result = collision_warning(context.distance)
    assert result == (expected == "True")
