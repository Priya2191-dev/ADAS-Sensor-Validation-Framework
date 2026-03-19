Feature: Collision Warning
  Scenario: Trigger warning
    Given distance is 3
    Then collision warning should be True
