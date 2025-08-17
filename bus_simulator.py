import time
import random
import json

# List of 5 buses
buses = ["Bus_200", "Bus_201", "Bus_202", "Bus_203", "Bus_204"]

# Starting location (somewhere in Delhi)
start_lat = 28.4595
start_lon = 77.0266

# Dictionary for bus locations
locations = {}

# Initialize all buses at the start location
for bus in buses:
    locations[bus] = {"lat": start_lat, "lon": start_lon}

# Keep updating the location
while True:
    for bus in locations:
        # Add a small random change to lat/lon
        delta_lat = random.uniform(-0.0005, 0.0005)
        delta_lon = random.uniform(-0.0005, 0.0005)

        # Update the bus location
        locations[bus]["lat"] += delta_lat
        locations[bus]["lon"] += delta_lon

    # Save to a JSON file
    with open("bus_locations.json", "w") as file:
        json.dump(locations, file, indent=4)

    print("Bus locations updated.")
    
    # Wait for 2 seconds before next update
    time.sleep(2)
