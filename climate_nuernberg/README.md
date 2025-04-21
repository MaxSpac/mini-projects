# Weather Visualization Nuremberg (2023-2025)

## Overview
This project visualizes monthly weather data for Nuremberg (Station 10763) from September 2023 to February 2025 using Python and Matplotlib. The data includes:
- Middle Temperature (°C) (`TMM`)
- Sun Hours (h) (`SOS`)
- Rain Days (Days) (`NMM`)
- Rainfall (mm) (`RSS`)

The visualization combines line plots and bar charts to display these parameters over time, with annotations highlighting the maximum values for each metric.

## Features
- **Dual Axes:** Left axis shows temperature and rain days; right axis shows sun hours and rainfall.
- **Consistent Line Visibility:** Lines maintain full opacity (`alpha=1.0`) over bars, ensuring no transparency blending.
- **Data Source:** Monthly weather values from Station 10763 (Nuremberg).
- **Output:** Plot saved as `wetter_nuernberg_full_2023_2025.png`.

## Requirements
- Python 3.x
- Matplotlib (`pip install matplotlib`)

## Usage
1. Ensure the required libraries are installed.
2. Run the script (e.g., `python weather_nuremberg.py`).
3. The plot will display and save automatically.
