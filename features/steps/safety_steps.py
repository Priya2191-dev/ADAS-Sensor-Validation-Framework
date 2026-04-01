from behave import given, when, then
from safety_scenario import safety_scenario


@given('speed is {speed} and obstacle distance is {distance}')
def given_input(context, speed, distance):
    context.speed = int(speed)
    context.distance = int(distance)

@when('system evaluates safely')
def when_evaluate(context):
    context.result = safety_scenario(context.speed, context.distance)

@then('safety result should be "{expected}"')
def then_output(context, expected):
    assert context.result == expected
