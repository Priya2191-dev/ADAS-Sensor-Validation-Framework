Feature: Obstacle Detection

  Scenario: Detect obstacles below threshold
    Given sensor data "10,2,3,7"
    When threshold is 5
    Then obstacles should be "2,3"
