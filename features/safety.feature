Feature: Safety Scenario

  Scenario: High risk condition
    Given speed is 70 and obstacle distance is 3
    When system evaluates safely
    Then safety result should be "HIGH RISK"

  Scenario: Safe condition
    Given speed is 30 and obstacle distance is 10
    When system evaluates safely
    Then safety result should be "SAFE"

  Scenario: Moderate condition
    Given speed is 60 and obstacle distance is 5
    When system evaluates safely
    Then safety result should be "MODERATE"

  Scenario: Edge condition
    Given speed is 50 and obstacle distance is 6
    When system evaluates safely
    Then safety result should be "MODERATE"
