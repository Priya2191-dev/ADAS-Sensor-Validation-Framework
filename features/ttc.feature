Feature: Time To Collision

  Scenario: Calculate TTC
    Given TTC input distance 100 and speed 20
    When system calculates TTC
    Then TTC should be 5.0

  Scenario: Zero speed
    Given TTC input distance 100 and speed 0
    When system calculates TTC
    Then TTC should be inf

  Scenario: Zero distance
    Given TTC input distance 0 and speed 20
    When system calculates TTC
    Then TTC should be 0.0
