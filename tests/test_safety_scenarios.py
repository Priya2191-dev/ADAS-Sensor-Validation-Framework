from simulation.scenario_generator import ScenarioGenerator
from validation.collision_warning import CollisionWarningSystem

def test_safety_scenario():

    scenario = ScenarioGenerator()
    warning = CollisionWarningSystem()

    case = scenario.front_collision_scenario()

    result = warning.check_warning(case["obstacle_distance"])

    assert result == "WARNING"
