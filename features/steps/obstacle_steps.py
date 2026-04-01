from behave import given, when, then
from obstacle_detection import detect_obstacles


def parse_input(data):
    if data.strip() == "":
        return []
    return list(map(float, data.split(",")))

@given('sensor data "{data}"')
def given_sensor_data(context, data):
    context.sensor_data = parse_input(data)

@given('sensor data')
def given_empty_sensor_data(context):
    context.sensor_data = []

@when('threshold is {threshold}')
def when_threshold(context, threshold):
    context.result = detect_obstacles(context.sensor_data, threshold)

@then('obstacles should be "{expected}"')
def then_obstacles(context, expected):
    expected_list = parse_input(expected)
    assert context.result == expected_list
