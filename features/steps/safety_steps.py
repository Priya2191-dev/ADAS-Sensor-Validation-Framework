from behave import given, when, then
from safety_scenario import safety_scenario


@given('speed is {speed:d} and obstacle distance is {distance:d}')
def step_given_input(context, speed, distance):
    context.speed = speed
    context.distance = distance

@when('system evaluates safely')
def step_when_evaluate(context):
    context.result = safety_scenario(context.speed, context.distance)

@then('safety result should be "{expected}"')
def step_then_output(context, expected):
    assert context.result == expected
