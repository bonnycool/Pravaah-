  # Intelligent Traffic Control System 🚦

This project implements a **Dynamic and Intelligent Traffic Control System** using a **Deep Double Q-Network (D3QN)** to optimize traffic flow at a four-way intersection. The system dynamically adjusts traffic lights based on real-time vehicle counts, prioritizes roads with heavy traffic, prevents starvation, and incorporates energy-saving and safety features.

---

## **Features**

1. **Dynamic Traffic Signal Management**:  
   Adjusts signal timings based on real-time traffic data to ensure smooth flow.

2. **Prioritization Algorithm**:  
   Reduces congestion by prioritizing roads with higher vehicle counts and preventing starvation.

3. **Night-Time Safety Mode**:  
   - Switches off traffic lights during low-traffic hours to save energy.  
   - Activates flashing lights to warn speeding vehicles approaching from side roads.

4. **Emergency Vehicle Priority**:  
   Detects emergency vehicles and switches to an emergency mode to provide them with a green signal.

5. **High-Beam Detection at Night**:  
   Detects vehicles with high-beam headlights and warns drivers to dim their lights, improving safety for oncoming traffic.

6. **Reinforcement Learning (D3QN)**:  
   Utilizes Deep Double Q-Learning to dynamically learn and optimize traffic light decisions over time.

---

## **Technologies Used**

- **Languages**: Python
- **Libraries**: 
  - TensorFlow for the D3QN model
  - OpenCV for vehicle detection
  - NumPy for data manipulation
- **Hardware**: Raspberry Pi (for GPIO control and real-time deployment)
- **Algorithms**: 
  - Deep Reinforcement Learning (D3QN)
  - Dynamic prioritization and starvation prevention
- **Tools**: TensorFlow Lite for lightweight inference on Raspberry Pi

---

<!--## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/intelligent-traffic-control-system.git
   cd intelligent-traffic-control-system
-->
