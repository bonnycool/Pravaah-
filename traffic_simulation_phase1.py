import time
import random

# Initialize vehicle counts and starvation counters for each road
vehicle_counts = {
    'North': 0,
    'East': 0,
    'South': 0,
    'West': 0
}

# Define correct adjacent roads for permissive left turns to avoid conflicts
adjacent_roads = {
    'North': 'West',
    'East': 'North',
    'South': 'East',
    'West': 'South'
}

# Starvation threshold: how many cycles a road can go without a green light before being prioritized
STARVATION_THRESHOLD = 3
starvation_counters = {road: 0 for road in vehicle_counts}

# Function to simulate vehicle arrival
def update_vehicle_counts():
    for road in vehicle_counts:
        vehicle_counts[road] += random.randint(0, 3)  # Simulate vehicles arriving
        print(f"Vehicle count on {road} road: {vehicle_counts[road]}")

# Function to dynamically determine the highest priority road
def get_priority_road():
    # Sort roads by vehicle count and starvation counter
    sorted_roads = sorted(
        vehicle_counts.keys(),
        key=lambda r: (vehicle_counts[r], starvation_counters[r]),
        reverse=True
    )
    # Return the road with the highest count or one that needs priority to avoid starvation
    for road in sorted_roads:
        if vehicle_counts[road] > 0 or starvation_counters[road] >= STARVATION_THRESHOLD:
            return road
    return None  # In case no eligible road meets criteria

# Traffic light control function with dynamic real-time re-evaluation
def traffic_light_control():
    while True:
        # Update vehicle counts at the beginning of each cycle
        update_vehicle_counts()

        # Dynamically select the road with the highest vehicle count after each green light
        for _ in range(4):  # Attempt to serve each road at least once per cycle
            priority_road = get_priority_road()

            # If no eligible road, skip the cycle
            if not priority_road:
                print("No vehicles to serve. Skipping cycle.")
                break

            # Set green duration based on vehicle count
            green_duration = 10 if vehicle_counts[priority_road] > 5 else 7
            
            # Serve the green light to the priority road
            print(f"{priority_road} Light: Green ON for {green_duration} seconds (straight and right turn)")
            time.sleep(green_duration)

            # Allow permissive left turn on the adjacent road only (to avoid conflicts)
            adjacent_road = adjacent_roads[priority_road]
            if vehicle_counts[adjacent_road] > 0:
                print(f"{adjacent_road} Light: Green ON for 3 seconds (permissive left turn)")
                time.sleep(3)

            # Decrease the vehicle count based on vehicles that passed
            if vehicle_counts[priority_road] > 0:
                vehicle_counts[priority_road] -= random.randint(1, min(vehicle_counts[priority_road], 3))

            # Display yellow and red signals
            print(f"{priority_road} Light: Yellow ON")
            time.sleep(2)
            print(f"{priority_road} Light: Red ON")
            time.sleep(1)

            # Update starvation counters
            for road in starvation_counters:
                if road == priority_road:
                    starvation_counters[road] = 0  # Reset counter for served road
                else:
                    starvation_counters[road] += 1  # Increment counter for other roads

            # Dynamically update vehicle counts again after serving each road
            update_vehicle_counts()
        
        print("Cycle Complete. Restarting...\n")

# Run the traffic light control
traffic_light_control()
