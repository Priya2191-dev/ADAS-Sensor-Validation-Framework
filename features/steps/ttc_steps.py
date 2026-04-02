from behave import given, when, then
from ttc import time_to_collision

@given('TTC input distance {distance} and speed {speed}')
def given_ttc(context, distance, speed):
    context.distance = float(distance)
    context.speed = float(speed)

@when('system calculates TTC')
def when_calculate(context):
    context.result = time_to_collision(context.distance, context.speed)

@then('TTC should be {expected}')
def then_output(context, expected):
    if expected == "inf":
        assert context.result == float('inf')
    else:
        assert round(context.result, 2) == round(float(expected), 2)
