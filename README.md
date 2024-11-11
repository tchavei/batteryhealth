# EV Battery Health Graph

Graphical display of EV battery health over time

## Installation

Clone the required files with

`git clone git@github.com:tchavei/batteryhealth.git`

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

Please note that by default the set thresholds (3 years, 8 years) and the corresponding levels
