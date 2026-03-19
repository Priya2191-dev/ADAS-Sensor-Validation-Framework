Feature: Autonomous Emergency Braking

  Scenario: Apply brakes when TTC is low
    Given TTC is 2.5
    Then braking should be True
