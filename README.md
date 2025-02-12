# Condition Monitoring of hydraulic systems
# Hydraulic Test Rig Dataset
The used dataset can be downloaded under this link: https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems

## Project Overview

The goal of the project is to use different techniques (Machine Learning & Deep Learning) to predict the target "Valve Condition". Other target conditions are also availabe but are not considered in this project.

## Data Details

The dataset contains raw sensor data, recorded by the following sensors:

|Sensor |Physical Quantity |Unit  |Sampling Rate |
|--------|-------------------|-------|---------------|
| PS1 - PS6 | Pressure | bar  | 100 Hz |
| EPS1 | Motor Power | W | 100 Hz |
| FS1 - FS2 | Volume Flow | l/min | 10 Hz |
| TS1 - TS4 | Temperature | °C | 1 Hz |
| VS1 | Vibration | mm/s | 1 Hz |
| CE | Cooling Efficiency (Virtual) | % | 1 Hz |
| CP | Cooling Power (Virtual) | kW | 1 Hz |
| SE | Efficiency Factor | % | 1 Hz |

## Target Condition Annotations
The target condition values are cycle-wise and are annotated in `profile.txt` (tab-delimited). The columns represent the following:

**Valve Condition (%)**: 
   - 100: Optimal switching behavior
   - 90: Small lag
   - 80: Severe lag
   - 73: Close to total failure

## Purpose
The dataset is useful for analyzing and predicting the behavior of hydraulic systems under varying conditions, particularly for failure detection and performance analysis of critical hydraulic components.
