from behave import given, when, then
from sensor_fusion import sensor_fusion


# Helper function
def convert_to_list(data):
    # If empty string -> return empty list
    if data.strip() == "":
        return []

    # Convert "15, 20" -> [15.0, 20.0]
    return [float(x) for x in data.split(",")]

@given('camera data "{camera}" and radar data "{radar}"')
def step_given_input(context, camera, radar):
    context.camera = convert_to_list(camera)
    context.radar = convert_to_list(radar)

@given('camera data "" and radar data ""')
def step_given_empty(context):
    context.camera = []
    context.radar = []

@when('system performs sensor fusion')
def step_when_fusion(context):
    context.result = sensor_fusion(context.camera, context.radar)

@then('fused result should be "{expected}"')
def step_then_output(context, expected):
    expected_list = convert_to_list(expected)
    assert context.result == expected_list

@then('fused result should be ""')
def step_then_empty(context):
    assert context.result == []
