Feature: Obstacle Detection
  Scenario: Detect obstacles
    Given sensor data "10,2,3"
    When threshold is 5
    Then obstacles should be "2,3"
