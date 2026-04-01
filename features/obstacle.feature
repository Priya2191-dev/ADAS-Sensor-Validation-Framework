Feature: Obstacle Detection

  Scenario: Detect obstacles below threshold
    Given sensor data "10,2,3,7"
    When threshold is 5
    Then obstacles should be "2,3"

  Scenario: No obstacles detected
    Given sensor data "10,8,6"
    When threshold is 5
    Then obstacles should be ""

  Scenario: All values are obstacles
    Given sensor data "1,2,3"
    When threshold is 5
    Then obstacles should be "1,2,3"

  Scenario: Empty sensor data
    Given sensor data ""
    When threshold is 5
    Then obstacles should be ""
