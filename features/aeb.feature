Feature: Autonomous Emergency Braking

  Scenario: Apply brakes when TTC is low
    Given AEB TTC is 2.5
    When system evaluates braking
    Then braking should be "True"

  Scenario: Do not apply brakes when TTC is high
    Given AEB TTC is 5
    When system evaluates braking
    Then braking should be "False"

  Scenario: Boundary condition
    Given AEB TTC is 3
    When system evaluates braking
    Then braking should be "False"
