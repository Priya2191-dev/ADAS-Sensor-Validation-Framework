from behave import given, when, then
from collision_warning import collision_warning


@given('distance is {distance}')
def given_distance(context, distance):
    context.distance = float(distance)

@when('system checks collision')
def when_check(context):
    context.result = collision_warning(context.distance)

@then('collision warning should be "{expected}"')
def then_result(context, expected):
    # Convert string → boolean
    expected_bool = expected.lower() == "true"
    assert context.result == expected_bool
