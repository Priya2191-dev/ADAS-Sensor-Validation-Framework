# 🚗 ADAS Sensor Validation Framework

##  Overview

The ADAS Sensor Validation Framework is a Python-based automation testing project designed to simulate and validate key functionalities of Advanced Driver Assistance Systems (ADAS).

This project demonstrates:
- Sensor data processing  
- Collision prediction  
- Safety scenario validation  
- Sensor fusion logic  
- Automated testing using Pytest & BDD (Behave)  
- CI/CD integration using GitHub Actions  

##  Objectives

- Simulate ADAS features  
- Validate safety-critical scenarios  
- Automate testing  
- Implement CI/CD  

## Features

- Obstacle Detection:
  
  Detects obstacles within safety threshold.
  
- Collision Warning:
  
  Triggers warning when object is too close, to ensure timely alerts for warning collision.
  
- Safety Scenario Testing:

  Detects high risk driving conditions, validates safety logic, ensure reliability under extreme scenarios.
  
- Sensor Data Validation:

  Validate integrity of sensor data, prevents system failure due to bad inputs, ensure reliable decision making.
  
- Sensor Fusion:

  Improves detection accuracy, reduce sensor noise and uncertainity, enhance decision making.
  
- Time To Collision (TTC):

  Predict collision timing, support warning & braking system, improves safety decision making.
  
- Autonomous Emergency Braking (AEB):

  Reduce collision impact, automate emergency response, enhance vehicle safety system.

## Installation

git clone https://github.com/Priya2191-dev/ADAS-sensor-validation-framework.git

cd ADAS-validation-sensor-framework 

pip install -r requirements.txt

## Interactive Simulation Demo

Run the ADAS sensor validation framework demo

[Open in Google collab] (https://colab.research.google.com/github/Priya2191-dev/ADAS-sensor-validation-framework/blob/main/notebook/ADAS-bus-validation-framework.ipynb)

## Tests

- Automation Testing (Pytest + BDD)
- CI/CD Integration

## Usage

Run Tests:

pytest 

behave  

## CI/CD

GitHub Actions pipeline runs pytest and behave automatically.

## Technologies

- numpy
- pandas
- pytest
- behave

## Author

Priyanka Lale

