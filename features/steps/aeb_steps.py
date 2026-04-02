from behave import given, when, then
from aeb import apply_brakes


@given('AEB TTC is {ttc}')
def given_ttc(context, ttc):
    context.ttc = float(ttc)  


@when('system evaluates braking')
def when_evaluate(context):
    context.result = apply_brakes(context.ttc)


@then('braking should be {expected}')
def then_output(context, expected):
    expected_bool = expected.lower() == "true"
    assert context.result == expected_bool
