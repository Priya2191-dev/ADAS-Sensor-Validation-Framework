from behave import given, when, then
from aeb import apply_brakes


@given('AEB TTC is {ttc:f}')
def step_given_ttc(context, ttc):
    context.ttc = ttc

@when('system evaluates braking')
def step_when_eval(context):
    context.result = apply_brakes(context.ttc)

@then('braking should be "{expected}"')
def step_then_output(context, expected):
    expected_bool = expected.lower() == "true"
    assert context.result == expected_bool
