from sensors.radar_sensor import RadarSensor
from sensors.camera_sensor import CameraSensor
from validation.sensor_fusion import SensorFusion


def test_obstacle_confirmed():

    radar = RadarSensor()
    camera = CameraSensor()
    fusion = SensorFusion()

    radar_result = radar.get_object_distance(40)
    camera_result = camera.detect_object(True)

    result = fusion.fuse(radar_result, camera_result)

    assert result == "Obstacle Confirmed"


def test_possible_obstacle_radar_only():

    radar = RadarSensor()
    camera = CameraSensor()
    fusion = SensorFusion()

    radar_result = radar.get_object_distance(40)
    camera_result = camera.detect_object(False)

    result = fusion.fuse(radar_result, camera_result)

    assert result == "Possible Obstacle"


def test_no_obstacle():

    radar = RadarSensor()
    camera = CameraSensor()
    fusion = SensorFusion()

    radar_result = radar.get_object_distance(200)
    camera_result = camera.detect_object(False)

    result = fusion.fuse(radar_result, camera_result)

    assert result == "No Obstacle"
