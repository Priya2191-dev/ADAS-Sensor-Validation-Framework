from behave import given, then
from src.ttc import time_to_collision

@given('distance {distance:d} and speed {speed:d}')
def step_input(context, distance, speed):
    context.distance = distance
    context.speed = speed

@then('TTC should be {expected:f}')
def step_output(context, expected):
    result = time_to_collision(context.distance, context.speed)
    assert round(result, 2) == round(expected, 2)
