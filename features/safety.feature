Feature: Safety Scenario

  Scenario: High risk condition
    Given speed is 70 and obstacle distance is 3
    Then safety result should be "HIGH RISK"
