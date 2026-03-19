Feature: Time To Collision

  Scenario: Calculate TTC
    Given distance 100 and speed 20
    Then TTC should be 5.0
