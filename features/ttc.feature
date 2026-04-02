Feature: Time To Collision

  Scenario: Calculate TTC
    Given collision distance 100 and collision speed 20
    When system calculates TTC
    Then TTC should be 5.0

  Scenario: Zero speed
    Given collision distance 100 and collision speed 0
    When system calculates TTC
    Then TTC should be inf

  Scenario: Zero distance
    Given collision distance 0 and collision speed 20
    When system calculates TTC
    Then TTC should be 0.0
