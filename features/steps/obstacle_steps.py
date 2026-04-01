from behave import given, when, then
from obstacle_detection import detect_obstacles


# Helper function
def convert_to_list(data):
    # If empty string -> return empty list
    if data.strip() == "":
        return []

    # Convert "10,2,3" -> [10.0, 2.0, 3.0]
    return [float(x) for x in data.split(",")]

@given('sensor data "{data}"')
def given_sensor_data(context, data):
    context.sensor_data = convert_to_list(data)

@given('sensor data ""')
def given_empty_data(context):
    context.sensor_data = []

@when('threshold is {threshold}')
def when_threshold(context, threshold):
    context.result = detect_obstacles(context.sensor_data, float(threshold))

@then('obstacles should be "{expected}"')
def then_obstacles(context, expected):
    expected_list = convert_to_list(expected)
    assert context.result == expected_list

@then('obstacles should be ""')
def then_empty(context):
    assert context.result == []
