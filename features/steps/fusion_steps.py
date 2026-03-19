from behave import given, then
from src.sensor_fusion import sensor_fusion

@given('camera data "{camera}" and radar data "{radar}"')
def step_input(context, camera, radar):
    context.camera = list(map(int, camera.split(',')))
    context.radar = list(map(int, radar.split(',')))

@then('fused result should be "{expected}"')
def step_output(context, expected):
    expected_list = list(map(float, expected.split(',')))
    result = sensor_fusion(context.camera, context.radar)
    assert result == expected_list
