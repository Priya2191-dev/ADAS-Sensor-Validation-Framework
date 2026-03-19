from behave import given, when, then
from obstacle_detection import detect_obstacles

@given('sensor data "{data}"')
def step_sensor_data(context, data):
    context.data = list(map(int, data.split(',')))

@when('threshold is {threshold:d}')
def step_threshold(context, threshold):
    context.result = detect_obstacles(context.data, threshold)

@then('obstacles should be "{expected}"')
def step_validate(context, expected):
    expected_list = list(map(int, expected.split(',')))
    assert context.result == expected_list
