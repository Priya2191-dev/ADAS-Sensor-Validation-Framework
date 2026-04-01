Feature: Sensor Data Validation

  Scenario: Validate correct sensor data
    Given sensor values "10,5,3"
    When system validates sensor data
    Then sensor data should be valid

  Scenario: Detect invalid sensor data
    Given sensor values "10,-1,3"
    When system validates sensor data
    Then sensor data should be invalid

  Scenario: Empty sensor data
    Given sensor values ""
    When system validates sensor data
    Then sensor data should be valid
