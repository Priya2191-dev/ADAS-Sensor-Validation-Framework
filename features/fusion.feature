Feature: Sensor Fusion

  Scenario: Fuse camera and radar data
    Given camera data "10,20" and radar data "20,30"
    When system performs sensor fusion
    Then fused result should be "15.0,25.0"

  Scenario: Unequal length data
    Given camera data "10,20" and radar data "30"
    When system performs sensor fusion
    Then fused result should be "20.0"

  Scenario: Empty input
    Given camera data "" and radar data ""
    When system performs sensor fusion
    Then fused result should be ""
