from behave import given, when, then
from sensor_data import validate_sensor_data


# Helper function
def convert_to_list(data):
    #If empty string -> return empty list
    if data.strip() == "":
        return []

    #Convert "10, 5, 3" into [10.0, 5.0, 3.0]
    return [float(x) for x in data.split(",")]

@given('sensor values "{data}"')
def given_data(context, data):
    context.data = convert_to_list(data)

@given('sensor values ""')
def given_empty(context):
    context.data = []

@when('system validates sensor data')
def when_validate(context):
    context.result = validate_sensor_data(context.data)

@then('sensor data should be valid')
def then_valid(context):
    assert context.result is True

@then('sensor data should be invalid')
def then_invalid(context):
    assert context.result is False
