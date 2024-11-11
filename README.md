# EV Battery Health Graph

Graphical display of EV battery health over time

## Installation

Clone the required files with

`git clone git@github.com:tchavei/batteryhealth.git`

Install the required libraries

`pip install -r requirements.txt`

## Configuration

edit the .env file, if needed, to adapt the app to your personal needs.

Explanation:

`STEP=2000` → steps for the X axis. You shouldn't need to change this unless you want more or less granular output.

`FILE_NAME`='data.csv' → name of the file that holds your data.

`THRESHOLD_LEVELS=[70,80]` → What are the threshold levels for each warranty claim window.

`THRESHOLD_LABELS=["3 Year Threshold","8 Year Threshold"]` → Labels for the previous thresholds.

`CHART_LIMITS=[60,100]` → Define minimum and maximum Y axis. Makes a more viewable graph.

## Usage

Update your `data.csv` file with your own readings. The format has to be in form of:

```
km,health
reading_km,SoH
reading_km,SoH
```

For example:

```
km,health
1401,97.47
3129,95.12
5000,94.74
```

Run the aplication from the terminal with:

`python battery_health.py`

## Preset Battery Health Thresholds

Please note that by default the set thresholds (3 years, 8 years) and the corresponding levels (70% and 80%) may vary from EV manufacturer to EV manufacturer.
