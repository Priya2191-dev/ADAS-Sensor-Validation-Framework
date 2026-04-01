Feature: Collision Warning

  Scenario: Trigger collision warning
    Given distance is 3
    When system checks collision
    Then collision warning should be "True"

  Scenario: No collision warning
    Given distance is 6
    When system checks collision
    Then collision warning should be "False"

  Scenario: Boundary condition
    Given distance is 4
    When system checks collision
    Then collision warning should be "False"

  Scenario: Zero distance
    Given distance is 0
    When system checks collision
    Then collision warning should be "True"
