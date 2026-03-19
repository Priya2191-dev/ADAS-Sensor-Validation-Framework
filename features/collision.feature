Feature: Collision Warning

  Scenario: Trigger collision warning
    Given distance is 3
    Then collision warning should be True
