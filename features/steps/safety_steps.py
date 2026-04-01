from behave import given, when, then
from safety_scenario import safety_scenario


@given('speed is {speed:d} and obstacle distance is {distance:d}')
def given_input(context, speed, distance):
    context.speed = speed
    context.distance = distance

@when('system evaluates safely')
def when_evaluate(context):
    context.result = safety_scenario(context.speed, context.distance)

@then('safety result should be "{expected}"')
def then_output(context, expected):
    assert context.result == expected
