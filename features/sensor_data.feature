Feature: Sensor Data Validation

  Scenario: Validate correct sensor data
    Given sensor values "10,5,3"
    Then sensor data should be valid
