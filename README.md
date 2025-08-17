# Bus Location Simulator

This project simulates the real-time locations of multiple buses starting from a fixed location (somewhere in Delhi). The bus locations are updated periodically and saved to a JSON file.

## Features

- Simulates movement of 5 buses.
- Updates bus locations randomly around a starting point.
- Saves the updated locations to a JSON file (`bus_locations.json`) after each update.
- Can be used for testing or demo purposes where live bus location data is required.

## Files

- `bus_simulator.py`: The main script that runs the bus location simulation.
- `bus_locations.json`: JSON file where the latest bus locations are saved.
- `README.md`: This file.

## How to Run

1. Make sure you have Python installed (Python 3.x recommended).
2. Clone this repository or download the files.
3. Open terminal or command prompt in the project directory.
4. Run the simulator script:

   ```bash
   python bus_simulator.py
