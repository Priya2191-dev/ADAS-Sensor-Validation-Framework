from behave import given, then
from safety_scenario import safety_scenario

@given('speed is {speed:d} and obstacle distance is {distance:d}')
def step_input(context, speed, distance):
    context.speed = speed
    context.distance = distance

@then('safety result should be "{expected}"')
def step_output(context, expected):
    result = safety_scenario(context.speed, context.distance)
    assert result == expected
