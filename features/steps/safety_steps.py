from behave import given, then
from safety_scenario import safety_scenario

@given('speed is {speed} and obstacle distance is {distance}')
def step_input(context, speed, distance):
    context.speed = int(speed)
    context.distance = int(distance)

@then('safety result should be "{expected}"')
def step_output(context, expected):
    context.result = safety_scenario(context.speed, context.distance)
    assert context.result == expected
