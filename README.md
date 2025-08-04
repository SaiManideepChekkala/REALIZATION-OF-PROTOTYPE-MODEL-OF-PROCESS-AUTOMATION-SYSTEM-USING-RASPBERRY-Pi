
# 🔧 Realization of Prototype Model of Process Automation System Using Raspberry Pi

## 🎯 Objective

The primary goal of this project is to **monitor and maintain server rack temperature** through an automated system built on **Raspberry Pi**.

Key features include:
- 🌡️ **Real-time monitoring** of the system (CPU/server) temperature.
- 📉 **Threshold-based control**: When temperature crosses a defined limit, an **automatic response is triggered**—such as opening server doors or switching on cooling mechanisms.
- 💡 Initially, the prototype was tested using the **Raspberry Pi’s own CPU temperature**, simulating sensor input. This forms the foundation for future development with actual server environments.
- 🏭 The design can be extended into **data center automation** for optimized temperature control and server safety.
---
## 🧩 System Modules

### 🧪 1. Temperature Monitoring and Client Notification (Project1)

This module demonstrates:
- Raspberry Pi acting as a **sensor node**.
- Continuous temperature readings (initially from the Pi's CPU).
- Transmission of these readings to a **remote client** for logging and alerts.
- **Threshold logic** that simulates an action trigger—like door opening—when temperature exceeds safe limits.

**Files:**
- `sensor master socket.py`: Reads temperature and acts as a server.
- `client_main.py`: A client app that receives real-time temperature updates.
- `temperature_test.py`: Tests the CPU temperature reading and logic.

### 💡 2. Remote LED Control System (Project2)

This part simulates:
- An actuator system (e.g., fan, alarm, or door release mechanism).
- Remotely toggled via a GUI.
- Implemented using **Kivy framework** with a visually appealing interface.

**Files:**
- `main.py`: Main controller script for GUI interface.
- `switch.kv`: Layout file used by Kivy to define UI elements.
- `readcodeled.py`: Backend code controlling the physical LED (or actuator).
- `LED ON.png / LED OFF.png`: Output screenshots simulating control states.
---
## 🧠 Key Features

- 🔁 **Client-Server Architecture**  
  Uses Python's socket programming to enable communication between sensor systems and client interfaces.

- 🌡️ **Real-Time Temperature Monitoring**  
  Captures live data from the sensor (initially Raspberry Pi's CPU) and transmits it to a remote GUI client.

- 💡 **LED Control Interface**  
  GUI-based LED ON/OFF control using the **Kivy framework** for intuitive user interaction and feedback.

- 📊 **Visual Documentation**  
  Includes output screenshots, a detailed project report (`.docx`), and presentation slides (`.pptx`) to explain architecture, flow, and results.
---
## 🧱 Components Used

| Component                  | Purpose                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| 🧠 **Raspberry Pi**        | Acts as sensor node and central controller.                            |
| 🌡️ **CPU Temperature (simulated sensor)** | Initially used as a proxy for environment monitoring.           |
| 🧪 **Future Sensor: DHT11/LM35** | For expansion into real-world thermal sensing in server racks.     |
| 💡 **LED**                | Simulates actuators like door locks or cooling fans.                   |
| 📟 **Kivy UI**             | Builds interactive interface for actuator control.                     |
| 🌐 **Python Socket Programming** | Enables real-time client-server communication.                      |

---
## ⚙️ Working Mechanism

1. **Server Initialization**  
   Raspberry Pi reads internal temperature and broadcasts it to connected clients via TCP.

2. **Threshold Detection**  
   A set temperature threshold is compared against the current temperature.

3. **Trigger Action**  
   If the threshold is crossed:
   - A control signal is sent to open a virtual "server door" (currently represented by LED ON).
   - Clients are updated immediately.

4. **User Interface**  
   Kivy-based app enables manual override or control of the LED (i.e., actuator).
---

## 🚀 How to Run

### 🔧 Install Dependencies

Make sure Python 3 is installed. Then install required packages:

```bash
pip install kivy
```


### 💡 Run LED Control System (Project2)

```bash
python3 main.py
```


### 🌡️ Run Temperature Monitoring System (Project1)

**Start the server:**

```bash
python3 sensor\ master\ socket.py
```

**Start the client:**

```bash
python3 client_main.py
```
---

## 📦 Project Contents

```
Manideep_Yashwanth/
├── Project Report.docx & PPTX – Explanation, flowcharts, and circuit design
├── Project1(temp) – CPU temperature monitoring using sockets
├── Project2(LED) – GUI and actuator simulation
├── Output Images – Screenshots of working UI and backend
```
---
## 🚀 Future Enhancements

- ✅ Replace CPU sensor with external DHT11/LM35 temperature sensors.
- 🧰 Interface real actuators like **servo-controlled doors**, **fans**, or **cooling systems**.
- 🌐 Add **cloud connectivity** for monitoring server racks remotely.
- 🔐 Include **authentication & logging** for real-world data center implementation.

---
## 🙌 Acknowledgments

Developed by:
- **Sai Manideep C.**

Special thanks to mentors and faculty who supported this embedded-IoT hybrid prototype.
