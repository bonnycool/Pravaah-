import time
import random

# Simulated GPIO pin states for each traffic light direction
gpio_state = {
    "North_Green_Left": False,
    "North_Green_Right": False,
    "North_Green_Straight": False,
    "North_Yellow": False,
    "North_Red": False,
    "East_Green_Left": False,
    "East_Green_Right": False,
    "East_Green_Straight": False,
    "East_Yellow": False,
    "East_Red": False,
    "South_Green_Left": False,
    "South_Green_Right": False,
    "South_Green_Straight": False,
    "South_Yellow": False,
    "South_Red": False,
    "West_Green_Left": False,
    "West_Green_Right": False,
    "West_Green_Straight": False,
    "West_Yellow": False,
    "West_Red": False
}

# Function to set the GPIO pin state
def set_gpio(pin, state):
    gpio_state[pin] = state
    print(f"GPIO {pin} set to {'HIGH' if state else 'LOW'}")

# Function to reset all GPIO pins to LOW (OFF)
def clear_all_gpio():
    for pin in gpio_state.keys():
        set_gpio(pin, False)

# Simulated vehicle counts for each road
vehicle_counts = {
    'North': 0,
    'East': 0,
    'South': 0,
    'West': 0
}

# Starvation counters to prevent starvation for each road
starvation_counters = {
    'North': 0,
    'East': 0,
    'South': 0,
    'West': 0
}
STARVATION_THRESHOLD = 3  # Number of cycles a road can be skipped before gaining priority

# Function to simulate random vehicle arrivals at each road
def update_vehicle_counts():
    for road in vehicle_counts:
        vehicle_counts[road] += random.randint(0, 3)
        print(f"Vehicle count on {road} road: {vehicle_counts[road]}")

# Function to determine the priority road based on vehicle counts and starvation counters
def get_priority_road():
    # Increase priority for roads that have been starved
    prioritized_roads = sorted(
        vehicle_counts.keys(),
        key=lambda r: (vehicle_counts[r], starvation_counters[r]),
        reverse=True
    )
    
    # Select the highest priority road
    for road in prioritized_roads:
        # Prioritize based on vehicle count or starvation threshold
        if vehicle_counts[road] > 0 or starvation_counters[road] >= STARVATION_THRESHOLD:
            return road
    return None  # In case no road meets the criteria

# Function to control each lane with prioritization
def control_lane(road):
    # Define GPIO pins for each green light direction and yellow/red lights
    green_left = f"{road}_Green_Left"
    green_straight = f"{road}_Green_Straight"
    green_right = f"{road}_Green_Right"
    yellow_pin = f"{road}_Yellow"
    red_pin = f"{road}_Red"

    # Clear all lights to start with a clean slate
    clear_all_gpio()

    # Serve left turn
    set_gpio(green_left, True)
    print(f"{road} Light: Green ON for left turn")
    time.sleep(5)
    set_gpio(green_left, False)

    # Serve straight
    set_gpio(green_straight, True)
    print(f"{road} Light: Green ON for straight")
    time.sleep(7)
    set_gpio(green_straight, False)

    # Serve right turn
    set_gpio(green_right, True)
    print(f"{road} Light: Green ON for right turn")
    time.sleep(5)
    set_gpio(green_right, False)

    # Set yellow for transition
    set_gpio(yellow_pin, True)
    print(f"{road} Light: Yellow ON for 2 seconds")
    time.sleep(2)
    set_gpio(yellow_pin, False)

    # Set red after yellow
    set_gpio(red_pin, True)
    print(f"{road} Light: Red ON")
    time.sleep(1)

# Traffic light control logic with dynamic prioritization and starvation prevention
def traffic_light_control():
    while True:
        update_vehicle_counts()  # Update vehicle counts before each cycle
        
        # Determine the priority road based on the highest vehicle count or starvation counter
        priority_road = get_priority_road()

        # Control the traffic lights for the priority road
        print(f"Serving the priority road: {priority_road}")
        control_lane(priority_road)

        # Reset starvation counter for the served road, increment others
        for road in starvation_counters:
            if road == priority_road:
                starvation_counters[road] = 0
            else:
                starvation_counters[road] += 1

        # Update vehicle counts again to adapt to changing conditions
        update_vehicle_counts()

        print("Cycle Complete. Restarting...\n")

# Run the traffic light control simulation
if __name__ == "__main__":
    traffic_light_control()
