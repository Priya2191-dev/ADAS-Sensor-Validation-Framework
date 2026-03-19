from behave import given, then
from sensor_data import validate_sensor_data

@given('sensor values "{data}"')
def step_input(context, data):
    context.data = list(map(int, data.split(',')))

@then('sensor data should be valid')
def step_output(context):
    assert validate_sensor_data(context.data) is True
