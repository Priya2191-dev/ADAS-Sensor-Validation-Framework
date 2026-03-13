class ScenarioGenerator:

    def front_collision_scenario(self):
        return {
            "vehicle_speed": 60,
            "obstacle_distance": 20
        }

    def safe_distance_scenario(self):
        return {
            "vehicle_speed": 60,
            "obstacle_distance": 80
        }
