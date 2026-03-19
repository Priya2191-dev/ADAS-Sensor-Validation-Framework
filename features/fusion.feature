Feature: Sensor Fusion

  Scenario: Fuse camera and radar data
    Given camera data "10,20" and radar data "20,30"
    Then fused result should be "15.0,25.0"
