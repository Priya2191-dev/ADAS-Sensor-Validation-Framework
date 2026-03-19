from behave import given, then
from aeb import apply_brakes

@given('TTC is {ttc:f}')
def step_input(context, ttc):
    context.ttc = ttc

@then('braking should be {expected}')
def step_output(context, expected):
    result = apply_brakes(context.ttc)
    assert result == (expected == "True")
