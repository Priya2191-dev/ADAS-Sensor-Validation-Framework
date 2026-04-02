# 🚗 ADAS Sensor Validation Framework

## Objective

- Simulate ADAS features
- Validate safety critical scenarios
- Automate testing
- Implement CI/CD
- To generate automated testing reports using allure

##  Overview

The ADAS Sensor Validation Framework is a Python-based automation testing project designed to simulate and validate key functionalities of Advanced Driver Assistance Systems (ADAS).

This project demonstrates:
- Sensor data processing  
- Collision prediction  
- Safety scenario validation  
- Sensor fusion logic  
- Automated testing using Pytest & BDD (Behave)  
- CI/CD integration using GitHub Actions  

## Features

- Obstacle Detection:
  
  Detects obstacles within safety threshold.
  
- Collision Warning:
  
  Triggers warning when object is too close, to ensure timely alerts for warning collision.
  
- Safety Scenario Testing:

  Classifies driving conditions: Safe, Moderate & High Risk.
  
- Sensor Data Validation:

  Validate integrity of sensor data, prevents system failure due to bad inputs, ensure reliable decision making.
  
- Sensor Fusion:

  Combines camera & radar data & validates fused output consistency.Improves detection accuracy, reduce sensor noise and uncertainity,   enhance decision making.
  
- Time To Collision (TTC):

  Calculates collision risk using distance & speed. Handles edge cases (zero speed -> infinity).
  
- Autonomous Emergency Braking (AEB):

  Applies braking when TTC < threshold and validates safety critical decision logic.

## Installations

git clone https://github.com/Priya2191-dev/ADAS-sensor-validation-framework.git

cd ADAS-sensor-validation-framework 

pip install -r requirements.txt

## Tech Stack

- Language: Python
- Testing: Pytest, Behave(BDD)
- CI/CD: Github Actions
- Reporting: Allure Reports

## Testing Strategy

- Unit Testing using Pytest
- Behaviour Driven Testing using Behave
- Edge Case Handling
- Input Validation Testing
- Invalid Case Testing

## CI/CD

- Runs on every push & pull request.
- Executes:

  Pytest(Unit tests)

  Behave(BDD tests)

- Generates:

  Allure reports

  Coverage reports

## Reports & Outputs

- Allure Test Reports
- Behave Execution Logs
- Coverage Report

## Author

Priyanka Lale

