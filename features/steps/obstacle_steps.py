from behave import given, when, then
from obstacle_detection import detect_obstacles


def parse_input(data):
    if data.strip() == "":
        return []
    return list(map(float, data.split(",")))


@given('sensor data "{data}"')
def step_given_sensor_data(context, data):
    context.sensor_data = parse_input(data)


@when('threshold is {threshold:g}')
def step_when_threshold(context, threshold):
    context.result = detect_obstacles(context.sensor_data, threshold)


@then('obstacles should be "{expected}"')
def step_then_obstacles(context, expected):
    expected_list = parse_input(expected)
    assert context.result == expected_list
