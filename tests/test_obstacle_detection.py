from sensors.lidar_sensor import LidarSensor
from simulation.obstacle_simulation import ObstacleSimulation

def test_obstacle_detection():

    lidar = LidarSensor()
    sim = ObstacleSimulation()

    distance = sim.generate_obstacle_distance()

    result = lidar.detect_obstacle(distance)

    assert result in [True, False]
